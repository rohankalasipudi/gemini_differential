import streamlit as st
from symptoms import analyze_symptoms, DATA
from treatments import TREATMENTS

def main():
    """
    This is the main function for the Streamlit application.
    It creates the UI and handles the symptom analysis and treatment display.
    """
    st.set_page_config(
        page_title="Differential Diagnosis & Treatment Companion",
        page_icon="⚕️",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    st.title("⚕️ Differential Diagnosis & Treatment Companion")
    st.markdown("""
        _This tool provides a differential diagnosis and a treatment overview based on the symptoms you provide. It is for educational purposes only and is not a substitute for professional medical advice._
    """)

    st.sidebar.header("How to Use")
    st.sidebar.markdown("""
        1. Enter your symptoms in the text box below, separated by commas.
        2. Click the 'Analyze Symptoms' button.
        3. The app will display potential diseases and their treatment protocols.
        4. Use the expanders to view detailed treatment information.
    """)

    # User input for symptoms
    user_input = st.text_area(
        "Please enter your symptoms, separated by commas (e.g., fever, cough, joint pain, fatigue).",
        height=100,
        placeholder="e.g., fever, cough, joint pain, fatigue"
    )

    # A button to trigger the analysis
    if st.button("Analyze Symptoms"):
        if not user_input:
            st.warning("Please enter at least one symptom to run the analysis.")
        else:
            # Process user symptoms and get the differential diagnosis.
            user_symptoms = [s.strip().lower() for s in user_input.split(',')]
            disease_scores = analyze_symptoms(user_symptoms)

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

                    with st.expander(f"**({i+1}) Potential Disease:** {disease} (Match Score: {score}/{total_symptoms})"):
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
