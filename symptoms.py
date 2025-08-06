# symptoms.py

# This file contains the medical data and the core diagnostic function.
# It is designed to be imported by the main application file (main.py).
# It has been significantly expanded with a wider range of symptoms and diseases.

# Consolidate data into a single object for easier management.
DATA = {
    "symptoms": sorted([
        # General Constitutional Symptoms
        "fever", "chills", "fatigue", "malaise", "weight loss", "weight gain",
        "night sweats", "excessive thirst", "excessive hunger", "loss of appetite",
        "dizziness", "lightheadedness", "vertigo", "weakness", "muscle aches", "joint pain",
        "swelling", "easy bruising", "pale skin", "jaundice", "malaise", "anorexia",
        "cachexia", "polydipsia", "polyphagia", "asthenia", "petechiae", "purpura", "lymphadenopathy",
        "unexplained weight loss", "unexplained weight gain", "paresthesia", "dysesthesia",
        
        # Respiratory Symptoms
        "cough", "shortness of breath", "chest pain", "sore throat", "runny nose",
        "nasal congestion", "sneezing", "hoarse voice", "wheezing", "sputum production",
        "difficulty swallowing", "earache", "sinus pressure", "hemoptysis", "dyspnea",
        "orthopnea", "paroxysmal nocturnal dyspnea", "stridor", "tachypnea", "pleurisy",
        "apnea", "epistaxis", "vocal hoarseness", "rales", "rhonchi", "pleural effusion",
        
        # Cardiovascular Symptoms
        "heart palpitations", "chest tightness", "chest pressure", "ankle swelling",
        "leg swelling", "fainting", "syncope", "orthostatic hypotension", "muffled heart sounds",
        "peripheral edema", "angina", "claudication", "dependent edema", "exertional dyspnea",
        "jugular venous distention", "S3 heart sound", "S4 heart sound", "murmur",
        "intermittent claudication", "rest pain", "cyanosis", "arrhythmia", "bradycardia",
        "tachycardia", "hypertension", "hypotension", "bounding pulse", "diminished pulse",
        "thrill", "bruit", "cardiac rub",
        
        # Gastrointestinal Symptoms
        "abdominal pain", "nausea", "vomiting", "diarrhea", "constipation",
        "bloating", "indigestion", "heartburn", "difficulty swallowing", "abdominal cramps",
        "blood in stool", "dark stool", "painful swallowing", "hematemesis", "melena",
        "bright red blood per rectum", "ascites", "dysphagia", "odynophagia", "tenesmus",
        "dyspepsia", "flatulence", "globus sensation", "steatorrhea", "anorectal pain",
        "rectal bleeding", "hematochezia", "borborygmi", "early satiety", "gastric outlet obstruction",
        "rebound tenderness", "guarding", "jaundice", "hepatomegaly", "splenomegaly", "inguinal hernia",
        "epigastric pain", "periumbilical pain", "right lower quadrant pain", "right upper quadrant pain",
        
        # Neurological Symptoms
        "headache", "blurred vision", "double vision", "photophobia", "sensitivity to sound",
        "numbness", "tingling", "confusion", "memory loss", "seizures",
        "neck stiffness", "tremors", "loss of coordination", "balance problems",
        "loss of taste", "loss of smell", "slurred speech", "vertigo", "ataxia", "aphasia",
        "dysarthria", "hemianopsia", "nystagmus", "ptosis", "dystonia", "tinnitus",
        "carpal tunnel syndrome", "foot drop", "drop attacks", "syncope", "loss of consciousness",
        "dementia", "amnesia", "delirium", "paresthesia", "diplopia", "unilateral weakness",
        
        # Urinary and Reproductive Symptoms
        "frequent urination", "painful urination", "blood in urine", "dark urine",
        "urinary incontinence", "flank pain", "back pain", "pelvic pain",
        "abnormal vaginal bleeding", "pain during intercourse", "hematuria", "oliguria",
        "anuria", "dysuria", "uremic pruritus", "nocturia", "urinary urgency",
        "urinary hesitancy", "urethral discharge", "renal colic", "testicular pain",
        "erectile dysfunction", "vaginal discharge", "dyspareunia", "amenorrhea",
        "dysmenorrhea", "polyuria", "oligomenorrhea", "metrorrhagia",
        
        # Dermatological Symptoms
        "rash", "itching", "hives", "dry skin", "skin lesions", "hair loss",
        "dermatitis", "psoriasis plaques", "eczema", "alopecia", "erythema", "petechiae",
        "purpura", "urticaria", "acanthosis nigricans", "striae", "pruritus",
        "cellulitis", "skin discoloration", "ulceration", "nodules", "papules", "vesicles",
        
        # Musculoskeletal Symptoms
        "back pain", "neck pain", "joint stiffness", "muscle weakness", "cramps",
        "scoliosis", "kyphosis", "lordosis", "tenderness", "swelling of joints", "joint effusion",
        "gout", "bursitis", "sciatica", "radiculopathy", "osteoarthritis", "rheumatoid arthritis",
        "fibromyalgia", "polymyalgia rheumatica",
        
        # Mental Health Symptoms
        "anxiety", "depression", "mood swings", "difficulty sleeping", "insomnia",
        "irritability", "lack of interest", "suicidal ideation", "panic attacks",
        "anhedonia", "flat affect", "psychosis", "delusions", "hallucinations", "catatonia",
        "mania", "hypomania", "obsessive thoughts", "compulsive behaviors", "social withdrawal",
        "PTSD flashbacks", "dissociation", "low self-esteem", "hopelessness", "fearfulness",
        "paranoia", "poor concentration", "agitation", "psychomotor retardation", "avolition",
        
        # Other Symptoms
        "tinnitus", "hearing loss", "swollen lymph nodes", "oral sores",
        "bleeding gums", "persistent cough", "anosmia", "dysgeusia", "diplopia",
        "exophthalmos", "lid lag", "goiter", "hoarseness", "cold intolerance",
        "heat intolerance"
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
            "symptoms": ["shortness of breath", "fatigue", "ankle swelling", "leg swelling", "cough", "weight gain", "dependent edema"],
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
            "symptoms": ["fatigue", "weakness", "nausea", "vomiting", "loss of appetite", "leg swelling", "itching", "uremic pruritus"],
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
            "symptoms": ["abdominal pain", "diarrhea", "blood in stool", "fatigue", "weight loss", "tenesmus"],
            "differentiating_factors": "A type of Inflammatory Bowel Disease characterized by continuous inflammation starting in the rectum. Presents with bloody diarrhea and tenesmus.",
        },
        "Crohn's Disease": {
            "symptoms": ["abdominal pain", "diarrhea", "fatigue", "weight loss", "oral sores"],
            "differentiating_factors": "A type of Inflammatory Bowel Disease characterized by patchy, transmural inflammation anywhere from mouth to anus. Fistulas and strictures are common.",
        },
        "Schizophrenia": {
            "symptoms": ["hallucinations", "delusions", "paranoia", "psychosis", "slurred speech", "social withdrawal"],
            "differentiating_factors": "Presence of positive symptoms (hallucinations, delusions) and negative symptoms (flat affect, social withdrawal). Requires a continuous duration of at least 6 months.",
        },
        "Bipolar Disorder": {
            "symptoms": ["mood swings", "depression", "insomnia", "irritability", "psychosis", "increased energy", "mania", "hypomania"],
            "differentiating_factors": "Characterized by episodes of mania/hypomania and major depression. Mood swings are distinct, not just daily irritability.",
        },
        "Eczema (Atopic Dermatitis)": {
            "symptoms": ["itching", "rash", "dry skin", "skin lesions"],
            "differentiating_factors": "A chronic, inflammatory skin condition. Presents with an extremely itchy rash on flexural surfaces (e.g., inner elbows, knees). Often has a history of atopy (asthma, allergic rhinitis).",
        },
        "Psoriasis": {
            "symptoms": ["rash", "itching", "skin lesions", "joint pain"],
            "differentiating_factors": "Presents with well-demarcated, erythematous plaques with silvery scales, typically on extensor surfaces (e.g., elbows, knees). Can be associated with psoriatic arthritis.",
        },
        "Peptic Ulcer Disease (PUD)": {
            "symptoms": ["abdominal pain", "indigestion", "heartburn", "melena", "hematemesis"],
            "differentiating_factors": "Epigastric pain that is gnawing or burning. Duodenal ulcers are relieved by food, while gastric ulcers are often worsened by it.",
        },
        "Atrial Fibrillation (Afib)": {
            "symptoms": ["heart palpitations", "shortness of breath", "chest pain", "lightheadedness", "fainting"],
            "differentiating_factors": "Irregularly irregular rhythm on EKG. Often presents as palpitations or symptoms of decreased cardiac output.",
        },
        "Peripheral Artery Disease (PAD)": {
            "symptoms": ["claudication", "leg pain", "muscle weakness", "cramps"],
            "differentiating_factors": "Leg pain that occurs with exercise and is relieved by rest (claudication). Diminished or absent peripheral pulses and cool extremities are key signs.",
        },
        "Acute Kidney Injury (AKI)": {
            "symptoms": ["oliguria", "anuria", "swelling", "fatigue", "nausea", "confusion"],
            "differentiating_factors": "Rapid decline in kidney function, often reversible. Labs show a rapid increase in BUN and creatinine. History often includes a predisposing factor like dehydration or medication use.",
        },
        "Nephrotic Syndrome": {
            "symptoms": ["peripheral edema", "leg swelling", "ankle swelling", "fatigue", "weight gain"],
            "differentiating_factors": "Characterized by heavy proteinuria. The edema is often pitting and can be severe. Associated with low serum albumin.",
        },
        "Major Depressive Disorder (MDD)": {
            "symptoms": ["anhedonia", "depression", "insomnia", "difficulty sleeping", "fatigue", "suicidal ideation", "weight loss", "loss of appetite"],
            "differentiating_factors": "Persistent depressed mood or loss of interest for at least two weeks, along with other symptoms. Symptoms cause clinically significant distress or impairment.",
        },
        "Acute Myocardial Pericarditis": {
            "symptoms": ["chest pain", "fever", "malaise", "muffled heart sounds"],
            "differentiating_factors": "Chest pain is sharp, pleuritic, and relieved by leaning forward. A pericardial friction rub is often heard on auscultation.",
        },
        "Acute Pancreatitis": {
            "symptoms": ["abdominal pain", "nausea", "vomiting", "back pain"],
            "differentiating_factors": "Severe, constant epigastric pain that radiates to the back. A history of gallstones or heavy alcohol use is common.",
        },
        "Acute Glomerulonephritis": {
            "symptoms": ["hematuria", "oliguria", "hypertension", "edema"],
            "differentiating_factors": "Characterized by hematuria, proteinuria, and edema. Often occurs after a strep infection.",
        },
        "Nephritic Syndrome": {
            "symptoms": ["hematuria", "hypertension", "oliguria", "facial swelling"],
            "differentiating_factors": "Presents with hematuria and hypertension due to inflammation of the glomeruli. Facial swelling is a common early sign.",
        },
        "Bipolar I Disorder": {
            "symptoms": ["mania", "hypomania", "depression", "psychosis", "insomnia"],
            "differentiating_factors": "Diagnosis requires at least one manic episode. Manic episodes are marked by a distinct period of abnormally and persistently elevated, expansive, or irritable mood.",
        },
        "Obsessive-Compulsive Disorder (OCD)": {
            "symptoms": ["obsessive thoughts", "compulsive behaviors", "anxiety"],
            "differentiating_factors": "Characterized by obsessions (recurrent, unwanted thoughts) and compulsions (repetitive behaviors) that an individual feels driven to perform to reduce anxiety.",
        },
        "Gout": {
            "symptoms": ["joint pain", "joint swelling", "joint redness", "fever"],
            "differentiating_factors": "Sudden onset of severe pain in a single joint, often the big toe. Caused by hyperuricemia and crystal deposition. 'Podagra' is the term for gout in the big toe.",
        },
        "Fibromyalgia": {
            "symptoms": ["widespread pain", "fatigue", "sleep disturbance", "cognitive dysfunction", "headache"],
            "differentiating_factors": "Characterized by chronic widespread pain and tenderness in specific 'tender points.' Often associated with fatigue, sleep, and mood issues. Diagnosis is clinical.",
        },
        "Chronic Pain Syndrome": {
            "symptoms": ["chronic pain", "fatigue", "sleep disturbance", "depression"],
            "differentiating_factors": "Pain that persists for longer than 3-6 months. Often has a significant psychological component and can be associated with depression or anxiety.",
        },
        "Diabetic Ketoacidosis (DKA)": {
            "symptoms": ["excessive thirst", "frequent urination", "nausea", "vomiting", "abdominal pain", "fruity breath"],
            "differentiating_factors": "A serious complication of diabetes, often in Type 1. Characterized by hyperglycemia, metabolic acidosis, and ketonemia. Fruity breath is a classic sign.",
        },
        "Inflammatory Bowel Disease (IBD)": {
            "symptoms": ["abdominal pain", "diarrhea", "blood in stool", "fever", "weight loss", "fatigue"],
            "differentiating_factors": "A group of conditions, primarily Crohn's disease and ulcerative colitis, characterized by chronic inflammation of the GI tract. Differentiated by location and type of inflammation.",
        },
        "Rheumatic Fever": {
            "symptoms": ["joint pain", "fever", "fatigue", "chorea", "rash", "carditis"],
            "differentiating_factors": "A delayed complication of a strep throat infection. Diagnosis is based on the Jones criteria, which include carditis, polyarthritis, chorea, erythema marginatum, and subcutaneous nodules.",
        },
        "Atrial Flutter": {
            "symptoms": ["heart palpitations", "shortness of breath", "lightheadedness", "fainting"],
            "differentiating_factors": "EKG shows a classic 'sawtooth' pattern of atrial activity. Typically a more organized rhythm than Afib, with atrial rates around 300 bpm.",
        },
        "Ventricular Tachycardia": {
            "symptoms": ["heart palpitations", "dizziness", "chest pain", "fainting", "syncope"],
            "differentiating_factors": "A potentially life-threatening arrhythmia. EKG shows a wide QRS complex. Often a sign of underlying structural heart disease.",
        },
        "Gastritis": {
            "symptoms": ["abdominal pain", "nausea", "indigestion", "bloating"],
            "differentiating_factors": "Inflammation of the stomach lining. Epigastric pain is common and often associated with a history of NSAID or alcohol use.",
        },
        "Gastroenteritis": {
            "symptoms": ["abdominal pain", "diarrhea", "nausea", "vomiting", "fever"],
            "differentiating_factors": "Often referred to as 'stomach flu.' An acute illness with a sudden onset of nausea, vomiting, and/or diarrhea. Usually self-limiting.",
        },
        "Endocarditis": {
            "symptoms": ["fever", "fatigue", "malaise", "murmur", "splenomegaly", "petechiae"],
            "differentiating_factors": "Infection of the heart valves. Fever and a new or changed heart murmur are key signs. Risk factors include IV drug use and pre-existing heart valve issues.",
        },
        "Pyelonephritis": {
            "symptoms": ["flank pain", "fever", "chills", "nausea", "vomiting", "dysuria"],
            "differentiating_factors": "A kidney infection. Patients are often acutely ill with high fever and CVA (costovertebral angle) tenderness.",
        },
        "Nephrolithiasis (Kidney Stones)": {
            "symptoms": ["flank pain", "back pain", "hematuria", "nausea", "vomiting"],
            "differentiating_factors": "Pain is colicky and severe, often radiating from the flank to the groin. The pain comes in waves and is not relieved by position changes.",
        },
        "Bipolar II Disorder": {
            "symptoms": ["hypomania", "depression", "insomnia", "fatigue", "mood swings"],
            "differentiating_factors": "Characterized by at least one major depressive episode and at least one hypomanic episode. Unlike Bipolar I, there is no history of a full manic episode.",
        },
        "Generalized Anxiety Disorder (GAD)": {
            "symptoms": ["anxiety", "worry", "restlessness", "fatigue", "difficulty sleeping", "muscle tension"],
            "differentiating_factors": "Excessive and uncontrollable worry about a variety of things for at least 6 months. Worry is out of proportion to the actual likelihood of a negative event.",
        },
        "Post-Traumatic Stress Disorder (PTSD)": {
            "symptoms": ["PTSD flashbacks", "anxiety", "difficulty sleeping", "avoidance", "irritability"],
            "differentiating_factors": "Symptoms arise after exposure to a traumatic event. The core features are re-experiencing the event, avoidance, negative changes in cognition/mood, and hyperarousal.",
        },
        "Schizoaffective Disorder": {
            "symptoms": ["psychosis", "hallucinations", "delusions", "depression", "mania"],
            "differentiating_factors": "A combination of symptoms of schizophrenia (psychosis) and a mood disorder (mania or depression). Psychosis must be present for at least two weeks without prominent mood symptoms.",
        },
        "Acute Stress Disorder (ASD)": {
            "symptoms": ["anxiety", "dissociation", "nightmares", "flashbacks"],
            "differentiating_factors": "Symptoms are similar to PTSD but occur within one month of a traumatic event. If symptoms persist beyond one month, the diagnosis changes to PTSD.",
        },
        "Borderline Personality Disorder (BPD)": {
            "symptoms": ["mood swings", "impulsivity", "fear of abandonment", "unstable relationships"],
            "differentiating_factors": "A pervasive pattern of instability in interpersonal relationships, self-image, and affects. Often associated with self-harm and intense, inappropriate anger.",
        },
        "Bulimia Nervosa": {
            "symptoms": ["binge eating", "purging", "body image concerns", "weight gain", "tooth enamel erosion"],
            "differentiating_factors": "Recurrent episodes of binge eating followed by compensatory behaviors like self-induced vomiting or excessive exercise. Patients are often a normal weight or overweight.",
        },
        "Anorexia Nervosa": {
            "symptoms": ["weight loss", "fear of gaining weight", "distorted body image", "amenorrhea", "bradycardia"],
            "differentiating_factors": "Intense fear of gaining weight and a distorted perception of body shape. Characterized by a significantly low body weight. Often associated with amenorrhea in females.",
        },
        "Celiac Disease": {
            "symptoms": ["diarrhea", "abdominal pain", "bloating", "weight loss", "fatigue"],
            "differentiating_factors": "An autoimmune reaction to gluten. Symptoms improve dramatically on a gluten-free diet. Can lead to malabsorption.",
        },
        "Cystic Fibrosis": {
            "symptoms": ["persistent cough", "sputum production", "fatigue", "weight loss", "steatorrhea"],
            "differentiating_factors": "A genetic disorder affecting the lungs and digestive system. Characterized by thick, sticky mucus production. Sweat chloride test is the diagnostic gold standard.",
        },
        "Pneumothorax": {
            "symptoms": ["sudden chest pain", "shortness of breath", "tachypnea"],
            "differentiating_factors": "Sudden onset of dyspnea and sharp, pleuritic chest pain. Diagnosis is confirmed by a chest X-ray showing a collapsed lung. Can be spontaneous or traumatic.",
        },
        "Pericardial Tamponade": {
            "symptoms": ["shortness of breath", "chest pain", "hypotension", "muffled heart sounds"],
            "differentiating_factors": "A life-threatening condition where fluid accumulates in the pericardial sac, compressing the heart. Beck's triad of hypotension, JVD, and muffled heart sounds is classic.",
        },
        "Mitral Stenosis": {
            "symptoms": ["dyspnea", "fatigue", "heart palpitations", "hemoptysis"],
            "differentiating_factors": "Narrowing of the mitral valve. Often a late complication of rheumatic fever. Leads to a classic 'opening snap' and a diastolic rumble on auscultation.",
        },
        "Aortic Stenosis": {
            "symptoms": ["syncope", "angina", "dyspnea", "heart murmur"],
            "differentiating_factors": "Narrowing of the aortic valve. Classic triad of syncope, angina, and dyspnea. Associated with a crescendo-decrescendo systolic murmur.",
        },
        "Tricuspid Regurgitation": {
            "symptoms": ["peripheral edema", "ascites", "jugular venous distention"],
            "differentiating_factors": "Incomplete closure of the tricuspid valve. Leads to right-sided heart failure symptoms. Often secondary to pulmonary hypertension or left-sided heart failure.",
        },
        "Pyelonephritis": {
            "symptoms": ["fever", "flank pain", "nausea", "vomiting", "dysuria"],
            "differentiating_factors": "A kidney infection. Symptoms include high fever, CVA tenderness, and dysuria. Often a progression from an untreated UTI.",
        },
        "Urinary Tract Infection (UTI)": {
            "symptoms": ["dysuria", "frequent urination", "urinary urgency", "pelvic pain"],
            "differentiating_factors": "Infection of the bladder or urethra. Symptoms are localized to the urinary tract. Often treated with a short course of antibiotics.",
        },
        "Benign Prostatic Hyperplasia (BPH)": {
            "symptoms": ["urinary hesitancy", "frequent urination", "nocturia", "weak stream"],
            "differentiating_factors": "Enlargement of the prostate gland in older men. Causes obstructive urinary symptoms.",
        },
        "Depersonalization/Derealization Disorder": {
            "symptoms": ["depersonalization", "derealization", "anxiety", "feeling detached"],
            "differentiating_factors": "Persistent or recurrent feelings of being detached from one's own body (depersonalization) or from one's surroundings (derealization).",
        },
        "Somatization Disorder": {
            "symptoms": ["multiple physical symptoms", "fatigue", "pain", "gastrointestinal symptoms"],
            "differentiating_factors": "Characterized by multiple, persistent physical symptoms without a clear medical explanation. Patients often seek care from many different doctors.",
        },
        "Conversion Disorder": {
            "symptoms": ["weakness", "paralysis", "seizures", "blindness", "sensory loss"],
            "differentiating_factors": "Presents with neurological symptoms (e.g., paralysis) that are incompatible with a known neurological or medical condition. Often a psychological cause.",
        },
        "Factitious Disorder (Munchausen Syndrome)": {
            "symptoms": ["unusual symptoms", "multiple hospital visits", "lying about symptoms"],
            "differentiating_factors": "Falsification of physical or psychological symptoms without an obvious external reward. The motivation is to assume the sick role.",
        },
        "Malingering": {
            "symptoms": ["fabricated symptoms"],
            "differentiating_factors": "Intentional production of false or grossly exaggerated physical or psychological symptoms motivated by external incentives, like financial gain or avoiding work.",
        },
        "Acute Coronary Syndrome (ACS)": {
            "symptoms": ["chest pain", "chest pressure", "radiating arm pain", "shortness of breath", "nausea"],
            "differentiating_factors": "A group of conditions that includes unstable angina and myocardial infarction. Differentiated by EKG changes and cardiac enzymes.",
        },
        "Congenital Heart Defects": {
            "symptoms": ["cyanosis", "dyspnea", "failure to thrive", "murmur"],
            "differentiating_factors": "Present in infants and children. Specific symptoms depend on the type of defect (e.g., Tetralogy of Fallot, VSD, ASD).",
        },
        "End-Stage Renal Disease (ESRD)": {
            "symptoms": ["fatigue", "weakness", "nausea", "uremic pruritus", "peripheral edema"],
            "differentiating_factors": "A chronic, irreversible state of kidney failure. Patients often require dialysis or a kidney transplant. Labs show significantly elevated BUN and creatinine.",
        },
        "Urolithiasis (Kidney Stones)": {
            "symptoms": ["flank pain", "hematuria", "nausea", "vomiting"],
            "differentiating_factors": "Severe, colicky pain radiating from the flank to the groin. Hematuria is common. Often associated with a history of dehydration.",
        },
        "Gastroesophageal Varices": {
            "symptoms": ["hematemesis", "melena", "fatigue", "abdominal pain"],
            "differentiating_factors": "Enlarged veins in the esophagus or stomach, often due to portal hypertension from cirrhosis. Bleeding is a medical emergency.",
        },
        "Small Bowel Obstruction (SBO)": {
            "symptoms": ["abdominal pain", "vomiting", "bloating", "constipation"],
            "differentiating_factors": "Pain is colicky and intermittent. Vomiting is often bilious. Abdominal distention and absent bowel sounds are key exam findings. X-ray shows dilated loops of small bowel.",
        },
        "Large Bowel Obstruction (LBO)": {
            "symptoms": ["abdominal pain", "bloating", "constipation", "vomiting"],
            "differentiating_factors": "Symptoms are often more gradual than SBO. Vomiting is often feculent. Abdominal distention is more pronounced.",
        },
        "Diverticulitis": {
            "symptoms": ["abdominal pain", "fever", "nausea", "change in bowel habits"],
            "differentiating_factors": "Pain is typically in the left lower quadrant and is associated with fever and elevated white blood cell count. Imaging (CT scan) is diagnostic.",
        },
        "Anorectal Abscess": {
            "symptoms": ["anorectal pain", "swelling", "fever", "perirectal fullness"],
            "differentiating_factors": "Severe, throbbing pain in the anal area. Patients may have a palpable, tender mass. Often requires surgical drainage.",
        },
        "Hemorrhoids": {
            "symptoms": ["rectal bleeding", "itching", "pain", "prolapse"],
            "differentiating_factors": "Swollen veins in the rectum or anus. Bleeding is typically bright red and painless. Can be painful if thrombosed.",
        },
        "Anal Fissure": {
            "symptoms": ["anorectal pain", "rectal bleeding"],
            "differentiating_factors": "A small tear in the lining of the anal canal. Pain is sharp and severe, often described as 'tearing' or 'burning' during and after a bowel movement.",
        },
        "Esophagitis": {
            "symptoms": ["dysphagia", "odynophagia", "heartburn", "chest pain"],
            "differentiating_factors": "Inflammation of the esophagus. Painful swallowing is a key symptom. Often caused by reflux, infection, or medication side effects.",
        },
        "Barrett's Esophagus": {
            "symptoms": ["heartburn", "dysphagia"],
            "differentiating_factors": "A complication of chronic GERD where the esophageal lining changes. Often asymptomatic but is a precursor to esophageal cancer.",
        },
        "Achalasia": {
            "symptoms": ["dysphagia", "regurgitation", "weight loss"],
            "differentiating_factors": "A motility disorder of the esophagus. Patients have difficulty swallowing both solids and liquids. Barium swallow shows a 'bird's beak' appearance.",
        },
        "Scleroderma (Systemic Sclerosis)": {
            "symptoms": ["skin thickening", "Raynaud's phenomenon", "dysphagia", "shortness of breath", "joint pain"],
            "differentiating_factors": "An autoimmune disease affecting connective tissue. The CREST syndrome (Calcinosis, Raynaud's, Esophageal dysmotility, Sclerodactyly, Telangiectasias) is a key presentation.",
        },
        "Polymyositis/Dermatomyositis": {
            "symptoms": ["muscle weakness", "fatigue", "rash", "joint pain", "difficulty swallowing"],
            "differentiating_factors": "An inflammatory myopathy. Presents with symmetrical proximal muscle weakness. Dermatomyositis also includes characteristic rashes (Heliotrope rash, Gottron's papules).",
        },
        "Osteomyelitis": {
            "symptoms": ["fever", "localized pain", "swelling", "tenderness"],
            "differentiating_factors": "Infection of the bone. Pain is often severe and unremitting. Diagnosis requires imaging (MRI) and a positive culture.",
        },
        "Spondylolisthesis": {
            "symptoms": ["low back pain", "radiculopathy"],
            "differentiating_factors": "Forward slip of one vertebra over another. Causes low back pain that worsens with activity. Can cause nerve impingement and radiculopathy.",
        },
        "Sciatica": {
            "symptoms": ["radiculopathy", "lower back pain", "leg pain", "numbness"],
            "differentiating_factors": "Pain that radiates along the path of the sciatic nerve. Often caused by a herniated disc or spinal stenosis. The pain is usually unilateral.",
        },
        "Spinal Stenosis": {
            "symptoms": ["back pain", "leg pain", "numbness", "weakness"],
            "differentiating_factors": "Narrowing of the spinal canal. Causes neurogenic claudication, where leg pain occurs with standing/walking and is relieved by sitting or leaning forward.",
        },
        "Sjögren's Syndrome": {
            "symptoms": ["dry mouth", "dry eyes", "fatigue", "joint pain"],
            "differentiating_factors": "An autoimmune disorder affecting exocrine glands. Classic symptoms are dry mouth (xerostomia) and dry eyes (keratoconjunctivitis sicca).",
        },
        "Myasthenia Gravis": {
            "symptoms": ["muscle weakness", "ptosis", "diplopia", "dysphagia", "slurred speech"],
            "differentiating_factors": "An autoimmune disorder affecting neuromuscular junctions. Presents with fluctuating muscle weakness that worsens with activity and improves with rest.",
        },
        "Amyotrophic Lateral Sclerosis (ALS)": {
            "symptoms": ["muscle weakness", "slurred speech", "difficulty swallowing", "muscle twitching"],
            "differentiating_factors": "A progressive neurodegenerative disease affecting motor neurons. Presents with a combination of upper motor neuron signs (spasticity, hyperreflexia) and lower motor neuron signs (atrophy, fasciculations).",
        },
        "Huntington's Disease": {
            "symptoms": ["chorea", "dementia", "mood swings", "involuntary movements"],
            "differentiating_factors": "An inherited neurodegenerative disorder. The classic triad is motor dysfunction (chorea), cognitive decline, and psychiatric symptoms. Onset is typically in mid-adulthood.",
        },
        "Tourette Syndrome": {
            "symptoms": ["motor tics", "vocal tics", "involuntary movements", "behavioral problems"],
            "differentiating_factors": "Characterized by multiple motor tics and at least one vocal tic. Onset is typically in childhood. Tics are suppressible but often return with greater intensity.",
        },
        "Narcolepsy": {
            "symptoms": ["daytime sleepiness", "cataplexy", "sleep paralysis", "hypnagogic hallucinations"],
            "differentiating_factors": "A chronic neurological disorder affecting sleep-wake cycles. Cataplexy (sudden loss of muscle tone) triggered by strong emotions is a key feature.",
        },
        "Obstructive Sleep Apnea (OSA)": {
            "symptoms": ["snoring", "daytime sleepiness", "apnea", "fatigue"],
            "differentiating_factors": "Recurrent episodes of upper airway obstruction during sleep. The gold standard for diagnosis is a polysomnography (sleep study).",
        },
        "Restless Legs Syndrome (RLS)": {
            "symptoms": ["restless legs", "tingling", "unpleasant leg sensations", "insomnia"],
            "differentiating_factors": "An urge to move the legs, usually due to unpleasant sensations. Symptoms are worse at rest and are relieved by movement. Often worse in the evening/night.",
        },
        "Fibroadenoma": {
            "symptoms": ["breast lump", "mobile mass"],
            "differentiating_factors": "A benign breast tumor. Typically presents as a firm, rubbery, well-defined, and mobile mass. Common in young women.",
        },
        "Breast Cancer": {
            "symptoms": ["breast lump", "nipple discharge", "skin dimpling", "swollen lymph nodes"],
            "differentiating_factors": "A malignant breast tumor. Lumps are often hard, irregular, and non-mobile. Requires a biopsy for definitive diagnosis.",
        },
        "Prostate Cancer": {
            "symptoms": ["urinary hesitancy", "frequent urination", "back pain", "pelvic pain"],
            "differentiating_factors": "A malignant tumor of the prostate gland. Often asymptomatic initially. Can cause obstructive urinary symptoms and bone pain if it metastasizes.",
        },
        "Testicular Torsion": {
            "symptoms": ["testicular pain", "swelling"],
            "differentiating_factors": "A surgical emergency where the testicle twists. Presents with sudden onset of severe testicular pain and swelling. The cremasteric reflex is absent.",
        },
        "Epididymitis": {
            "symptoms": ["testicular pain", "swelling", "fever"],
            "differentiating_factors": "Inflammation of the epididymis. Pain is gradual in onset and is often relieved by lifting the testicle (Prehn's sign).",
        },
        "Renal Cell Carcinoma (RCC)": {
            "symptoms": ["hematuria", "flank pain", "abdominal mass", "weight loss"],
            "differentiating_factors": "A kidney cancer. The classic triad is hematuria, flank pain, and an abdominal mass. Often associated with paraneoplastic syndromes.",
        },
        "Polycystic Kidney Disease (PKD)": {
            "symptoms": ["flank pain", "hematuria", "hypertension", "renal cysts"],
            "differentiating_factors": "A genetic disorder causing multiple cysts to grow on the kidneys. Patients often have a family history and hypertension. Can progress to ESRD.",
        },
        "Urinary Incontinence": {
            "symptoms": ["urinary incontinence", "urinary urgency", "frequent urination"],
            "differentiating_factors": "Involuntary leakage of urine. Different types include stress, urge, and overflow incontinence. The cause and treatment vary.",
        },
        "Cystitis (Bladder Infection)": {
            "symptoms": ["dysuria", "frequent urination", "urinary urgency", "pelvic pain"],
            "differentiating_factors": "Inflammation of the bladder, often due to a bacterial infection. Symptoms are localized to the bladder. Often associated with a positive urine culture.",
        },
        "Urethritis": {
            "symptoms": ["dysuria", "urethral discharge", "itching"],
            "differentiating_factors": "Inflammation of the urethra. Often caused by sexually transmitted infections (STIs). Discharge can be purulent or watery.",
        },
        "Acute Tubular Necrosis (ATN)": {
            "symptoms": ["oliguria", "anuria", "fatigue", "nausea"],
            "differentiating_factors": "Damage to the kidney tubules, often caused by ischemia or toxins. A major cause of intrinsic acute kidney injury. Urine studies often show muddy brown casts.",
        },
        "Anemia": {
            "symptoms": ["fatigue", "weakness", "pale skin", "shortness of breath", "tachycardia"],
            "differentiating_factors": "A decrease in red blood cells or hemoglobin. Different types (e.g., iron-deficiency, B12 deficiency) have unique differentiating factors and lab findings.",
        },
        "Hemophilia": {
            "symptoms": ["easy bruising", "excessive bleeding", "joint pain", "hemarthrosis"],
            "differentiating_factors": "A genetic bleeding disorder. Patients have prolonged bleeding after injury or surgery. Hemarthrosis (bleeding into joints) is a classic finding.",
        },
        "Thrombocytopenia": {
            "symptoms": ["easy bruising", "petechiae", "purpura", "gingival bleeding", "epistaxis"],
            "differentiating_factors": "A low platelet count. Leads to easy bruising and bleeding from mucosal surfaces. Diagnosis is based on a CBC.",
        },
        "Leukemia": {
            "symptoms": ["fatigue", "fever", "night sweats", "easy bruising", "bleeding gums", "lymphadenopathy"],
            "differentiating_factors": "A cancer of the blood. Presents with constitutional symptoms, bleeding, and infections. Diagnosis is made with a bone marrow biopsy.",
        },
        "Lymphoma": {
            "symptoms": ["swollen lymph nodes", "night sweats", "fever", "weight loss", "fatigue"],
            "differentiating_factors": "A cancer of the lymphatic system. Presents with painless lymphadenopathy and 'B symptoms' (fever, night sweats, weight loss).",
        },
        "Multiple Myeloma": {
            "symptoms": ["bone pain", "fatigue", "anemia", "pathological fractures"],
            "differentiating_factors": "A cancer of plasma cells. The classic CRAB mnemonic stands for Hypercalcemia, Renal failure, Anemia, and Bone lesions. Pain is often in the back or ribs.",
        },
        "Sarcoidosis": {
            "symptoms": ["cough", "shortness of breath", "fatigue", "erythema nodosum", "swollen lymph nodes"],
            "differentiating_factors": "An inflammatory disease characterized by the formation of granulomas. Often affects the lungs, lymph nodes, and skin. Erythema nodosum is a key skin finding.",
        },
        "Systemic Lupus Erythematosus (SLE)": {
            "symptoms": ["malar rash", "joint pain", "fatigue", "fever", "photosensitivity"],
            "differentiating_factors": "A systemic autoimmune disease. The classic butterfly-shaped malar rash is a hallmark sign. ANA is almost always positive.",
        },
        "Sjogren's Syndrome": {
            "symptoms": ["dry eyes", "dry mouth", "fatigue", "joint pain"],
            "differentiating_factors": "An autoimmune disease affecting moisture-producing glands. The sicca symptoms (dryness) are key. Often associated with rheumatoid arthritis or lupus.",
        },
        "Gastroesophageal Reflux Disease (GERD)": {
            "symptoms": ["heartburn", "acid reflux", "chest pain", "dysphagia", "cough"],
            "differentiating_factors": "Burning retrosternal chest pain (heartburn) that worsens after meals, when lying down, or with bending over. The pain is not exertional and is not associated with signs of MI.",
        },
        "Gastric Ulcer": {
            "symptoms": ["abdominal pain", "nausea", "indigestion", "melena"],
            "differentiating_factors": "Epigastric pain that is worsened by food. Can lead to bleeding, presenting as melena or hematemesis.",
        },
        "Duodenal Ulcer": {
            "symptoms": ["abdominal pain", "indigestion", "heartburn"],
            "differentiating_factors": "Epigastric pain that is relieved by food. Often wakes the patient up at night. The pain can be gnawing or burning.",
        },
        "Celiac Disease": {
            "symptoms": ["diarrhea", "abdominal pain", "bloating", "weight loss", "fatigue"],
            "differentiating_factors": "An autoimmune reaction to gluten. Symptoms improve on a gluten-free diet. Can lead to malabsorption.",
        },
        "Lactose Intolerance": {
            "symptoms": ["diarrhea", "abdominal pain", "bloating", "flatulence"],
            "differentiating_factors": "Symptoms occur after consuming dairy products. The gold standard for diagnosis is a lactose tolerance test or hydrogen breath test.",
        },
        "Appendicitis": {
            "symptoms": ["abdominal pain", "nausea", "vomiting", "fever", "loss of appetite"],
            "differentiating_factors": "Pain begins periumbilically and migrates to the right lower quadrant. Rebound tenderness and guarding on exam at McBurney's point are classic.",
        },
        "Diverticulitis": {
            "symptoms": ["abdominal pain", "fever", "nausea", "change in bowel habits"],
            "differentiating_factors": "Pain is typically in the left lower quadrant and is associated with fever and elevated white blood cell count. Imaging (CT scan) is diagnostic.",
        },
        "Cholecystitis": {
            "symptoms": ["abdominal pain", "nausea", "vomiting", "fever"],
            "differentiating_factors": "Pain is in the right upper quadrant and may radiate to the right shoulder. Often triggered by a fatty meal. A positive Murphy's sign is highly suggestive.",
        },
        "Pancreatitis": {
            "symptoms": ["abdominal pain", "nausea", "vomiting", "fever"],
            "differentiating_factors": "Abdominal pain is severe, constant, and radiates to the back. A history of heavy alcohol use or gallstones is common. Labs show elevated lipase and amylase.",
        },
        "Hepatitis (Viral)": {
            "symptoms": ["fatigue", "nausea", "vomiting", "jaundice", "right upper quadrant pain"],
            "differentiating_factors": "Inflammation of the liver, caused by a virus. Labs show elevated liver enzymes. Differentiated by serology for the specific viral agent.",
        },
        "Gallstones (Cholelithiasis)": {
            "symptoms": ["abdominal pain", "nausea", "vomiting"],
            "differentiating_factors": "Pain is in the right upper quadrant and is colicky, often occurring after eating a fatty meal. Ultrasound is the diagnostic study of choice.",
        },
        "Cholangitis": {
            "symptoms": ["fever", "jaundice", "right upper quadrant pain"],
            "differentiating_factors": "Infection of the bile ducts. The classic Charcot's triad is fever, jaundice, and RUQ pain. Can be a life-threatening emergency.",
        },
        "Crohn's Disease": {
            "symptoms": ["abdominal pain", "diarrhea", "fatigue", "weight loss", "oral sores"],
            "differentiating_factors": "A type of Inflammatory Bowel Disease characterized by patchy, transmural inflammation anywhere from mouth to anus. Fistulas and strictures are common.",
        },
        "Ulcerative Colitis (UC)": {
            "symptoms": ["abdominal pain", "diarrhea", "blood in stool", "fatigue", "weight loss", "tenesmus"],
            "differentiating_factors": "A type of Inflammatory Bowel Disease characterized by continuous inflammation starting in the rectum. Presents with bloody diarrhea and tenesmus.",
        },
        "Celiac Disease": {
            "symptoms": ["diarrhea", "abdominal pain", "bloating", "weight loss", "fatigue"],
            "differentiating_factors": "An autoimmune reaction to gluten. Symptoms improve dramatically on a gluten-free diet. Can lead to malabsorption.",
        },
        "Irritable Bowel Syndrome (IBS)": {
            "symptoms": ["abdominal pain", "bloating", "diarrhea", "constipation"],
            "differentiating_factors": "Chronic abdominal pain associated with changes in bowel habits. Diagnosis is based on clinical criteria and exclusion of other pathologies.",
        },
        "Diabetic Neuropathy": {
            "symptoms": ["numbness", "tingling", "pain", "muscle weakness"],
            "differentiating_factors": "Nerve damage caused by long-term high blood sugar. Often presents as a 'stocking-glove' distribution of symptoms in the feet and hands.",
        },
        "Diabetic Nephropathy": {
            "symptoms": ["leg swelling", "fatigue", "hypertension", "proteinuria"],
            "differentiating_factors": "Damage to the kidneys caused by diabetes. The leading cause of end-stage renal disease. Microalbuminuria is an early sign.",
        },
        "Diabetic Retinopathy": {
            "symptoms": ["blurred vision", "double vision", "floaters"],
            "differentiating_factors": "Damage to the blood vessels of the retina caused by diabetes. A leading cause of blindness in adults.",
        },
        "Hypertensive Crisis": {
            "symptoms": ["severe headache", "blurred vision", "dizziness", "shortness of breath", "chest pain"],
            "differentiating_factors": "A severe increase in blood pressure that can lead to stroke, heart attack, or kidney damage. Differentiated by end-organ damage.",
        },
        "Renal Artery Stenosis": {
            "symptoms": ["hypertension", "flank pain"],
            "differentiating_factors": "Narrowing of the renal arteries. Causes secondary hypertension that is often resistant to medication. A renal bruit may be heard on exam.",
        },
        "Glomerulonephritis": {
            "symptoms": ["hematuria", "hypertension", "edema", "oliguria"],
            "differentiating_factors": "Inflammation of the glomeruli. Can be acute or chronic. Presents with a nephritic or nephrotic picture depending on the type.",
        },
        "Bipolar II Disorder": {
            "symptoms": ["hypomania", "depression", "insomnia", "fatigue", "mood swings"],
            "differentiating_factors": "Characterized by at least one major depressive episode and at least one hypomanic episode. Unlike Bipolar I, there is no history of a full manic episode.",
        },
        "Generalized Anxiety Disorder (GAD)": {
            "symptoms": ["anxiety", "worry", "restlessness", "fatigue", "difficulty sleeping", "muscle tension"],
            "differentiating_factors": "Excessive and uncontrollable worry about a variety of things for at least 6 months. Worry is out of proportion to the actual likelihood of a negative event.",
        },
        "Post-Traumatic Stress Disorder (PTSD)": {
            "symptoms": ["flashbacks", "anxiety", "difficulty sleeping", "avoidance", "irritability"],
            "differentiating_factors": "Symptoms arise after exposure to a traumatic event. The core features are re-experiencing the event, avoidance, negative changes in cognition/mood, and hyperarousal.",
        },
        "Obsessive-Compulsive Disorder (OCD)": {
            "symptoms": ["obsessive thoughts", "compulsive behaviors", "anxiety", "repetitive actions"],
            "differentiating_factors": "Characterized by obsessions (recurrent, unwanted thoughts) and compulsions (repetitive behaviors) that an individual feels driven to perform to reduce anxiety.",
        },
        "Schizoaffective Disorder": {
            "symptoms": ["psychosis", "hallucinations", "delusions", "depression", "mania"],
            "differentiating_factors": "A combination of symptoms of schizophrenia (psychosis) and a mood disorder (mania or depression). Psychosis must be present for at least two weeks without prominent mood symptoms.",
        },
        "Borderline Personality Disorder (BPD)": {
            "symptoms": ["mood swings", "impulsivity", "fear of abandonment", "unstable relationships"],
            "differentiating_factors": "A pervasive pattern of instability in interpersonal relationships, self-image, and affects. Often associated with self-harm and intense, inappropriate anger.",
        },
        "Anorexia Nervosa": {
            "symptoms": ["weight loss", "fear of gaining weight", "distorted body image", "amenorrhea", "bradycardia"],
            "differentiating_factors": "Intense fear of gaining weight and a distorted perception of body shape. Characterized by a significantly low body weight. Often associated with amenorrhea in females.",
        },
        "Bulimia Nervosa": {
            "symptoms": ["binge eating", "purging", "body image concerns", "weight gain", "tooth enamel erosion"],
            "differentiating_factors": "Recurrent episodes of binge eating followed by compensatory behaviors like self-induced vomiting or excessive exercise. Patients are often a normal weight or overweight.",
        },
        "Adjustment Disorder": {
            "symptoms": ["depression", "anxiety", "mood swings", "difficulty sleeping"],
            "differentiating_factors": "Emotional or behavioral symptoms that develop within 3 months of an identifiable stressor. The symptoms are clinically significant but do not meet criteria for a major depressive episode.",
        },
        "Delirium": {
            "symptoms": ["confusion", "disorientation", "hallucinations", "fluctuating consciousness"],
            "differentiating_factors": "An acute change in mental status, often caused by a medical condition or substance intoxication/withdrawal. Consciousness level fluctuates throughout the day.",
        },
        "Dementia": {
            "symptoms": ["memory loss", "confusion", "cognitive decline", "difficulty with language", "social withdrawal"],
            "differentiating_factors": "A progressive, chronic decline in cognitive function that interferes with daily living. Onset is insidious. Alzheimer's is the most common cause.",
        },
        "Alzheimer's Disease": {
            "symptoms": ["memory loss", "confusion", "difficulty with language", "difficulty with problem-solving"],
            "differentiating_factors": "The most common type of dementia. Characterized by a progressive decline in memory and cognitive function. Pathological hallmarks are amyloid plaques and neurofibrillary tangles.",
        },
        "Vascular Dementia": {
            "symptoms": ["confusion", "memory loss", "slurred speech", "balance problems", "unilateral weakness"],
            "differentiating_factors": "Cognitive decline caused by cerebrovascular disease. Often has a 'step-wise' progression, with sudden declines in function after a series of small strokes.",
        },
        "Lewy Body Dementia": {
            "symptoms": ["dementia", "visual hallucinations", "parkinsonian symptoms", "fluctuating cognition"],
            "differentiating_factors": "A type of dementia with a unique triad of dementia, parkinsonian features, and visual hallucinations. Patients often have vivid dreams and fluctuating attention.",
        },
        "Frontotemporal Dementia": {
            "symptoms": ["personality changes", "apathy", "social withdrawal", "language problems"],
            "differentiating_factors": "A group of disorders causing progressive nerve cell loss in the frontal or temporal lobes. Often presents with behavioral changes or language deficits before memory loss.",
        },
        "Narcolepsy with Cataplexy": {
            "symptoms": ["excessive daytime sleepiness", "cataplexy", "sleep paralysis", "hypnagogic hallucinations"],
            "differentiating_factors": "A chronic sleep disorder. Cataplexy, a sudden loss of muscle tone triggered by strong emotions, is a hallmark feature.",
        },
        "Obstructive Sleep Apnea (OSA)": {
            "symptoms": ["snoring", "daytime sleepiness", "apnea", "fatigue"],
            "differentiating_factors": "Recurrent episodes of upper airway obstruction during sleep. The gold standard for diagnosis is a polysomnography (sleep study).",
        },
        "Insomnia": {
            "symptoms": ["difficulty sleeping", "daytime sleepiness", "fatigue"],
            "differentiating_factors": "Difficulty initiating or maintaining sleep, leading to daytime impairment. It can be a primary disorder or a symptom of another condition.",
        },
        "Rheumatoid Arthritis (RA)": {
            "symptoms": ["joint pain", "joint stiffness", "swelling", "joint swelling", "fatigue", "morning stiffness"],
            "differentiating_factors": "Symmetrical joint involvement, especially in the small joints of the hands and feet. Morning stiffness lasting more than 30 minutes is a key feature.",
        },
        "Osteoarthritis (OA)": {
            "symptoms": ["joint pain", "joint stiffness", "bony enlargement"],
            "differentiating_factors": "Asymmetrical joint involvement, primarily in weight-bearing joints. Morning stiffness is brief (<30 minutes). Pain worsens with activity and improves with rest.",
        },
        "Gout": {
            "symptoms": ["joint pain", "joint swelling", "joint redness", "fever"],
            "differentiating_factors": "Sudden onset of severe pain in a single joint, often the big toe. Caused by hyperuricemia and crystal deposition. 'Podagra' is the term for gout in the big toe.",
        },
        "Psoriatic Arthritis": {
            "symptoms": ["joint pain", "joint stiffness", "psoriasis plaques", "nail pitting"],
            "differentiating_factors": "An inflammatory arthritis that affects some people with psoriasis. Dactylitis ('sausage digits') is a classic sign.",
        },
        "Fibromyalgia": {
            "symptoms": ["widespread pain", "fatigue", "sleep disturbance", "cognitive dysfunction", "headache"],
            "differentiating_factors": "Characterized by chronic widespread pain and tenderness in specific 'tender points.' Often associated with fatigue, sleep, and mood issues. Diagnosis is clinical.",
        },
        "Polymyalgia Rheumatica (PMR)": {
            "symptoms": ["muscle aches", "joint stiffness", "weakness", "fever", "weight loss"],
            "differentiating_factors": "An inflammatory disorder causing muscle pain and stiffness, especially in the shoulders and hips. Primarily affects people over 50. Responds well to low-dose steroids.",
        },
        "Sepsis": {
            "symptoms": ["fever", "chills", "tachycardia", "confusion", "hypotension"],
            "differentiating_factors": "Systemic inflammatory response to an infection. Look for signs of organ dysfunction (e.g., altered mental status, hypotension, oliguria).",
        },
        "Toxic Shock Syndrome (TSS)": {
            "symptoms": ["fever", "hypotension", "rash", "confusion", "vomiting"],
            "differentiating_factors": "A life-threatening complication of a bacterial infection. Presents with a high fever, diffuse erythematous rash, and hypotension. Often associated with tampon use.",
        },
        "Acute Renal Failure (ARF)": {
            "symptoms": ["oliguria", "anuria", "swelling", "fatigue", "nausea", "confusion"],
            "differentiating_factors": "Rapid decline in kidney function. Can be pre-renal (dehydration), intra-renal (ATN), or post-renal (obstruction).",
        },
        "Polycystic Kidney Disease (PKD)": {
            "symptoms": ["flank pain", "hematuria", "hypertension", "renal cysts"],
            "differentiating_factors": "A genetic disorder causing multiple cysts to grow on the kidneys. Patients often have a family history and hypertension. Can progress to ESRD.",
        },
        "Goodpasture Syndrome": {
            "symptoms": ["hemoptysis", "shortness of breath", "hematuria", "glomerulonephritis"],
            "differentiating_factors": "An autoimmune disease affecting the kidneys and lungs. Characterized by glomerulonephritis and pulmonary hemorrhage. Anti-GBM antibodies are diagnostic.",
        },
        "Wegener's Granulomatosis (GPA)": {
            "symptoms": ["nasal congestion", "sinus pressure", "cough", "hemoptysis", "glomerulonephritis"],
            "differentiating_factors": "A vasculitis affecting small- and medium-sized vessels. Presents with a classic triad of upper respiratory, lower respiratory, and renal symptoms. C-ANCA is often positive.",
        },
        "Lupus Nephritis": {
            "symptoms": ["hematuria", "proteinuria", "hypertension", "edema", "fatigue"],
            "differentiating_factors": "A serious kidney complication of systemic lupus erythematosus. Diagnosis requires a kidney biopsy. Presents with signs of glomerulonephritis or nephrotic syndrome.",
        },
        "Bipolar II Disorder": {
            "symptoms": ["hypomania", "depression", "insomnia", "fatigue", "mood swings"],
            "differentiating_factors": "Characterized by at least one major depressive episode and at least one hypomanic episode. Unlike Bipolar I, there is no history of a full manic episode.",
        },
        "Generalized Anxiety Disorder (GAD)": {
            "symptoms": ["anxiety", "worry", "restlessness", "fatigue", "difficulty sleeping", "muscle tension"],
            "differentiating_factors": "Excessive and uncontrollable worry about a variety of things for at least 6 months. Worry is out of proportion to the actual likelihood of a negative event.",
        },
        "Post-Traumatic Stress Disorder (PTSD)": {
            "symptoms": ["flashbacks", "anxiety", "difficulty sleeping", "avoidance", "irritability"],
            "differentiating_factors": "Symptoms arise after exposure to a traumatic event. The core features are re-experiencing the event, avoidance, negative changes in cognition/mood, and hyperarousal.",
        },
        "Obsessive-Compulsive Disorder (OCD)": {
            "symptoms": ["obsessive thoughts", "compulsive behaviors", "anxiety", "repetitive actions"],
            "differentiating_factors": "Characterized by obsessions (recurrent, unwanted thoughts) and compulsions (repetitive behaviors) that an individual feels driven to perform to reduce anxiety.",
        },
        "Schizoaffective Disorder": {
            "symptoms": ["psychosis", "hallucinations", "delusions", "depression", "mania"],
            "differentiating_factors": "A combination of symptoms of schizophrenia (psychosis) and a mood disorder (mania or depression). Psychosis must be present for at least two weeks without prominent mood symptoms.",
        },
        "Borderline Personality Disorder (BPD)": {
            "symptoms": ["mood swings", "impulsivity", "fear of abandonment", "unstable relationships"],
            "differentiating_factors": "A pervasive pattern of instability in interpersonal relationships, self-image, and affects. Often associated with self-harm and intense, inappropriate anger.",
        },
        "Anorexia Nervosa": {
            "symptoms": ["weight loss", "fear of gaining weight", "distorted body image", "amenorrhea", "bradycardia"],
            "differentiating_factors": "Intense fear of gaining weight and a distorted perception of body shape. Characterized by a significantly low body weight. Often associated with amenorrhea in females.",
        },
        "Bulimia Nervosa": {
            "symptoms": ["binge eating", "purging", "body image concerns", "weight gain", "tooth enamel erosion"],
            "differentiating_factors": "Recurrent episodes of binge eating followed by compensatory behaviors like self-induced vomiting or excessive exercise. Patients are often a normal weight or overweight.",
        },
        "Adjustment Disorder": {
            "symptoms": ["depression", "anxiety", "mood swings", "difficulty sleeping"],
            "differentiating_factors": "Emotional or behavioral symptoms that develop within 3 months of an identifiable stressor. The symptoms are clinically significant but do not meet criteria for a major depressive episode.",
        },
        "Delirium": {
            "symptoms": ["confusion", "disorientation", "hallucinations", "fluctuating consciousness"],
            "differentiating_factors": "An acute change in mental status, often caused by a medical condition or substance intoxication/withdrawal. Consciousness level fluctuates throughout the day.",
        },
        "Dementia": {
            "symptoms": ["memory loss", "confusion", "cognitive decline", "difficulty with language", "social withdrawal"],
            "differentiating_factors": "A progressive, chronic decline in cognitive function that interferes with daily living. Onset is insidious. Alzheimer's is the most common cause.",
        },
        "Alzheimer's Disease": {
            "symptoms": ["memory loss", "confusion", "difficulty with language", "difficulty with problem-solving"],
            "differentiating_factors": "The most common type of dementia. Characterized by a progressive decline in memory and cognitive function. Pathological hallmarks are amyloid plaques and neurofibrillary tangles.",
        },
        "Vascular Dementia": {
            "symptoms": ["confusion", "memory loss", "slurred speech", "balance problems", "unilateral weakness"],
            "differentiating_factors": "Cognitive decline caused by cerebrovascular disease. Often has a 'step-wise' progression, with sudden declines in function after a series of small strokes.",
        },
        "Lewy Body Dementia": {
            "symptoms": ["dementia", "visual hallucinations", "parkinsonian symptoms", "fluctuating cognition"],
            "differentiating_factors": "A type of dementia with a unique triad of dementia, parkinsonian features, and visual hallucinations. Patients often have vivid dreams and fluctuating attention.",
        },
        "Frontotemporal Dementia": {
            "symptoms": ["personality changes", "apathy", "social withdrawal", "language problems"],
            "differentiating_factors": "A group of disorders causing progressive nerve cell loss in the frontal or temporal lobes. Often presents with behavioral changes or language deficits before memory loss.",
        },
        "Narcolepsy with Cataplexy": {
            "symptoms": ["excessive daytime sleepiness", "cataplexy", "sleep paralysis", "hypnagogic hallucinations"],
            "differentiating_factors": "A chronic sleep disorder. Cataplexy, a sudden loss of muscle tone triggered by strong emotions, is a hallmark feature.",
        },
        "Obstructive Sleep Apnea (OSA)": {
            "symptoms": ["snoring", "daytime sleepiness", "apnea", "fatigue"],
            "differentiating_factors": "Recurrent episodes of upper airway obstruction during sleep. The gold standard for diagnosis is a polysomnography (sleep study).",
        },
        "Insomnia": {
            "symptoms": ["difficulty sleeping", "daytime sleepiness", "fatigue"],
            "differentiating_factors": "Difficulty initiating or maintaining sleep, leading to daytime impairment. It can be a primary disorder or a symptom of another condition.",
        },
        "Rheumatoid Arthritis (RA)": {
            "symptoms": ["joint pain", "joint stiffness", "swelling", "joint swelling", "fatigue", "morning stiffness"],
            "differentiating_factors": "Symmetrical joint involvement, especially in the small joints of the hands and feet. Morning stiffness lasting more than 30 minutes is a key feature.",
        },
        "Osteoarthritis (OA)": {
            "symptoms": ["joint pain", "joint stiffness", "bony enlargement"],
            "differentiating_factors": "Asymmetrical joint involvement, primarily in weight-bearing joints. Morning stiffness is brief (<30 minutes). Pain worsens with activity and improves with rest.",
        },
        "Gout": {
            "symptoms": ["joint pain", "joint swelling", "joint redness", "fever"],
            "differentiating_factors": "Sudden onset of severe pain in a single joint, often the big toe. Caused by hyperuricemia and crystal deposition. 'Podagra' is the term for gout in the big toe.",
        },
        "Psoriatic Arthritis": {
            "symptoms": ["joint pain", "joint stiffness", "psoriasis plaques", "nail pitting"],
            "differentiating_factors": "An inflammatory arthritis that affects some people with psoriasis. Dactylitis ('sausage digits') is a classic sign.",
        },
        "Fibromyalgia": {
            "symptoms": ["widespread pain", "fatigue", "sleep disturbance", "cognitive dysfunction", "headache"],
            "differentiating_factors": "Characterized by chronic widespread pain and tenderness in specific 'tender points.' Often associated with fatigue, sleep, and mood issues. Diagnosis is clinical.",
        },
        "Polymyalgia Rheumatica (PMR)": {
            "symptoms": ["muscle aches", "joint stiffness", "weakness", "fever", "weight loss"],
            "differentiating_factors": "An inflammatory disorder causing muscle pain and stiffness, especially in the shoulders and hips. Primarily affects people over 50. Responds well to low-dose steroids.",
        },
        "Sepsis": {
            "symptoms": ["fever", "chills", "tachycardia", "confusion", "hypotension"],
            "differentiating_factors": "Systemic inflammatory response to an infection. Look for signs of organ dysfunction (e.g., altered mental status, hypotension, oliguria).",
        },
        "Toxic Shock Syndrome (TSS)": {
            "symptoms": ["fever", "hypotension", "rash", "confusion", "vomiting"],
            "differentiating_factors": "A life-threatening complication of a bacterial infection. Presents with a high fever, diffuse erythematous rash, and hypotension. Often associated with tampon use.",
        },
        "Acute Renal Failure (ARF)": {
            "symptoms": ["oliguria", "anuria", "swelling", "fatigue", "nausea", "confusion"],
            "differentiating_factors": "Rapid decline in kidney function. Can be pre-renal (dehydration), intra-renal (ATN), or post-renal (obstruction).",
        },
        "Polycystic Kidney Disease (PKD)": {
            "symptoms": ["flank pain", "hematuria", "hypertension", "renal cysts"],
            "differentiating_factors": "A genetic disorder causing multiple cysts to grow on the kidneys. Patients often have a family history and hypertension. Can progress to ESRD.",
        },
        "Goodpasture Syndrome": {
            "symptoms": ["hemoptysis", "shortness of breath", "hematuria", "glomerulonephritis"],
            "differentiating_factors": "An autoimmune disease affecting the kidneys and lungs. Characterized by glomerulonephritis and pulmonary hemorrhage. Anti-GBM antibodies are diagnostic.",
        },
        "Wegener's Granulomatosis (GPA)": {
            "symptoms": ["nasal congestion", "sinus pressure", "cough", "hemoptysis", "glomerulonephritis"],
            "differentiating_factors": "A vasculitis affecting small- and medium-sized vessels. Presents with a classic triad of upper respiratory, lower respiratory, and renal symptoms. C-ANCA is often positive.",
        },
        "Lupus Nephritis": {
            "symptoms": ["hematuria", "proteinuria", "hypertension", "edema", "fatigue"],
            "differentiating_factors": "A serious kidney complication of systemic lupus erythematosus. Diagnosis requires a kidney biopsy. Presents with signs of glomerulonephritis or nephrotic syndrome.",
        },
        "Renal Cell Carcinoma (RCC)": {
            "symptoms": ["hematuria", "flank pain", "abdominal mass", "weight loss"],
            "differentiating_factors": "A kidney cancer. The classic triad is hematuria, flank pain, and an abdominal mass. Often associated with paraneoplastic syndromes.",
        },
        "Urinary Tract Infection (UTI)": {
            "symptoms": ["dysuria", "frequent urination", "urinary urgency", "pelvic pain"],
            "differentiating_factors": "Infection of the bladder or urethra. Symptoms are localized to the urinary tract. Often treated with a short course of antibiotics.",
        },
        "Pyelonephritis": {
            "symptoms": ["fever", "flank pain", "nausea", "vomiting", "dysuria"],
            "differentiating_factors": "A kidney infection. Symptoms include high fever, CVA tenderness, and dysuria. Often a progression from an untreated UTI.",
        },
        "Benign Prostatic Hyperplasia (BPH)": {
            "symptoms": ["urinary hesitancy", "frequent urination", "nocturia", "weak stream"],
            "differentiating_factors": "Enlargement of the prostate gland in older men. Causes obstructive urinary symptoms.",
        },
        "Cystitis (Bladder Infection)": {
            "symptoms": ["dysuria", "frequent urination", "urinary urgency", "pelvic pain"],
            "differentiating_factors": "Inflammation of the bladder, often due to a bacterial infection. Symptoms are localized to the bladder. Often associated with a positive urine culture.",
        },
        "Urethritis": {
            "symptoms": ["dysuria", "urethral discharge", "itching"],
            "differentiating_factors": "Inflammation of the urethra. Often caused by sexually transmitted infections (STIs). Discharge can be purulent or watery.",
        },
        "Testicular Torsion": {
            "symptoms": ["testicular pain", "swelling"],
            "differentiating_factors": "A surgical emergency where the testicle twists. Presents with sudden onset of severe testicular pain and swelling. The cremasteric reflex is absent.",
        },
        "Epididymitis": {
            "symptoms": ["testicular pain", "swelling", "fever"],
            "differentiating_factors": "Inflammation of the epididymis. Pain is gradual in onset and is often relieved by lifting the testicle (Prehn's sign).",
        },
        "Prostate Cancer": {
            "symptoms": ["urinary hesitancy", "frequent urination", "back pain", "pelvic pain"],
            "differentiating_factors": "A malignant tumor of the prostate gland. Often asymptomatic initially. Can cause obstructive urinary symptoms and bone pain if it metastasizes.",
        },
        "Acute Coronary Syndrome (ACS)": {
            "symptoms": ["chest pain", "chest pressure", "radiating arm pain", "shortness of breath", "nausea"],
            "differentiating_factors": "A group of conditions that includes unstable angina and myocardial infarction. Differentiated by EKG changes and cardiac enzymes.",
        },
        "Unstable Angina": {
            "symptoms": ["chest pain", "chest pressure", "shortness of breath"],
            "differentiating_factors": "Chest pain at rest or with minimal exertion. Unlike stable angina, it is not relieved by rest or nitroglycerin. No EKG changes or elevated troponins.",
        },
        "Congenital Heart Defects": {
            "symptoms": ["cyanosis", "dyspnea", "failure to thrive", "murmur"],
            "differentiating_factors": "Present in infants and children. Specific symptoms depend on the type of defect (e.g., Tetralogy of Fallot, VSD, ASD).",
        },
        "Atrial Fibrillation (Afib)": {
            "symptoms": ["heart palpitations", "shortness of breath", "chest pain", "lightheadedness", "fainting"],
            "differentiating_factors": "Irregularly irregular rhythm on EKG. Often presents as palpitations or symptoms of decreased cardiac output.",
        },
        "Atrial Flutter": {
            "symptoms": ["heart palpitations", "shortness of breath", "lightheadedness", "fainting"],
            "differentiating_factors": "EKG shows a classic 'sawtooth' pattern of atrial activity. Typically a more organized rhythm than Afib, with atrial rates around 300 bpm.",
        },
        "Ventricular Tachycardia": {
            "symptoms": ["heart palpitations", "dizziness", "chest pain", "fainting", "syncope"],
            "differentiating_factors": "A potentially life-threatening arrhythmia. EKG shows a wide QRS complex. Often a sign of underlying structural heart disease.",
        },
        "Tricuspid Regurgitation": {
            "symptoms": ["peripheral edema", "ascites", "jugular venous distention"],
            "differentiating_factors": "Incomplete closure of the tricuspid valve. Leads to right-sided heart failure symptoms. Often secondary to pulmonary hypertension or left-sided heart failure.",
        },
        "Mitral Stenosis": {
            "symptoms": ["dyspnea", "fatigue", "heart palpitations", "hemoptysis"],
            "differentiating_factors": "Narrowing of the mitral valve. Often a late complication of rheumatic fever. Leads to a classic 'opening snap' and a diastolic rumble on auscultation.",
        },
        "Aortic Stenosis": {
            "symptoms": ["syncope", "angina", "dyspnea", "heart murmur"],
            "differentiating_factors": "Narrowing of the aortic valve. Classic triad of syncope, angina, and dyspnea. Associated with a crescendo-decrescendo systolic murmur.",
        },
        "Peripheral Artery Disease (PAD)": {
            "symptoms": ["claudication", "leg pain", "muscle weakness", "cramps"],
            "differentiating_factors": "Leg pain that occurs with exercise and is relieved by rest (claudication). Diminished or absent peripheral pulses and cool extremities are key signs.",
        },
        "Venous Insufficiency": {
            "symptoms": ["leg swelling", "dependent edema", "skin discoloration", "ulceration"],
            "differentiating_factors": "Improper functioning of leg veins. Causes leg swelling that worsens during the day and improves with elevation. Skin changes are common.",
        },
        "Deep Vein Thrombosis (DVT)": {
            "symptoms": ["leg swelling", "leg pain", "tenderness", "erythema"],
            "differentiating_factors": "A blood clot in a deep vein, usually in the leg. Swelling and pain are unilateral. Homan's sign (pain on dorsiflexion of the foot) is a classic but unreliable sign.",
        },
        "Cellulitis": {
            "symptoms": ["erythema", "swelling", "tenderness", "fever"],
            "differentiating_factors": "A bacterial skin infection. The rash is erythematous, warm, and has poorly defined borders. A key differentiating factor from DVT is the presence of fever.",
        },
        "Gastric Ulcer": {
            "symptoms": ["abdominal pain", "nausea", "indigestion", "melena"],
            "differentiating_factors": "Epigastric pain that is worsened by food. Can lead to bleeding, presenting as melena or hematemesis.",
        },
        "Duodenal Ulcer": {
            "symptoms": ["abdominal pain", "indigestion", "heartburn"],
            "differentiating_factors": "Epigastric pain that is relieved by food. Often wakes the patient up at night. The pain can be gnawing or burning.",
        },
        "Hepatitis (Viral)": {
            "symptoms": ["fatigue", "nausea", "vomiting", "jaundice", "right upper quadrant pain"],
            "differentiating_factors": "Inflammation of the liver, caused by a virus. Labs show elevated liver enzymes. Differentiated by serology for the specific viral agent.",
        },
        "Gallstones (Cholelithiasis)": {
            "symptoms": ["abdominal pain", "nausea", "vomiting"],
            "differentiating_factors": "Pain is in the right upper quadrant and is colicky, often occurring after eating a fatty meal. Ultrasound is the diagnostic study of choice.",
        },
        "Cholangitis": {
            "symptoms": ["fever", "jaundice", "right upper quadrant pain"],
            "differentiating_factors": "Infection of the bile ducts. The classic Charcot's triad is fever, jaundice, and RUQ pain. Can be a life-threatening emergency.",
        },
        "Diverticulitis": {
            "symptoms": ["abdominal pain", "fever", "nausea", "change in bowel habits"],
            "differentiating_factors": "Pain is typically in the left lower quadrant and is associated with fever and elevated white blood cell count. Imaging (CT scan) is diagnostic.",
        },
        "Small Bowel Obstruction (SBO)": {
            "symptoms": ["abdominal pain", "vomiting", "bloating", "constipation"],
            "differentiating_factors": "Pain is colicky and intermittent. Vomiting is often bilious. Abdominal distention and absent bowel sounds are key exam findings. X-ray shows dilated loops of small bowel.",
        },
        "Large Bowel Obstruction (LBO)": {
            "symptoms": ["abdominal pain", "bloating", "constipation", "vomiting"],
            "differentiating_factors": "Symptoms are often more gradual than SBO. Vomiting is often feculent. Abdominal distention is more pronounced.",
        },
        "Anorectal Abscess": {
            "symptoms": ["anorectal pain", "swelling", "fever", "perirectal fullness"],
            "differentiating_factors": "Severe, throbbing pain in the anal area. Patients may have a palpable, tender mass. Often requires surgical drainage.",
        },
        "Hemorrhoids": {
            "symptoms": ["rectal bleeding", "itching", "pain", "prolapse"],
            "differentiating_factors": "Swollen veins in the rectum or anus. Bleeding is typically bright red and painless. Can be painful if thrombosed.",
        },
        "Anal Fissure": {
            "symptoms": ["anorectal pain", "rectal bleeding"],
            "differentiating_factors": "A small tear in the lining of the anal canal. Pain is sharp and severe, often described as 'tearing' or 'burning' during and after a bowel movement.",
        },
        "Esophagitis": {
            "symptoms": ["dysphagia", "odynophagia", "heartburn", "chest pain"],
            "differentiating_factors": "Inflammation of the esophagus. Painful swallowing is a key symptom. Often caused by reflux, infection, or medication side effects.",
        },
        "Barrett's Esophagus": {
            "symptoms": ["heartburn", "dysphagia"],
            "differentiating_factors": "A complication of chronic GERD where the esophageal lining changes. Often asymptomatic but is a precursor to esophageal cancer.",
        },
        "Achalasia": {
            "symptoms": ["dysphagia", "regurgitation", "weight loss"],
            "differentiating_factors": "A motility disorder of the esophagus. Patients have difficulty swallowing both solids and liquids. Barium swallow shows a 'bird's beak' appearance.",
        },
        "Celiac Disease": {
            "symptoms": ["diarrhea", "abdominal pain", "bloating", "weight loss", "fatigue"],
            "differentiating_factors": "An autoimmune reaction to gluten. Symptoms improve dramatically on a gluten-free diet. Can lead to malabsorption.",
        },
        "Lactose Intolerance": {
            "symptoms": ["diarrhea", "abdominal pain", "bloating", "flatulence"],
            "differentiating_factors": "Symptoms occur after consuming dairy products. The gold standard for diagnosis is a lactose tolerance test or hydrogen breath test.",
        },
        "Diabetic Ketoacidosis (DKA)": {
            "symptoms": ["excessive thirst", "frequent urination", "nausea", "vomiting", "abdominal pain", "fruity breath"],
            "differentiating_factors": "A serious complication of diabetes, often in Type 1. Characterized by hyperglycemia, metabolic acidosis, and ketonemia. Fruity breath is a classic sign.",
        },
        "Hypoglycemia": {
            "symptoms": ["dizziness", "lightheadedness", "shakiness", "sweating", "confusion", "slurred speech", "syncope"],
            "differentiating_factors": "Low blood sugar. Often in diabetic patients. Symptoms improve rapidly with the administration of glucose.",
        },
        "Hyperosmolar Hyperglycemic State (HHS)": {
            "symptoms": ["excessive thirst", "frequent urination", "confusion", "weakness", "lethargy"],
            "differentiating_factors": "A serious complication of diabetes, often in Type 2. Characterized by severe hyperglycemia and dehydration. Less common than DKA and has a higher mortality rate.",
        },
        "Inflammatory Bowel Disease (IBD)": {
            "symptoms": ["abdominal pain", "diarrhea", "blood in stool", "fever", "weight loss", "fatigue"],
            "differentiating_factors": "A group of conditions, primarily Crohn's disease and ulcerative colitis, characterized by chronic inflammation of the GI tract. Differentiated by location and type of inflammation.",
        },
        "Rheumatic Fever": {
            "symptoms": ["joint pain", "fever", "fatigue", "chorea", "rash", "carditis"],
            "differentiating_factors": "A delayed complication of a strep throat infection. Diagnosis is based on the Jones criteria, which include carditis, polyarthritis, chorea, erythema marginatum, and subcutaneous nodules.",
        },
        "Cystic Fibrosis": {
            "symptoms": ["persistent cough", "sputum production", "fatigue", "weight loss", "steatorrhea"],
            "differentiating_factors": "A genetic disorder affecting the lungs and digestive system. Characterized by thick, sticky mucus production. Sweat chloride test is the diagnostic gold standard.",
        },
        "Pneumothorax": {
            "symptoms": ["sudden chest pain", "shortness of breath", "tachypnea"],
            "differentiating_factors": "Sudden onset of dyspnea and sharp, pleuritic chest pain. Diagnosis is confirmed by a chest X-ray showing a collapsed lung. Can be spontaneous or traumatic.",
        },
        "Pericardial Tamponade": {
            "symptoms": ["shortness of breath", "chest pain", "hypotension", "muffled heart sounds"],
            "differentiating_factors": "A life-threatening condition where fluid accumulates in the pericardial sac, compressing the heart. Beck's triad of hypotension, JVD, and muffled heart sounds is classic.",
        },
        "Mitral Stenosis": {
            "symptoms": ["dyspnea", "fatigue", "heart palpitations", "hemoptysis"],
            "differentiating_factors": "Narrowing of the mitral valve. Often a late complication of rheumatic fever. Leads to a classic 'opening snap' and a diastolic rumble on auscultation.",
        },
        "Aortic Stenosis": {
            "symptoms": ["syncope", "angina", "dyspnea", "heart murmur"],
            "differentiating_factors": "Narrowing of the aortic valve. Classic triad of syncope, angina, and dyspnea. Associated with a crescendo-decrescendo systolic murmur.",
        },
        "Tricuspid Regurgitation": {
            "symptoms": ["peripheral edema", "ascites", "jugular venous distention"],
            "differentiating_factors": "Incomplete closure of the tricuspid valve. Leads to right-sided heart failure symptoms. Often secondary to pulmonary hypertension or left-sided heart failure.",
        },
        "Pyelonephritis": {
            "symptoms": ["flank pain", "fever", "nausea", "vomiting", "dysuria"],
            "differentiating_factors": "A kidney infection. Symptoms include high fever, CVA tenderness, and dysuria. Often a progression from an untreated UTI.",
        },
        "Urinary Tract Infection (UTI)": {
            "symptoms": ["dysuria", "frequent urination", "urinary urgency", "pelvic pain"],
            "differentiating_factors": "Infection of the bladder or urethra. Symptoms are localized to the urinary tract. Often treated with a short course of antibiotics.",
        },
        "Benign Prostatic Hyperplasia (BPH)": {
            "symptoms": ["urinary hesitancy", "frequent urination", "nocturia", "weak stream"],
            "differentiating_factors": "Enlargement of the prostate gland in older men. Causes obstructive urinary symptoms.",
        },
        "Depersonalization/Derealization Disorder": {
            "symptoms": ["depersonalization", "derealization", "anxiety", "feeling detached"],
            "differentiating_factors": "Persistent or recurrent feelings of being detached from one's own body (depersonalization) or from one's surroundings (derealization).",
        },
        "Somatization Disorder": {
            "symptoms": ["multiple physical symptoms", "fatigue", "pain", "gastrointestinal symptoms"],
            "differentiating_factors": "Characterized by multiple, persistent physical symptoms without a clear medical explanation. Patients often seek care from many different doctors.",
        },
        "Conversion Disorder": {
            "symptoms": ["weakness", "paralysis", "seizures", "blindness", "sensory loss"],
            "differentiating_factors": "Presents with neurological symptoms (e.g., paralysis) that are incompatible with a known neurological or medical condition. Often a psychological cause.",
        },
        "Factitious Disorder (Munchausen Syndrome)": {
            "symptoms": ["unusual symptoms", "multiple hospital visits", "lying about symptoms"],
            "differentiating_factors": "Falsification of physical or psychological symptoms without an obvious external reward. The motivation is to assume the sick role.",
        },
        "Malingering": {
            "symptoms": ["fabricated symptoms"],
            "differentiating_factors": "Intentional production of false or grossly exaggerated physical or psychological symptoms motivated by external incentives, like financial gain or avoiding work.",
        },
        "Acute Coronary Syndrome (ACS)": {
            "symptoms": ["chest pain", "chest pressure", "radiating arm pain", "shortness of breath", "nausea"],
            "differentiating_factors": "A group of conditions that includes unstable angina and myocardial infarction. Differentiated by EKG changes and cardiac enzymes.",
        },
        "Congenital Heart Defects": {
            "symptoms": ["cyanosis", "dyspnea", "failure to thrive", "murmur"],
            "differentiating_factors": "Present in infants and children. Specific symptoms depend on the type of defect (e.g., Tetralogy of Fallot, VSD, ASD).",
        },
        "End-Stage Renal Disease (ESRD)": {
            "symptoms": ["fatigue", "weakness", "nausea", "uremic pruritus", "peripheral edema"],
            "differentiating_factors": "A chronic, irreversible state of kidney failure. Patients often require dialysis or a kidney transplant. Labs show significantly elevated BUN and creatinine.",
        },
        "Urolithiasis (Kidney Stones)": {
            "symptoms": ["flank pain", "hematuria", "nausea", "vomiting"],
            "differentiating_factors": "Severe, colicky pain radiating from the flank to the groin. Hematuria is common. Often associated with a history of dehydration.",
        },
        "Gastroesophageal Varices": {
            "symptoms": ["hematemesis", "melena", "fatigue", "abdominal pain"],
            "differentiating_factors": "Enlarged veins in the esophagus or stomach, often due to portal hypertension from cirrhosis. Bleeding is a medical emergency.",
        },
        "Small Bowel Obstruction (SBO)": {
            "symptoms": ["abdominal pain", "vomiting", "bloating", "constipation"],
            "differentiating_factors": "Pain is colicky and intermittent. Vomiting is often bilious. Abdominal distention and absent bowel sounds are key exam findings. X-ray shows dilated loops of small bowel.",
        },
        "Large Bowel Obstruction (LBO)": {
            "symptoms": ["abdominal pain", "bloating", "constipation", "vomiting"],
            "differentiating_factors": "Symptoms are often more gradual than SBO. Vomiting is often feculent. Abdominal distention is more pronounced.",
        },
        "Diverticulitis": {
            "symptoms": ["abdominal pain", "fever", "nausea", "change in bowel habits"],
            "differentiating_factors": "Pain is typically in the left lower quadrant and is associated with fever and elevated white blood cell count. Imaging (CT scan) is diagnostic.",
        },
        "Anorectal Abscess": {
            "symptoms": ["anorectal pain", "swelling", "fever", "perirectal fullness"],
            "differentiating_factors": "Severe, throbbing pain in the anal area. Patients may have a palpable, tender mass. Often requires surgical drainage.",
        },
        "Hemorrhoids": {
            "symptoms": ["rectal bleeding", "itching", "pain", "prolapse"],
            "differentiating_factors": "Swollen veins in the rectum or anus. Bleeding is typically bright red and painless. Can be painful if thrombosed.",
        },
        "Anal Fissure": {
            "symptoms": ["anorectal pain", "rectal bleeding"],
            "differentiating_factors": "A small tear in the lining of the anal canal. Pain is sharp and severe, often described as 'tearing' or 'burning' during and after a bowel movement.",
        },
        "Esophagitis": {
            "symptoms": ["dysphagia", "odynophagia", "heartburn", "chest pain"],
            "differentiating_factors": "Inflammation of the esophagus. Painful swallowing is a key symptom. Often caused by reflux, infection, or medication side effects.",
        },
        "Barrett's Esophagus": {
            "symptoms": ["heartburn", "dysphagia"],
            "differentiating_factors": "A complication of chronic GERD where the esophageal lining changes. Often asymptomatic but is a precursor to esophageal cancer.",
        },
        "Achalasia": {
            "symptoms": ["dysphagia", "regurgitation", "weight loss"],
            "differentiating_factors": "A motility disorder of the esophagus. Patients have difficulty swallowing both solids and liquids. Barium swallow shows a 'bird's beak' appearance.",
        },
        "Scleroderma (Systemic Sclerosis)": {
            "symptoms": ["skin thickening", "Raynaud's phenomenon", "dysphagia", "shortness of breath", "joint pain"],
            "differentiating_factors": "An autoimmune disease affecting connective tissue. The CREST syndrome (Calcinosis, Raynaud's, Esophageal dysmotility, Sclerodactyly, Telangiectasias) is a key presentation.",
        },
        "Polymyositis/Dermatomyositis": {
            "symptoms": ["muscle weakness", "fatigue", "rash", "joint pain", "difficulty swallowing"],
            "differentiating_factors": "An inflammatory myopathy. Presents with symmetrical proximal muscle weakness. Dermatomyositis also includes characteristic rashes (Heliotrope rash, Gottron's papules).",
        },
        "Osteomyelitis": {
            "symptoms": ["fever", "localized pain", "swelling", "tenderness"],
            "differentiating_factors": "Infection of the bone. Pain is often severe and unremitting. Diagnosis requires imaging (MRI) and a positive culture.",
        },
        "Spondylolisthesis": {
            "symptoms": ["low back pain", "radiculopathy"],
            "differentiating_factors": "Forward slip of one vertebra over another. Causes low back pain that worsens with activity. Can cause nerve impingement and radiculopathy.",
        },
        "Sciatica": {
            "symptoms": ["radiculopathy", "lower back pain", "leg pain", "numbness"],
            "differentiating_factors": "Pain that radiates along the path of the sciatic nerve. Often caused by a herniated disc or spinal stenosis. The pain is usually unilateral.",
        },
        "Spinal Stenosis": {
            "symptoms": ["back pain", "leg pain", "numbness", "weakness"],
            "differentiating_factors": "Narrowing of the spinal canal. Causes neurogenic claudication, where leg pain occurs with standing/walking and is relieved by sitting or leaning forward.",
        },
        "Sjögren's Syndrome": {
            "symptoms": ["dry mouth", "dry eyes", "fatigue", "joint pain"],
            "differentiating_factors": "An autoimmune disorder affecting exocrine glands. Classic symptoms are dry mouth (xerostomia) and dry eyes (keratoconjunctivitis sicca).",
        },
        "Myasthenia Gravis": {
            "symptoms": ["muscle weakness", "ptosis", "diplopia", "dysphagia", "slurred speech"],
            "differentiating_factors": "An autoimmune disorder affecting neuromuscular junctions. Presents with fluctuating muscle weakness that worsens with activity and improves with rest.",
        },
        "Amyotrophic Lateral Sclerosis (ALS)": {
            "symptoms": ["muscle weakness", "slurred speech", "difficulty swallowing", "muscle twitching"],
            "differentiating_factors": "A progressive neurodegenerative disease affecting motor neurons. Presents with a combination of upper motor neuron signs (spasticity, hyperreflexia) and lower motor neuron signs (atrophy, fasciculations).",
        },
        "Huntington's Disease": {
            "symptoms": ["chorea", "dementia", "mood swings", "involuntary movements"],
            "differentiating_factors": "An inherited neurodegenerative disorder. The classic triad is motor dysfunction (chorea), cognitive decline, and psychiatric symptoms. Onset is typically in mid-adulthood.",
        },
        "Tourette Syndrome": {
            "symptoms": ["motor tics", "vocal tics", "involuntary movements", "behavioral problems"],
            "differentiating_factors": "Characterized by multiple motor tics and at least one vocal tic. Onset is typically in childhood. Tics are suppressible but often return with greater intensity.",
        },
        "Narcolepsy": {
            "symptoms": ["daytime sleepiness", "cataplexy", "sleep paralysis", "hypnagogic hallucinations"],
            "differentiating_factors": "A chronic neurological disorder affecting sleep-wake cycles. Cataplexy (sudden loss of muscle tone) triggered by strong emotions is a key feature.",
        },
        "Obstructive Sleep Apnea (OSA)": {
            "symptoms": ["snoring", "daytime sleepiness", "apnea", "fatigue"],
            "differentiating_factors": "Recurrent episodes of upper airway obstruction during sleep. The gold standard for diagnosis is a polysomnography (sleep study).",
        },
        "Restless Legs Syndrome (RLS)": {
            "symptoms": ["restless legs", "tingling", "unpleasant leg sensations", "insomnia"],
            "differentiating_factors": "An urge to move the legs, usually due to unpleasant sensations. Symptoms are worse at rest and are relieved by movement. Often worse in the evening/night.",
        },
        "Fibroadenoma": {
            "symptoms": ["breast lump", "mobile mass"],
            "differentiating_factors": "A benign breast tumor. Typically presents as a firm, rubbery, well-defined, and mobile mass. Common in young women.",
        },
        "Breast Cancer": {
            "symptoms": ["breast lump", "nipple discharge", "skin dimpling", "swollen lymph nodes"],
            "differentiating_factors": "A malignant breast tumor. Lumps are often hard, irregular, and non-mobile. Requires a biopsy for definitive diagnosis.",
        },
        "Prostate Cancer": {
            "symptoms": ["urinary hesitancy", "frequent urination", "back pain", "pelvic pain"],
            "differentiating_factors": "A malignant tumor of the prostate gland. Often asymptomatic initially. Can cause obstructive urinary symptoms and bone pain if it metastasizes.",
        },
        "Testicular Torsion": {
            "symptoms": ["testicular pain", "swelling"],
            "differentiating_factors": "A surgical emergency where the testicle twists. Presents with sudden onset of severe testicular pain and swelling. The cremasteric reflex is absent.",
        },
        "Epididymitis": {
            "symptoms": ["testicular pain", "swelling", "fever"],
            "differentiating_factors": "Inflammation of the epididymis. Pain is gradual in onset and is often relieved by lifting the testicle (Prehn's sign).",
        },
        "Renal Cell Carcinoma (RCC)": {
            "symptoms": ["hematuria", "flank pain", "abdominal mass", "weight loss"],
            "differentiating_factors": "A kidney cancer. The classic triad is hematuria, flank pain, and an abdominal mass. Often associated with paraneoplastic syndromes.",
        },
        "Polycystic Kidney Disease (PKD)": {
            "symptoms": ["flank pain", "hematuria", "hypertension", "renal cysts"],
            "differentiating_factors": "A genetic disorder causing multiple cysts to grow on the kidneys. Patients often have a family history and hypertension. Can progress to ESRD.",
        },
        "Urinary Incontinence": {
            "symptoms": ["urinary incontinence", "urinary urgency", "frequent urination"],
            "differentiating_factors": "Involuntary leakage of urine. Different types include stress, urge, and overflow incontinence. The cause and treatment vary.",
        },
        "Cystitis (Bladder Infection)": {
            "symptoms": ["dysuria", "frequent urination", "urinary urgency", "pelvic pain"],
            "differentiating_factors": "Inflammation of the bladder, often due to a bacterial infection. Symptoms are localized to the bladder. Often associated with a positive urine culture.",
        },
        "Urethritis": {
            "symptoms": ["dysuria", "urethral discharge", "itching"],
            "differentiating_factors": "Inflammation of the urethra. Often caused by sexually transmitted infections (STIs). Discharge can be purulent or watery.",
        },
        "Acute Tubular Necrosis (ATN)": {
            "symptoms": ["oliguria", "anuria", "fatigue", "nausea"],
            "differentiating_factors": "Damage to the kidney tubules, often caused by ischemia or toxins. A major cause of intrinsic acute kidney injury. Urine studies often show muddy brown casts.",
        },
        "Anemia": {
            "symptoms": ["fatigue", "weakness", "pale skin", "shortness of breath", "tachycardia"],
            "differentiating_factors": "A decrease in red blood cells or hemoglobin. Different types (e.g., iron-deficiency, B12 deficiency) have unique differentiating factors and lab findings.",
        },
        "Hemophilia": {
            "symptoms": ["easy bruising", "excessive bleeding", "joint pain", "hemarthrosis"],
            "differentiating_factors": "A genetic bleeding disorder. Patients have prolonged bleeding after injury or surgery. Hemarthrosis (bleeding into joints) is a classic finding.",
        },
        "Thrombocytopenia": {
            "symptoms": ["easy bruising", "petechiae", "purpura", "gingival bleeding", "epistaxis"],
            "differentiating_factors": "A low platelet count. Leads to easy bruising and bleeding from mucosal surfaces. Diagnosis is based on a CBC.",
        },
        "Leukemia": {
            "symptoms": ["fatigue", "fever", "night sweats", "easy bruising", "bleeding gums", "lymphadenopathy"],
            "differentiating_factors": "A cancer of the blood. Presents with constitutional symptoms, bleeding, and infections. Diagnosis is made with a bone marrow biopsy.",
        },
        "Lymphoma": {
            "symptoms": ["swollen lymph nodes", "night sweats", "fever", "weight loss", "fatigue"],
            "differentiating_factors": "A cancer of the lymphatic system. Presents with painless lymphadenopathy and 'B symptoms' (fever, night sweats, weight loss).",
        },
        "Multiple Myeloma": {
            "symptoms": ["bone pain", "fatigue", "anemia", "pathological fractures"],
            "differentiating_factors": "A cancer of plasma cells. The classic CRAB mnemonic stands for Hypercalcemia, Renal failure, Anemia, and Bone lesions. Pain is often in the back or ribs.",
        },
        "Sarcoidosis": {
            "symptoms": ["cough", "shortness of breath", "fatigue", "erythema nodosum", "swollen lymph nodes"],
            "differentiating_factors": "An inflammatory disease characterized by the formation of granulomas. Often affects the lungs, lymph nodes, and skin. Erythema nodosum is a key skin finding.",
        },
        "Systemic Lupus Erythematosus (SLE)": {
            "symptoms": ["malar rash", "joint pain", "fatigue", "fever", "photosensitivity"],
            "differentiating_factors": "A systemic autoimmune disease. The classic butterfly-shaped malar rash is a hallmark sign. ANA is almost always positive.",
        },
        "Sjogren's Syndrome": {
            "symptoms": ["dry eyes", "dry mouth", "fatigue", "joint pain"],
            "differentiating_factors": "An autoimmune disease affecting moisture-producing glands. The sicca symptoms (dryness) are key. Often associated with rheumatoid arthritis or lupus.",
        },
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
