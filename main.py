# app.py

import streamlit as st
import pandas as pd
from collections import defaultdict
from symptoms import ALL_SYMPTOMS # Import the symptom list from symptoms.py

# ==============================================================================
# Disclaimer and App Title
# ==============================================================================
st.set_page_config(page_title="Differential Diagnosis Simulator")
st.title("Differential Diagnosis Simulator")
st.markdown("### For Educational Use Only")
st.warning("This tool is a demonstration for educational purposes and should not be used for actual medical diagnosis. Always consult with a qualified healthcare professional.")
st.markdown("""
Welcome! This application simulates the process of differential diagnosis.
Select multiple symptoms from the list below, and the app will provide a ranked list of potential conditions based on symptom matches.
""")

# ==============================================================================
# Symptom and Disease Database
# This is a manually created, simplified database for demonstration.
# In a real application, this data would be much more complex and comprehensive.
# ==============================================================================

# A dictionary mapping diseases to their associated symptoms and reasoning.
DISEASE_DATA = {
    "Influenza (Flu)": {
        "symptoms": ["fever", "cough", "fatigue", "muscle aches", "sore throat", "runny nose", "chills", "headache"],
        "reasoning": "Influenza is a viral infection with common symptoms including high fever, chills, body aches, and respiratory issues like a cough and sore throat."
    },
    "Common Cold": {
        "symptoms": ["runny nose", "sore throat", "cough", "sneezing", "fatigue", "headache"],
        "reasoning": "The common cold is typically milder than the flu, characterized by a runny or stuffy nose and a scratchy throat. Fever is less common."
    },
    "COVID-19": {
        "symptoms": ["fever", "cough", "fatigue", "shortness of breath", "loss of taste", "loss of smell", "muscle aches", "sore throat", "chest pain", "difficulty breathing"],
        "reasoning": "COVID-19 presents with a wide range of symptoms, with key indicators often including a new cough, shortness of breath, and loss of taste or smell."
    },
    "Migraine": {
        "symptoms": ["headache", "nausea", "vomiting", "photophobia", "sensitivity to sound", "blurred vision"],
        "reasoning": "Migraine headaches are often severe and throbbing, accompanied by neurological symptoms like sensitivity to light and sound, and sometimes visual disturbances."
    },
    "Tension Headache": {
        "symptoms": ["headache", "neck stiffness", "fatigue", "dizziness"],
        "reasoning": "Tension headaches are the most common type, causing mild to moderate pain that feels like a tight band around the head, often linked to stress and muscle tension."
    },
    "Gastroenteritis (Stomach Flu)": {
        "symptoms": ["nausea", "vomiting", "diarrhea", "abdominal pain", "fever", "fatigue", "abdominal cramps"],
        "reasoning": "Gastroenteritis is an inflammation of the stomach and intestines, commonly caused by a virus, leading to severe nausea, vomiting, and diarrhea."
    },
    "Strep Throat": {
        "symptoms": ["sore throat", "fever", "difficulty swallowing", "swollen lymph nodes", "headache", "painful swallowing"],
        "reasoning": "Strep throat is a bacterial infection of the throat and tonsils, causing a sudden, severe sore throat, fever, and pain when swallowing."
    },
    "Allergies": {
        "symptoms": ["runny nose", "sneezing", "itching", "hives", "wheezing", "fatigue", "nasal congestion"],
        "reasoning": "Allergies are an immune response to a harmless substance, causing symptoms like a runny nose, sneezing, itching, and sometimes a rash or hives."
    },
    "Kidney Stones": {
        "symptoms": ["flank pain", "back pain", "abdominal pain", "blood in urine", "nausea", "vomiting", "frequent urination"],
        "reasoning": "Kidney stones can cause severe pain in the back and side, which may radiate to the lower abdomen, often accompanied by blood in the urine and nausea."
    },
    "Urinary Tract Infection (UTI)": {
        "symptoms": ["frequent urination", "painful urination", "blood in urine", "abdominal pain", "fever", "urinary incontinence"],
        "reasoning": "A UTI is an infection in the urinary system. Common symptoms include a persistent urge to urinate, a burning sensation during urination, and cloudy or bloody urine."
    },
    "Pneumonia": {
        "symptoms": ["cough", "fever", "shortness of breath", "chest pain", "chills", "fatigue", "sputum production"],
        "reasoning": "Pneumonia is an infection that inflames the air sacs in one or both lungs. Symptoms often include a cough with phlegm, fever, and difficulty breathing."
    },
    "Appendicitis": {
        "symptoms": ["abdominal pain", "nausea", "vomiting", "fever", "loss of appetite"],
        "reasoning": "Appendicitis typically starts with dull pain near the navel that moves to the lower right abdomen, often with a loss of appetite, nausea, and vomiting."
    },
    "Hypertension (High Blood Pressure)": {
        "symptoms": ["headache", "dizziness", "blurred vision", "chest pain", "shortness of breath", "flushing"],
        "reasoning": "While often asymptomatic, severe hypertension can lead to headaches, dizziness, chest pain, and blurred vision, indicating a need for urgent medical attention."
    },
    "Anxiety Disorder": {
        "symptoms": ["anxiety", "heart palpitations", "difficulty sleeping", "dizziness", "shortness of breath", "chest pain", "numbness", "tingling", "panic attacks"],
        "reasoning": "Anxiety can manifest physically with symptoms like rapid heart rate, chest pain, shortness of breath, and a feeling of panic or dread."
    },
    "Meningitis": {
        "symptoms": ["headache", "fever", "neck stiffness", "confusion", "nausea", "vomiting", "photophobia"],
        "reasoning": "Meningitis is an inflammation of the membranes surrounding the brain and spinal cord, with hallmark symptoms being fever, headache, and a stiff neck."
    },
    "Dehydration": {
        "symptoms": ["fatigue", "dizziness", "excessive thirst", "dry skin", "constipation", "dark urine"],
        "reasoning": "Dehydration occurs when the body loses more fluids than it takes in. Symptoms include thirst, fatigue, dizziness, and dark-colored urine."
    },
    "Anemia": {
        "symptoms": ["fatigue", "pale skin", "shortness of breath", "dizziness", "weakness", "heart palpitations"],
        "reasoning": "Anemia is a condition where the body lacks enough healthy red blood cells. Common symptoms include extreme fatigue, weakness, and pale skin."
    },
    "Hypothyroidism": {
        "symptoms": ["fatigue", "weight gain", "constipation", "dry skin", "depression", "cold sensitivity"],
        "reasoning": "Hypothyroidism is an underactive thyroid gland, which slows down the body's metabolism. This can cause fatigue, weight gain, constipation, and dry skin."
    },
    "Mononucleosis": {
        "symptoms": ["sore throat", "fatigue", "fever", "swollen lymph nodes", "headache", "muscle aches"],
        "reasoning": "Mono, caused by the Epstein-Barr virus, often presents with a combination of extreme fatigue, a severe sore throat, and swollen lymph nodes."
    },
    "Lupus": {
        "symptoms": ["fatigue", "joint pain", "rash", "fever", "chest pain", "swelling", "malaise"],
        "reasoning": "Lupus is a chronic autoimmune disease that can affect many parts of the body. Symptoms often include fatigue, joint pain, and a characteristic butterfly-shaped facial rash."
    },
    "Fibromyalgia": {
        "symptoms": ["fatigue", "muscle aches", "joint pain", "difficulty sleeping", "headache", "numbness", "tingling"],
        "reasoning": "Fibromyalgia is a disorder characterized by widespread musculoskeletal pain. It is often accompanied by fatigue, sleep, memory, and mood issues."
    },
    "Panic Attack": {
        "symptoms": ["heart palpitations", "shortness of breath", "chest pain", "dizziness", "nausea", "numbness", "tingling", "anxiety", "chest pressure"],
        "reasoning": "A panic attack is a sudden episode of intense fear that triggers severe physical reactions. Symptoms can mimic a heart attack, including chest pain and shortness of breath."
    },
    "Cirrhosis": {
        "symptoms": ["jaundice", "fatigue", "nausea", "vomiting", "easy bruising", "swelling", "abdominal pain"],
        "reasoning": "Cirrhosis is late-stage scarring of the liver. Symptoms often include jaundice (yellowing of the skin), fatigue, and swelling in the legs and abdomen."
    },
    "Gastroesophageal Reflux Disease (GERD)": {
        "symptoms": ["heartburn", "chest pain", "difficulty swallowing", "hoarse voice", "sore throat"],
        "reasoning": "GERD is a chronic digestive disease in which stomach acid flows back into the esophagus, causing symptoms like heartburn, chest pain, and a sour taste."
    },
    "Asthma": {
        "symptoms": ["wheezing", "cough", "shortness of breath", "chest tightness", "difficulty breathing"],
        "reasoning": "Asthma is a condition in which your airways narrow and swell. Common symptoms include wheezing, coughing, and shortness of breath, often triggered by exercise or allergens."
    }
}


# ==============================================================================
# User Input
# ==============================================================================
selected_symptoms = st.multiselect(
    "Select your symptoms from the list:",
    options=ALL_SYMPTOMS,
    help="You can select multiple symptoms. Start typing to filter the list."
)

# ==============================================================================
# Diagnosis Logic
# ==============================================================================
if st.button("Get Differential Diagnosis"):
    if not selected_symptoms:
        st.warning("Please select at least one symptom to get a diagnosis.")
    else:
        diagnosis_scores = {}
        for disease, data in DISEASE_DATA.items():
            symptom_matches = sum(1 for sym in selected_symptoms if sym in data["symptoms"])
            # Calculate a score based on the number of matching symptoms
            if symptom_matches > 0:
                # Normalizing the score to account for different disease symptom counts
                score = symptom_matches / len(data["symptoms"])
                diagnosis_scores[disease] = score

        # Sort the diagnoses by score in descending order
        sorted_diagnoses = sorted(diagnosis_scores.items(), key=lambda item: item[1], reverse=True)

        st.subheader("Differential Diagnosis:")
        if not sorted_diagnoses:
            st.info("No matching diagnoses found for the selected symptoms.")
        else:
            for i, (disease, score) in enumerate(sorted_diagnoses):
                # Display results with styling
                st.markdown(f"#### **{i + 1}. {disease}**")
                # Format score as a percentage for better readability
                st.write(f"Likelihood Score: **{score:.2%}**")
                st.write(f"**Reasoning:** {DISEASE_DATA[disease]['reasoning']}")
                st.markdown("---")

# ==============================================================================
# How to run and deploy instructions
# ==============================================================================
st.sidebar.markdown("### How to Use")
st.sidebar.markdown(
    """
    1.  **Save the files:** Save the code above into a file named `app.py` and the other code block into `symptoms.py`.
    2.  **Install Streamlit:** Run `pip install streamlit` in your terminal.
    3.  **Run the app:** Navigate to the folder where you saved your files and run `streamlit run app.py`.
    """
)
st.sidebar.markdown("### How to Deploy on Streamlit Cloud")
st.sidebar.markdown(
    """
    1.  **Create a GitHub Repo:** Put your `app.py`, `symptoms.py`, and a `requirements.txt` file into a new GitHub repository.
    2.  **Create `requirements.txt`:** This file should contain `streamlit`.
    3.  **Link to Streamlit Cloud:** Go to [share.streamlit.io](https://share.streamlit.io/), link your GitHub account, and select your repository to deploy the app.
    """
)
