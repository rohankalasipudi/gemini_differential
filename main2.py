import streamlit as st
import json
import requests
import time
from symptoms import analyze_symptoms, DATA
from treatments import TREATMENTS

def get_standardized_symptoms(user_input, available_symptoms):
    """
    Uses a language model API to interpret natural language symptoms and match them
    to a standardized list of symptoms.
    """
    st.info("Thinking like a medical language processor... this may take a moment.")
    
    # Prompt the LLM to act as a language processor and match symptoms
    prompt = f"""
    You are a medical language processor. Your task is to extract and standardize symptoms from a user's text.
    
    Available Symptoms List (do not use any symptoms not on this list):
    {', '.join(available_symptoms)}
    
    Instructions:
    1. Read the user's input carefully.
    2. Identify any symptoms mentioned or implied by the text.
    3. Match these to the closest possible symptom from the provided Available Symptoms List.
    4. If a symptom is not a direct match but is a clear synonym or related concept, use the official symptom name. For example, "headache" matches "headache," and "sore tummy" matches "abdominal pain."
    5. Do not hallucinate or create new symptoms. Only use symptoms from the provided list.
    6. Return a comma-separated list of the standardized symptoms. Do not include any other text or explanation in the response. If no symptoms match, return an empty string.
    
    User Input: "{user_input}"
    Standardized Symptoms:
    """

    chat_history = []
    chat_history.append({"role": "user", "parts": [{"text": prompt}]})

    payload = {
        "contents": chat_history,
        "generationConfig": {
            "responseMimeType": "application/json",
            "responseSchema": {
                "type": "ARRAY",
                "items": { "type": "STRING" }
            }
        }
    }
    
    # This is a placeholder for a real API key which is automatically provided in the environment.
    api_key = ""
    api_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-05-20:generateContent?key={api_key}"
    
    max_retries = 5
    for i in range(max_retries):
        try:
            response = requests.post(api_url, headers={'Content-Type': 'application/json'}, data=json.dumps(payload), timeout=30)
            response.raise_for_status() # Raise an error for bad status codes
            
            result = response.json()
            if result.get('candidates') and result['candidates'][0].get('content'):
                text = result['candidates'][0]['content']['parts'][0]['text']
                # The response is already a JSON string, so we can parse it directly.
                parsed_symptoms = json.loads(text)
                return [s.lower().strip() for s in parsed_symptoms]
            else:
                st.error("API response was empty or malformed.")
                return []
                
        except requests.exceptions.RequestException as e:
            st.error(f"Error calling the API: {e}")
            if i < max_retries - 1:
                st.warning(f"Retrying... ({i+1}/{max_retries})")
                time.sleep(2 ** i)  # Exponential backoff
            else:
                st.error("Failed to connect to the API after multiple retries.")
                return []
    return []

def main():
    """
    Main function for the Streamlit application.
    """
    st.set_page_config(
        page_title="USMLE Prep Companion",
        page_icon="🧠",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    st.title("🧠 USMLE Prep: Differential Diagnosis & Treatment")
    
    st.markdown("""
        _This tool helps you practice differential diagnosis and treatment planning for the USMLE. Enter symptoms in natural language, and the AI will match them to standardized medical terms, providing a comprehensive analysis._
    """)

    # USMLE-specific tips and instructions
    st.sidebar.header("💡 USMLE Prep Tips")
    st.sidebar.markdown("""
        1.  **Natural Language Input:** Describe a patient's symptoms as you might read them in a clinical vignette. The app will interpret your text.
        2.  **Focus on Key Findings:** Think about the most important signs and symptoms that point to a specific diagnosis.
        3.  **Review Treatment Plans:** Pay close attention to the first-line therapies and differentiating factors. This is crucial for exam questions.
        4.  **Broaden Your Differentials:** If the initial result isn't what you expected, try adding or removing symptoms to see how the differential list changes.
    """)

    # User input for symptoms
    user_input = st.text_area(
        "Describe the patient's symptoms in a short sentence or list.",
        height=100,
        placeholder="e.g., A 30-year-old male presents with severe chest pain, shortness of breath, and a cough. He reports recent travel."
    )

    # A button to trigger the analysis
    if st.button("Analyze Symptoms"):
        if not user_input:
            st.warning("Please enter at least one symptom to run the analysis.")
        else:
            with st.spinner("Analyzing your symptoms and generating a diagnosis..."):
                # Use the LLM to get standardized symptoms from the user's natural language input
                available_symptoms = DATA["symptoms"]
                standardized_symptoms = get_standardized_symptoms(user_input, available_symptoms)
                
                if not standardized_symptoms:
                    st.error("The AI could not identify any matching symptoms from your description. Please try a different wording.")
                    return
                
                st.markdown(f"**Identified Symptoms:** _{', '.join(standardized_symptoms)}_")
                
                disease_scores = analyze_symptoms(standardized_symptoms)

                if not disease_scores:
                    st.error("No matching diseases found for the provided symptoms. Please try again.")
                else:
                    # Sort the diseases by score in descending order and display the top results.
                    sorted_diseases = sorted(disease_scores.items(), key=lambda item: item[1]['score'], reverse=True)
                    
                    st.subheader("Differential Diagnosis and Treatment Plan")
                    
                    for i, (disease, data) in enumerate(sorted_diseases):
                        score = data['score']
                        symptoms_matched = data['symptoms_matched']
                        total_symptoms = data['total_symptoms']
                        differentiating_factors = data['differentiating_factors']

                        with st.expander(f"**({i+1}) Potential Diagnosis:** {disease} (Match Score: {score}/{total_symptoms})"):
                            st.markdown(f"**Matched Symptoms:** {', '.join(symptoms_matched)}")
                            st.markdown(f"**Differentiating Factors:** {differentiating_factors}")

                            # Check for and display the treatment plan for the disease.
                            if disease in TREATMENTS:
                                treatment_data = TREATMENTS[disease]
                                st.markdown("---")
                                st.markdown("#### Treatment Plan")
                                st.markdown(f"**Goals:** {', '.join(treatment_data['goals'])}")
                                st.markdown(f"**First-Line Therapy:** {', '.join(treatment_data['first_line'])}")
                                st.markdown(f"**Second-Line Therapy:** {', '.join(treatment_data['second_line'])}")
                                st.markdown(f"**Supportive Care:** {', '.join(treatment_data['supportive_care'])}")
                            else:
                                st.info("Treatment information not available for this disease.")

    # A sidebar option to list all available symptoms
    st.sidebar.markdown("---")
    if st.sidebar.button("Show All Available Symptoms"):
        symptoms = sorted(DATA["symptoms"])
        st.sidebar.subheader("Available Symptoms")
        st.sidebar.markdown(", ".join(symptoms))

if __name__ == "__main__":
    main()
