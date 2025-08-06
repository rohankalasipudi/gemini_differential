# symptoms.py

# This file contains the medical data and the core diagnostic function.
# It is designed to be imported by the main application file (main.py).

# Consolidate data into a single object for easier management.
DATA = {
    # This is a comprehensive list of common medical symptoms,
    # now using the list you provided.
    "symptoms": sorted([
        # General Constitutional Symptoms
        "fever", "chills", "fatigue", "malaise", "weight loss", "weight gain",
        "night sweats", "excessive thirst", "excessive hunger", "loss of appetite",
        "dizziness", "lightheadedness", "vertigo", "weakness", "muscle aches", "joint pain",
        "swelling", "easy bruising", "pale skin", "jaundice",

        # Respiratory Symptoms
        "cough", "shortness of breath", "chest pain", "sore throat", "runny nose",
        "nasal congestion", "sneezing", "hoarse voice", "wheezing", "sputum production",
        "difficulty swallowing", "earache", "sinus pressure",

        # Cardiovascular Symptoms
        "heart palpitations", "chest tightness", "chest pressure", "ankle swelling",
        "leg swelling", "fainting", "syncope", "orthostatic hypotension",

        # Gastrointestinal Symptoms
        "abdominal pain", "nausea", "vomiting", "diarrhea", "constipation",
        "bloating", "indigestion", "heartburn", "difficulty swallowing", "abdominal cramps",
        "blood in stool", "dark stool", "painful swallowing",

        # Neurological Symptoms
        "headache", "blurred vision", "double vision", "photophobia", "sensitivity to sound",
        "numbness", "tingling", "confusion", "memory loss", "seizures",
        "neck stiffness", "tremors", "loss of coordination", "balance problems",
        "loss of taste", "loss of smell", "slurred speech", "vertigo",

        # Urinary and Reproductive Symptoms
        "frequent urination", "painful urination", "blood in urine", "dark urine",
        "urinary incontinence", "flank pain", "back pain", "pelvic pain",
        "abnormal vaginal bleeding", "pain during intercourse",

        # Dermatological Symptoms
        "rash", "itching", "hives", "dry skin", "skin lesions", "hair loss",

        # Musculoskeletal Symptoms
        "back pain", "neck pain", "joint stiffness", "muscle weakness", "cramps",

        # Mental Health Symptoms
        "anxiety", "depression", "mood swings", "difficulty sleeping", "insomnia",
        "irritability", "lack of interest", "suicidal ideation", "panic attacks",

        # Other Symptoms
        "tinnitus", "hearing loss", "swollen lymph nodes", "oral sores",
        "bleeding gums", "persistent cough"
    ]),

    "diseases": {
        "Influenza (Flu)": {
            "symptoms": ["fever", "chills", "muscle aches", "fatigue", "cough", "sore throat", "headache", "runny nose"],
            "differentiating_factors": "Sudden onset with prominent systemic symptoms like high fever and myalgias. Tends to be more severe than the common cold.",
        },
        "COVID-19": {
            "symptoms": ["fever", "cough", "shortness of breath", "fatigue", "loss of taste", "loss of smell", "muscle aches", "headache"],
            "differentiating_factors": "Loss of taste and smell is highly specific. Can lead to severe respiratory distress and long-term 'long COVID' symptoms.",
        },
        "Bacterial Meningitis": {
            "symptoms": ["fever", "headache", "neck stiffness", "confusion", "nausea", "vomiting", "photophobia"],
            "differentiating_factors": "Classic triad of fever, stiff neck (nuchal rigidity), and altered mental status. Kernig's and Brudzinski's signs are specific on physical exam.",
        },
        "Anxiety/Panic Attack": {
            "symptoms": ["heart palpitations", "shortness of breath", "chest pain", "tremors", "sweating", "anxiety", "lightheadedness"],
            "differentiating_factors": "Symptoms peak within minutes and often resolve within 20-30 minutes. Chest pain is sharp and localized, unlike the crushing pressure of an MI.",
        },
        "Cirrhosis": {
            "symptoms": ["fatigue", "weakness", "nausea", "loss of appetite", "weight loss", "itching", "jaundice", "easy bruising", "swelling", "leg swelling"],
            "differentiating_factors": "A combination of liver failure signs (jaundice, coagulopathy) and portal hypertension signs (ascites, pedal edema). Labs show elevated LFTs and low albumin.",
        },
        "Pneumonia": {
            "symptoms": ["fever", "chills", "sputum production", "shortness of breath", "chest pain", "wheezing"],
            "differentiating_factors": "Characterized by a cough with colored sputum and pleuritic chest pain. Chest X-ray showing a lobar infiltrate is diagnostic.",
        },
        "Myocardial Infarction (MI)": {
            "symptoms": ["chest pain", "chest pressure", "radiating arm pain", "nausea", "sweating", "cold sweat", "lightheadedness", "shortness of breath"],
            "differentiating_factors": "Crushing, substernal chest pain that may radiate. Often associated with diaphoresis and impending doom. EKG changes and elevated troponins are definitive.",
        },
        "Congestive Heart Failure (CHF)": {
            "symptoms": ["shortness of breath", "fatigue", "ankle swelling", "leg swelling", "cough", "weight gain"],
            "differentiating_factors": "Symptoms worsen with exertion (dyspnea on exertion) and at night (orthopnea). Physical exam shows rales, an S3 heart sound, and jugular venous distention.",
        },
        "Pulmonary Embolism (PE)": {
            "symptoms": ["shortness of breath", "chest pain", "heart palpitations", "cough", "dizziness"],
            "differentiating_factors": "Sudden onset of dyspnea and pleuritic chest pain, often with no fever. Key risk factors include recent surgery, long-haul travel, and malignancy.",
        },
        "Appendicitis": {
            "symptoms": ["abdominal pain", "nausea", "vomiting", "fever", "loss of appetite"],
            "differentiating_factors": "Pain begins periumbilically and migrates to the right lower quadrant. Rebound tenderness and guarding on exam at McBurney's point are classic.",
        },
        "Cholecystitis": {
            "symptoms": ["abdominal pain", "nausea", "vomiting", "fever"],
            "differentiating_factors": "Pain is in the right upper quadrant and may radiate to the right shoulder. Often triggered by a fatty meal. A positive Murphy's sign is highly suggestive.",
        },
        "Pancreatitis": {
            "symptoms": ["abdominal pain", "nausea", "vomiting", "fever"],
            "differentiating_factors": "Abdominal pain is severe, constant, and radiates to the back. A history of heavy alcohol use or gallstones is common. Labs show elevated lipase and amylase.",
        },
        "Chronic Kidney Disease (CKD)": {
            "symptoms": ["fatigue", "weakness", "nausea", "vomiting", "loss of appetite", "leg swelling", "itching"],
            "differentiating_factors": "Insidious onset with long-term symptoms. Labs show elevated BUN/creatinine. Pruritus and 'uremic frost' are late-stage findings.",
        },
        "Hypothyroidism": {
            "symptoms": ["fatigue", "weight gain", "cold intolerance", "constipation", "dry skin", "hair loss", "depression"],
            "differentiating_factors": "Symptoms of a slowed metabolism. Labs show high TSH and low T4. Often gradual onset. Common in middle-aged women.",
        },
        "Hyperthyroidism (Graves' Disease)": {
            "symptoms": ["weight loss", "excessive hunger", "heat intolerance", "heart palpitations", "tremors", "anxiety"],
            "differentiating_factors": "Symptoms of a hypermetabolic state. Labs show low TSH and high T4/T3. Exophthalmos is a pathognomonic finding for Graves' disease.",
        },
        "Parkinson's Disease": {
            "symptoms": ["tremors", "neck stiffness", "slurred speech", "loss of coordination", "balance problems"],
            "differentiating_factors": "Classic triad of resting tremor, rigidity, and bradykinesia. The tremor is a 'pill-rolling' tremor that improves with voluntary movement.",
        },
        "Multiple Sclerosis (MS)": {
            "symptoms": ["numbness", "tingling", "weakness", "blurred vision", "double vision", "balance problems", "fatigue", "urinary incontinence"],
            "differentiating_factors": "Neurological deficits that are 'disseminated in space and time.' Symptoms often wax and wane (relapsing-remitting). MRI shows characteristic plaques.",
        },
        "Lupus (Systemic Lupus Erythematosus)": {
            "symptoms": ["fatigue", "joint pain", "joint stiffness", "malar rash", "fever", "weight loss", "photosensitivity", "oral ulcers"],
            "differentiating_factors": "A multi-system autoimmune disease. The classic 'butterfly' malar rash and photosensitivity are highly suggestive. Positive ANA is a key diagnostic marker.",
        },
        "Rheumatoid Arthritis (RA)": {
            "symptoms": ["joint pain", "joint stiffness", "swelling", "joint swelling", "fatigue", "morning stiffness"],
            "differentiating_factors": "Symmetrical joint involvement, especially in the small joints of the hands and feet. Morning stiffness lasting more than 30 minutes is a key feature.",
        },
        "Osteoarthritis (OA)": {
            "symptoms": ["joint pain", "joint stiffness", "bony enlargement"],
            "differentiating_factors": "Asymmetrical joint involvement, primarily in weight-bearing joints. Morning stiffness is brief (<30 minutes). Pain worsens with activity and improves with rest.",
        },
        "Sepsis": {
            "symptoms": ["fever", "chills", "heart palpitations", "confusion", "orthostatic hypotension"],
            "differentiating_factors": "Systemic inflammatory response to an infection. Look for signs of organ dysfunction (e.g., altered mental status, hypotension, oliguria).",
        },
        "Depression": {
            "symptoms": ["fatigue", "loss of appetite", "insomnia", "mood swings", "confusion", "social withdrawal", "suicidal ideation"],
            "differentiating_factors": "Requires a constellation of symptoms for at least two weeks, including a depressed mood or anhedonia. Symptoms are persistent and interfere with daily function.",
        },
        "Migraine": {
            "symptoms": ["headache", "nausea", "vomiting", "photophobia", "sensitivity to sound"],
            "differentiating_factors": "Unilateral, pulsating headache that is severe. Often associated with an aura and sensitivity to light and sound. Can be debilitating.",
        },
        "Stroke": {
            "symptoms": ["facial drooping", "weakness", "slurred speech", "blurred vision", "balance problems"],
            "differentiating_factors": "Sudden onset of focal neurological deficits. Use the FAST mnemonic: F-Facial drooping, A-Arm weakness, S-Speech difficulty, T-Time to call emergency services.",
        },
        "Type 1 Diabetes": {
            "symptoms": ["excessive thirst", "frequent urination", "weight loss", "excessive hunger", "fatigue"],
            "differentiating_factors": "Classic triad of polyuria, polydipsia, and polyphagia. Often sudden onset in children and young adults, due to autoimmune destruction of pancreatic beta cells.",
        },
        "Cushing's Syndrome": {
            "symptoms": ["weight gain", "central obesity", "moon facies", "buffalo hump", "striae", "easy bruising", "hypertension", "weakness"],
            "differentiating_factors": "Caused by chronic exposure to high levels of cortisol. Classic physical findings like central obesity with thin extremities, moon facies, and purple striae are key.",
        },
        "Chronic Obstructive Pulmonary Disease (COPD)": {
            "symptoms": ["cough", "shortness of breath", "wheezing", "weakness", "fatigue"],
            "differentiating_factors": "A progressive disease, typically in smokers. Characterized by a chronic, productive cough and progressive dyspnea. Spirometry is used for diagnosis.",
        },
        "Asthma": {
            "symptoms": ["shortness of breath", "wheezing", "cough", "chest tightness"],
            "differentiating_factors": "Characterized by reversible airway obstruction. Symptoms are often triggered by allergens or exercise and improve with bronchodilators. Classic wheezing on expiration is heard on exam.",
        },
        "Gastroesophageal Reflux Disease (GERD)": {
            "symptoms": ["heartburn", "acid reflux", "chest pain", "difficulty swallowing", "cough"],
            "differentiating_factors": "Burning retrosternal chest pain (heartburn) that worsens after meals, when lying down, or with bending over. The pain is not exertional and is not associated with signs of MI.",
        },
        "Irritable Bowel Syndrome (IBS)": {
            "symptoms": ["abdominal pain", "bloating", "diarrhea", "constipation"],
            "differentiating_factors": "Chronic abdominal pain associated with changes in bowel habits. Diagnosis is based on clinical criteria and exclusion of other pathologies.",
        },
        "Ulcerative Colitis (UC)": {
            "symptoms": ["abdominal pain", "diarrhea", "blood in stool", "fatigue", "weight loss"],
            "differentiating_factors": "A type of Inflammatory Bowel Disease characterized by continuous inflammation starting in the rectum. Presents with bloody diarrhea and tenesmus.",
        },
        "Crohn's Disease": {
            "symptoms": ["abdominal pain", "diarrhea", "fatigue", "weight loss", "oral sores"],
            "differentiating_factors": "A type of Inflammatory Bowel Disease characterized by patchy, transmural inflammation anywhere from mouth to anus. Fistulas and strictures are common.",
        },
        "Schizophrenia": {
            "symptoms": ["hallucinations", "delusions", "paranoia", "psychosis", "disorganized speech", "social withdrawal"],
            "differentiating_factors": "Presence of positive symptoms (hallucinations, delusions) and negative symptoms (flat affect, social withdrawal). Requires a continuous duration of at least 6 months.",
        },
        "Bipolar Disorder": {
            "symptoms": ["mood swings", "depression", "insomnia", "irritability", "psychosis", "increased energy"],
            "differentiating_factors": "Characterized by episodes of mania/hypomania and major depression. Mood swings are distinct, not just daily irritability.",
        },
        "Eczema (Atopic Dermatitis)": {
            "symptoms": ["itching", "rash", "dry skin", "skin lesions"],
            "differentiating_factors": "A chronic, inflammatory skin condition. Presents with an extremely itchy rash on flexural surfaces (e.g., inner elbows, knees). Often has a history of atopy (asthma, allergic rhinitis).",
        },
        "Psoriasis": {
            "symptoms": ["rash", "itching", "skin lesions", "joint pain"],
            "differentiating_factors": "Presents with well-demarcated, erythematous plaques with silvery scales, typically on extensor surfaces (e.g., elbows, knees). Can be associated with psoriatic arthritis.",
        }
    }
}

def analyze_symptoms(user_symptoms):
    """
    Finds potential diseases based on a list of user-provided symptoms.
    
    Args:
        user_symptoms (list): A list of symptoms the user is experiencing.
        
    Returns:
        dict: A dictionary mapping each potential disease to a match score and
              differentiating factors.
    """
    disease_scores = {}
    
    disease_data = DATA["diseases"]
    
    for disease, data in disease_data.items():
        score = 0
        matching_symptoms = []
        # Case-insensitive symptom matching
        disease_symptoms_lower = [s.lower().strip() for s in data["symptoms"]]
        for symptom in user_symptoms:
            if symptom.lower().strip() in disease_symptoms_lower:
                score += 1
                matching_symptoms.append(symptom)
        if score > 0:
            disease_scores[disease] = {
                "score": score,
                "symptoms_matched": matching_symptoms,
                "total_symptoms": len(data["symptoms"]),
                "differentiating_factors": data["differentiating_factors"]
            }
    
    return disease_scores
