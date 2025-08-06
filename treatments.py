"""
treatments.py

This module contains a dictionary of medical treatment protocols for all
diseases listed in symptoms.py. It is intended for educational purposes
and to be used as a data source for a separate application, such as a
differential diagnosis tool.

The data is structured as follows:
- The top-level dictionary `TREATMENTS` has disease names as keys.
- Each disease is a nested dictionary with keys for different aspects of
  treatment, such as 'goals', 'first_line', 'second_line', and
  'supportive_care'.
- The values for these keys are lists of strings, making the information
  easy to access and display.
"""

TREATMENTS = {
    "Influenza (Flu)": {
        "goals": [
            "Reduce the severity and duration of symptoms.",
            "Prevent complications like pneumonia.",
            "Limit spread of the virus."
        ],
        "first_line": [
            "Supportive Care: Rest, hydration, and fever/pain relievers (e.g., acetaminophen, NSAIDs).",
            "Antivirals (e.g., oseltamivir, zanamivir) if initiated within 48 hours of symptom onset."
        ],
        "second_line": [
            "For severe cases or high-risk patients: Inpatient care, oxygen support, and IV fluids.",
            "Prevention: Annual flu vaccination."
        ],
        "supportive_care": [
            "Patient education on infection control (hand washing, covering coughs).",
            "Symptom management."
        ]
    },
    "COVID-19": {
        "goals": [
            "Reduce symptom severity and duration.",
            "Prevent progression to severe disease and hospitalization.",
            "Manage long-term symptoms ('long COVID')."
        ],
        "first_line": [
            "Supportive Care: Rest, hydration, and fever/pain relievers.",
            "Mild to moderate cases (outpatient): Oral antivirals (e.g., nirmatrelvir/ritonavir) for high-risk patients.",
            "Severe cases (inpatient): Remdesivir, dexamethasone, and supportive care (e.g., oxygen, mechanical ventilation)."
        ],
        "second_line": [
            "Immunomodulatory therapy (e.g., tocilizumab) for severe cases with hyperinflammation."
        ],
        "supportive_care": [
            "Monitoring for oxygen saturation.",
            "Pulmonary rehabilitation for long COVID.",
            "Prevention: Vaccination and mask-wearing in high-risk settings."
        ]
    },
    "Bacterial Meningitis": {
        "goals": [
            "Eradicate the causative bacteria.",
            "Reduce inflammation and prevent brain damage.",
            "Prevent complications like hearing loss or hydrocephalus."
        ],
        "first_line": [
            "Empiric IV Antibiotics (e.g., ceftriaxone or cefotaxime, vancomycin) started immediately after lumbar puncture or blood cultures.",
            "Corticosteroids (e.g., dexamethasone) to reduce inflammation, especially for S. pneumoniae."
        ],
        "second_line": [
            "Tailor antibiotics based on culture and sensitivity results."
        ],
        "supportive_care": [
            "Strict bed rest.",
            "IV fluids for hydration.",
            "Management of increased intracranial pressure.",
            "Prevention: Vaccination (e.g., Meningococcal, Hib, Pneumococcal vaccines)."
        ]
    },
    "Anxiety/Panic Attack": {
        "goals": [
            "Rapidly terminate an acute panic attack.",
            "Reduce the frequency and intensity of future attacks.",
            "Improve coping mechanisms and quality of life."
        ],
        "first_line": [
            "Acute Attack: Reassurance, deep breathing exercises, and for severe cases, short-acting benzodiazepines (e.g., lorazepam).",
            "Long-term: Selective Serotonin Reuptake Inhibitors (SSRIs) (e.g., sertraline, escitalopram) or Serotonin-Norepinephrine Reuptake Inhibitors (SNRIs).",
            "Cognitive-Behavioral Therapy (CBT) is highly effective."
        ],
        "second_line": [
            "Other antidepressants (e.g., tricyclic antidepressants).",
            "Other anxiolytics (e.g., buspirone).",
            "Beta-blockers (e.g., propranolol) for physical symptoms like palpitations."
        ],
        "supportive_care": [
            "Stress management techniques.",
            "Regular exercise.",
            "Avoiding stimulants like caffeine."
        ]
    },
    "Cirrhosis": {
        "goals": [
            "Treat the underlying cause (e.g., hepatitis, alcohol).",
            "Manage complications of portal hypertension (e.g., ascites, varices).",
            "Prevent further liver damage."
        ],
        "first_line": [
            "Dietary changes: Low sodium diet for ascites.",
            "Diuretics (e.g., spironolactone and furosemide) for ascites.",
            "Endoscopic variceal ligation or beta-blockers (e.g., propranolol) to prevent variceal bleeding."
        ],
        "second_line": [
            "Paracentesis for refractory ascites.",
            "Transjugular Intrahepatic Portosystemic Shunt (TIPS) for refractory complications.",
            "Liver transplantation for end-stage liver disease."
        ],
        "supportive_care": [
            "Abstinence from alcohol.",
            "Screening for hepatocellular carcinoma.",
            "Lactulose for hepatic encephalopathy."
        ]
    },
    "Pneumonia": {
        "goals": [
            "Eradicate the causative pathogen.",
            "Alleviate symptoms (cough, fever, dyspnea).",
            "Prevent complications (e.g., pleural effusion, sepsis)."
        ],
        "first_line": [
            "Outpatient: Macrolide (e.g., azithromycin) or Doxycycline.",
            "Inpatient: Beta-lactam (e.g., ceftriaxone) plus a macrolide or a respiratory fluoroquinolone.",
            "Hospitalized patients with risk factors for MRSA or Pseudomonas should receive additional coverage."
        ],
        "second_line": [
            "Treatment for specific pathogens based on culture and sensitivity results."
        ],
        "supportive_care": [
            "Antipyretics/analgesics (e.g., acetaminophen).",
            "Hydration.",
            "Oxygen therapy if needed for hypoxemia."
        ]
    },
    "Myocardial Infarction (MI)": {
        "goals": [
            "Re-establish coronary blood flow (reperfusion) as quickly as possible.",
            "Limit infarct size.",
            "Prevent life-threatening arrhythmias.",
            "Reduce myocardial workload."
        ],
        "first_line": [
            "Immediate Actions: MONA (Morphine, Oxygen, Nitroglycerin, Aspirin).",
            "Reperfusion Therapy (ASAP): Primary Percutaneous Coronary Intervention (PCI) is preferred. Fibrinolytic therapy if PCI is not available.",
            "Beta-blockers and ACE inhibitors (started early unless contraindicated)."
        ],
        "second_line": [
            "Long-term medical management with ACE inhibitors, ARBs, beta-blockers, statins, and dual antiplatelet therapy."
        ],
        "supportive_care": [
            "Telemetry monitoring for arrhythmias.",
            "Aggressive risk factor modification and cardiac rehabilitation."
        ]
    },
    "Congestive Heart Failure (CHF)": {
        "goals": [
            "Improve symptoms and quality of life.",
            "Slow disease progression and reduce hospitalizations.",
            "Reduce mortality."
        ],
        "first_line": [
            "Diuretics (e.g., furosemide) for symptom relief (edema).",
            "ACE inhibitors/ARBs.",
            "Beta-blockers (e.g., metoprolol, carvedilol).",
            "Aldosterone antagonists (e.g., spironolactone)."
        ],
        "second_line": [
            "SGLT2 inhibitors (e.g., dapagliflozin) for patients with reduced ejection fraction.",
            "Angiotensin receptor-neprilysin inhibitors (ARNIs) (e.g., sacubitril/valsartan) as a replacement for ACEi/ARB.",
            "Cardiac resynchronization therapy (CRT) or Implantable cardioverter-defibrillator (ICD) for selected patients."
        ],
        "supportive_care": [
            "Dietary sodium restriction.",
            "Fluid restriction.",
            "Patient education and adherence counseling."
        ]
    },
    "Pulmonary Embolism (PE)": {
        "goals": [
            "Prevent further clot formation.",
            "Dissolve or stabilize existing clots.",
            "Prevent recurrence."
        ],
        "first_line": [
            "Anticoagulation: Low-molecular-weight heparin or unfractionated heparin, followed by oral anticoagulants (e.g., warfarin, DOACs).",
            "Thrombolytic therapy for massive PE with hemodynamic instability."
        ],
        "second_line": [
            "Surgical embolectomy or catheter-directed therapy for selected patients.",
            "Inferior Vena Cava (IVC) filter for patients with contraindications to anticoagulation."
        ],
        "supportive_care": [
            "Oxygen therapy.",
            "Pain management.",
            "Early mobilization to prevent further DVT/PE."
        ]
    },
    "Appendicitis": {
        "goals": [
            "Remove the inflamed appendix.",
            "Prevent rupture and peritonitis."
        ],
        "first_line": [
            "Surgical appendectomy (laparoscopic is preferred)."
        ],
        "second_line": [
            "Non-operative management with antibiotics for uncomplicated cases (e.g., phlegmon or abscess) is an option, but surgery is the definitive treatment."
        ],
        "supportive_care": [
            "Pre-operative IV fluids and broad-spectrum antibiotics.",
            "Pain management."
        ]
    },
    "Cholecystitis": {
        "goals": [
            "Relieve symptoms.",
            "Prevent complications (e.g., gangrene, perforation).",
            "Remove the inflamed gallbladder."
        ],
        "first_line": [
            "Supportive Care: NPO, IV fluids, and pain control.",
            "Antibiotics.",
            "Surgical cholecystectomy, typically within 24-72 hours."
        ],
        "second_line": [
            "Percutaneous cholecystostomy for patients who are too ill for surgery.",
            "Ursodeoxycholic acid for dissolution of small gallstones (not for acute cholecystitis)."
        ],
        "supportive_care": [
            "Pain management with NSAIDs or opioids.",
            "Post-operative care."
        ]
    },
    "Pancreatitis": {
        "goals": [
            "Provide supportive care (mainstay of treatment).",
            "Relieve pain.",
            "Treat underlying cause.",
            "Prevent complications."
        ],
        "first_line": [
            "Aggressive IV fluid resuscitation with crystalloids (e.g., Lactated Ringer's).",
            "Analgesia (e.g., opioids).",
            "Nutritional support (start with oral feedings if tolerated, otherwise consider enteral nutrition)."
        ],
        "second_line": [
            "For gallstone pancreatitis: Endoscopic retrograde cholangiopancreatography (ERCP) or cholecystectomy.",
            "For infected necrosis: Antibiotics and consideration for drainage or debridement."
        ],
        "supportive_care": [
            "Identify and treat the cause (e.g., cholecystectomy for gallstone pancreatitis, cessation of alcohol)."
        ]
    },
    "Chronic Kidney Disease (CKD)": {
        "goals": [
            "Slow the progression of kidney disease.",
            "Manage complications.",
            "Prepare for renal replacement therapy if needed."
        ],
        "first_line": [
            "Blood pressure control (often with ACE inhibitors or ARBs).",
            "Glycemic control for diabetic patients.",
            "Dietary protein restriction.",
            "Management of anemia (e.g., erythropoiesis-stimulating agents) and mineral bone disease (e.g., phosphate binders)."
        ],
        "second_line": [
            "Dialysis (hemodialysis or peritoneal dialysis).",
            "Kidney transplantation."
        ],
        "supportive_care": [
            "Treating underlying cause.",
            "Patient education on medication and dietary adherence."
        ]
    },
    "Hypothyroidism": {
        "goals": [
            "Restore normal thyroid hormone levels.",
            "Alleviate symptoms of hypothyroidism."
        ],
        "first_line": [
            "Thyroid hormone replacement therapy with synthetic levothyroxine.",
            "Titrate dose based on TSH levels."
        ],
        "second_line": [
            "For myxedema coma (severe hypothyroidism): IV thyroid hormone and supportive care."
        ],
        "supportive_care": [
            "Regular monitoring of TSH levels every 6-8 weeks until stable, then annually.",
            "Patient education on taking medication on an empty stomach."
        ]
    },
    "Hyperthyroidism (Graves' Disease)": {
        "goals": [
            "Reduce thyroid hormone production.",
            "Treat underlying autoimmune process (Graves' disease).",
            "Manage symptoms."
        ],
        "first_line": [
            "Beta-blockers (e.g., propranolol) for symptom control (e.g., tremors, palpitations).",
            "Antithyroid medications (e.g., methimazole or propylthiouracil)."
        ],
        "second_line": [
            "Radioactive iodine ablation.",
            "Surgical thyroidectomy."
        ],
        "supportive_care": [
            "For thyroid storm: Aggressive supportive care, high-dose antithyroid meds, beta-blockers, and corticosteroids."
        ]
    },
    "Parkinson's Disease": {
        "goals": [
            "Manage motor symptoms (tremor, rigidity, bradykinesia).",
            "Improve quality of life and functional independence.",
            "Manage non-motor symptoms (e.g., depression, cognitive changes)."
        ],
        "first_line": [
            "Levodopa/carbidopa (the most effective drug for motor symptoms).",
            "Dopamine agonists (e.g., pramipexole, ropinirole), especially in younger patients.",
            "MAO-B inhibitors (e.g., selegiline) as monotherapy or adjuncts."
        ],
        "second_line": [
            "COMT inhibitors (e.g., entacapone) to extend the effect of levodopa.",
            "Amantadine for dyskinesia.",
            "Deep Brain Stimulation (DBS) for advanced cases."
        ],
        "supportive_care": [
            "Physical therapy, occupational therapy, and speech therapy.",
            "Patient and family education."
        ]
    },
    "Multiple Sclerosis (MS)": {
        "goals": [
            "Treat acute relapses.",
            "Reduce the frequency and severity of relapses.",
            "Slow disease progression and disability."
        ],
        "first_line": [
            "Acute relapse: High-dose corticosteroids (e.g., IV methylprednisolone).",
            "Disease-Modifying Therapies (DMTs) for relapsing-remitting MS: interferon beta, glatiramer acetate, or newer oral agents (e.g., fingolimod, teriflunomide)."
        ],
        "second_line": [
            "Monoclonal antibodies (e.g., natalizumab, ocrelizumab) for more aggressive disease."
        ],
        "supportive_care": [
            "Symptom management (e.g., baclofen for spasticity, amantadine for fatigue).",
            "Physical therapy.",
            "Treatment of bladder dysfunction."
        ]
    },
    "Lupus (Systemic Lupus Erythematosus)": {
        "goals": [
            "Suppress inflammation and autoimmune activity.",
            "Prevent organ damage.",
            "Manage symptoms and improve quality of life."
        ],
        "first_line": [
            "Mild disease: NSAIDs for musculoskeletal pain, hydroxychloroquine for skin and joint symptoms.",
            "Moderate to severe disease: Corticosteroids (e.g., prednisone).",
            "Immunosuppressants (e.g., azathioprine, mycophenolate mofetil)."
        ],
        "second_line": [
            "Biologics (e.g., belimumab) for severe disease refractory to other treatments.",
            "Rituximab for specific manifestations."
        ],
        "supportive_care": [
            "Sun protection.",
            "Patient education and support.",
            "Monitoring for flares and organ involvement."
        ]
    },
    "Rheumatoid Arthritis (RA)": {
        "goals": [
            "Reduce joint pain and inflammation.",
            "Prevent joint destruction and deformity.",
            "Achieve and maintain disease remission."
        ],
        "first_line": [
            "Disease-Modifying Antirheumatic Drugs (DMARDs): Methotrexate is the gold standard.",
            "NSAIDs for symptom control (bridge therapy).",
            "Short course of glucocorticoids for symptom flares."
        ],
        "second_line": [
            "Biologic DMARDs (e.g., TNF inhibitors like infliximab, etanercept) for patients who fail conventional DMARDs."
        ],
        "supportive_care": [
            "Physical therapy and occupational therapy.",
            "Regular monitoring for drug toxicities."
        ]
    },
    "Osteoarthritis (OA)": {
        "goals": [
            "Reduce pain.",
            "Maintain or improve joint function.",
            "Improve quality of life."
        ],
        "first_line": [
            "Non-pharmacologic: Exercise (low-impact), weight management, physical therapy.",
            "Pharmacologic: Topical NSAIDs, oral NSAIDs (use with caution due to side effects), acetaminophen."
        ],
        "second_line": [
            "Intra-articular corticosteroid injections.",
            "Joint replacement surgery for severe, end-stage disease."
        ],
        "supportive_care": [
            "Heat/cold therapy.",
            "Assistive devices (e.g., cane)."
        ]
    },
    "Sepsis": {
        "goals": [
            "Identify and treat the source of infection.",
            "Restore tissue perfusion and oxygenation.",
            "Prevent organ damage."
        ],
        "first_line": [
            "Immediate broad-spectrum IV antibiotics.",
            "IV fluid resuscitation (e.g., 30 mL/kg crystalloids within the first 3 hours).",
            "Vasopressors (e.g., norepinephrine) if hypotension persists after fluids.",
            "Source control (e.g., draining an abscess)."
        ],
        "second_line": [
            "Tailor antibiotics based on culture results.",
            "Adrenal support with corticosteroids for septic shock."
        ],
        "supportive_care": [
            "Oxygen support, mechanical ventilation if needed.",
            "Blood glucose control.",
            "Monitoring for organ dysfunction."
        ]
    },
    "Depression": {
        "goals": [
            "Achieve symptom remission.",
            "Restore social and occupational function.",
            "Prevent recurrence."
        ],
        "first_line": [
            "Pharmacotherapy: SSRIs (e.g., fluoxetine, sertraline) are the most common first-line.",
            "Psychotherapy: Cognitive-Behavioral Therapy (CBT), Interpersonal Therapy (IPT)."
        ],
        "second_line": [
            "Switching to a different class of antidepressant (e.g., SNRIs, bupropion, TCAs).",
            "Augmentation strategies (e.g., adding an atypical antipsychotic)."
        ],
        "supportive_care": [
            "Regular follow-up and monitoring for suicidal ideation.",
            "Lifestyle changes: exercise, healthy diet, sleep hygiene."
        ]
    },
    "Migraine": {
        "goals": [
            "Treat acute attacks.",
            "Prevent future attacks."
        ],
        "first_line": [
            "Acute Attack: Triptans (e.g., sumatriptan), NSAIDs (e.g., ibuprofen), antiemetics (e.g., metoclopramide).",
            "Prevention (for frequent attacks): Beta-blockers (e.g., propranolol), antiepileptics (e.g., topiramate, valproate), or CGRP antagonists."
        ],
        "second_line": [
            "Botox injections for chronic migraines.",
            "CGRP antagonists for refractory cases."
        ],
        "supportive_care": [
            "Avoiding triggers (e.g., certain foods, stress).",
            "Maintaining a regular sleep schedule."
        ]
    },
    "Stroke": {
        "goals": [
            "Re-establish blood flow to the brain as quickly as possible.",
            "Prevent secondary brain injury.",
            "Prevent recurrence."
        ],
        "first_line": [
            "Acute Ischemic Stroke: IV alteplase (tPA) within 3-4.5 hours of symptom onset.",
            "Mechanical thrombectomy for large vessel occlusions within 6-24 hours."
        ],
        "second_line": [
            "Antiplatelet therapy (e.g., aspirin) for secondary prevention.",
            "Anticoagulation for cardioembolic stroke (e.g., AFib)."
        ],
        "supportive_care": [
            "Maintain blood pressure control.",
            "Rehabilitation (physical, occupational, and speech therapy)."
        ]
    },
    "Type 1 Diabetes": {
        "goals": [
            "Achieve and maintain glycemic control.",
            "Prevent complications like DKA.",
            "Integrate insulin therapy with lifestyle."
        ],
        "first_line": [
            "Intensive insulin therapy: Basal-bolus regimen with long-acting insulin and rapid-acting insulin.",
            "Carbohydrate counting to match insulin doses to food intake."
        ],
        "second_line": [
            "Continuous Glucose Monitoring (CGM) systems.",
            "Insulin pump therapy."
        ],
        "supportive_care": [
            "Regular blood glucose monitoring.",
            "Diabetes education.",
            "Management of comorbidities."
        ]
    },
    "Cushing's Syndrome": {
        "goals": [
            "Normalize cortisol levels.",
            "Remove or shrink the underlying tumor.",
            "Manage symptoms and comorbidities."
        ],
        "first_line": [
            "Surgical removal of the pituitary adenoma (for Cushing's disease) or adrenal tumor.",
            "Medications to inhibit cortisol production (e.g., metyrapone, ketoconazole) as a bridge to surgery or for inoperable cases."
        ],
        "second_line": [
            "Radiation therapy for pituitary tumors.",
            "Bilateral adrenalectomy for refractory cases."
        ],
        "supportive_care": [
            "Gradual tapering of exogenous steroids if that is the cause.",
            "Management of hypertension and diabetes."
        ]
    },
    "Chronic Obstructive Pulmonary Disease (COPD)": {
        "goals": [
            "Relieve symptoms and improve exercise tolerance.",
            "Prevent and treat exacerbations.",
            "Slow disease progression."
        ],
        "first_line": [
            "Smoking cessation (the most important intervention).",
            "Bronchodilators: Short-acting beta-agonists (SABAs) and long-acting beta-agonists (LABAs) or long-acting muscarinic antagonists (LAMAs)."
        ],
        "second_line": [
            "Inhaled corticosteroids (ICS) for patients with frequent exacerbations.",
            "Combination inhalers (LABA/LAMA/ICS)."
        ],
        "supportive_care": [
            "Pulmonary rehabilitation.",
            "Oxygen therapy for hypoxemia.",
            "Vaccinations (flu, pneumococcal)."
        ]
    },
    "Asthma": {
        "goals": [
            "Control symptoms and prevent exacerbations.",
            "Maintain normal lung function.",
            "Minimize medication side effects."
        ],
        "first_line": [
            "Short-acting beta-agonists (SABAs) (e.g., albuterol) for quick relief.",
            "Inhaled corticosteroids (ICS) for long-term control.",
            "Controller medications are based on the severity of the asthma."
        ],
        "second_line": [
            "Adding a long-acting beta-agonist (LABA) to ICS.",
            "Leukotriene receptor antagonists (e.g., montelukast).",
            "Biologic agents for severe, refractory asthma."
        ],
        "supportive_care": [
            "Identifying and avoiding triggers (allergens, cold air).",
            "Asthma action plan."
        ]
    },
    "Gastroesophageal Reflux Disease (GERD)": {
        "goals": [
            "Alleviate symptoms (heartburn, regurgitation).",
            "Heal esophagitis.",
            "Prevent complications like Barrett's esophagus."
        ],
        "first_line": [
            "Lifestyle modifications: Weight loss, elevating the head of the bed, avoiding trigger foods.",
            "Pharmacotherapy: Proton Pump Inhibitors (PPIs) (e.g., omeprazole) or H2 blockers (e.g., famotidine)."
        ],
        "second_line": [
            "Surgery (e.g., Nissen fundoplication) for refractory cases or when there is a large hiatal hernia."
        ],
        "supportive_care": [
            "Antacids for immediate relief.",
            "Patient education on diet and lifestyle."
        ]
    },
    "Irritable Bowel Syndrome (IBS)": {
        "goals": [
            "Relieve abdominal pain and discomfort.",
            "Manage diarrhea or constipation.",
            "Improve quality of life."
        ],
        "first_line": [
            "Dietary changes (e.g., low FODMAP diet).",
            "Antispasmodics (e.g., dicyclomine) for abdominal pain.",
            "Fiber supplements for constipation, loperamide for diarrhea."
        ],
        "second_line": [
            "Antidepressants (SSRIs or TCAs) for pain and mood regulation.",
            "Specific IBS-targeted medications (e.g., rifaximin for bloating, lubiprostone for constipation)."
        ],
        "supportive_care": [
            "Stress management.",
            "Psychological therapies (e.g., CBT)."
        ]
    },
    "Ulcerative Colitis (UC)": {
        "goals": [
            "Induce and maintain remission.",
            "Prevent flares and complications.",
            "Avoid colectomy."
        ],
        "first_line": [
            "Aminosalicylates (5-ASA) (e.g., mesalamine) for mild to moderate disease.",
            "Corticosteroids (e.g., prednisone) to induce remission in moderate to severe flares.",
            "Immunomodulators (e.g., azathioprine, 6-MP) for maintenance therapy."
        ],
        "second_line": [
            "Biologic agents (e.g., infliximab, vedolizumab) for moderate to severe disease.",
            "Colectomy for refractory or complicated cases."
        ],
        "supportive_care": [
            "Nutritional support.",
            "Screening for colon cancer."
        ]
    },
    "Crohn's Disease": {
        "goals": [
            "Induce and maintain remission.",
            "Heal mucosal damage.",
            "Prevent complications (fistulas, strictures)."
        ],
        "first_line": [
            "Corticosteroids to induce remission.",
            "Immunomodulators for maintenance therapy.",
            "Antibiotics (e.g., metronidazole, ciprofloxacin) for perianal disease."
        ],
        "second_line": [
            "Biologic agents (e.g., infliximab, adalimumab) for moderate to severe disease.",
            "Surgery for strictures or fistulas."
        ],
        "supportive_care": [
            "Nutritional support.",
            "Smoking cessation."
        ]
    },
    "Schizophrenia": {
        "goals": [
            "Reduce or eliminate psychotic symptoms.",
            "Improve social and occupational function.",
            "Prevent relapse."
        ],
        "first_line": [
            "Second-generation antipsychotics (e.g., olanzapine, risperidone) are generally preferred due to fewer motor side effects.",
            "Psychosocial treatments: CBT, family therapy, social skills training."
        ],
        "second_line": [
            "Clozapine for treatment-resistant schizophrenia.",
            "Long-acting injectable antipsychotics for adherence issues."
        ],
        "supportive_care": [
            "Supportive housing.",
            "Vocational training."
        ]
    },
    "Bipolar Disorder": {
        "goals": [
            "Stabilize mood (treat mania and depression).",
            "Prevent recurrence of mood episodes.",
            "Improve function and quality of life."
        ],
        "first_line": [
            "Mood stabilizers: Lithium is a classic first-line treatment.",
            "Anticonvulsants (e.g., valproate, lamotrigine) as mood stabilizers.",
            "Atypical antipsychotics (e.g., quetiapine, aripiprazole) for acute mania."
        ],
        "second_line": [
            "Combinations of mood stabilizers and antipsychotics.",
            "Electroconvulsive Therapy (ECT) for severe or refractory episodes."
        ],
        "supportive_care": [
            "Psychoeducation and family therapy.",
            "Regular monitoring of blood levels for lithium and valproate."
        ]
    },
    "Eczema (Atopic Dermatitis)": {
        "goals": [
            "Control itching and inflammation.",
            "Repair the skin barrier.",
            "Prevent flares."
        ],
        "first_line": [
            "Moisturizers and emollients.",
            "Topical corticosteroids for flares.",
            "Avoiding triggers (e.g., harsh soaps, hot water)."
        ],
        "second_line": [
            "Topical calcineurin inhibitors (e.g., tacrolimus) for sensitive areas.",
            "Phototherapy.",
            "Systemic immunosuppressants for severe cases."
        ],
        "supportive_care": [
            "Wet wrap therapy for severe flares.",
            "Antihistamines for nighttime itching."
        ]
    },
    "Psoriasis": {
        "goals": [
            "Reduce plaque formation and inflammation.",
            "Control symptoms (itching, scaling).",
            "Improve quality of life."
        ],
        "first_line": [
            "Topical corticosteroids, vitamin D analogues, and retinoids for localized disease.",
            "Phototherapy for more widespread disease."
        ],
        "second_line": [
            "Systemic therapy (e.g., methotrexate, cyclosporine) for moderate to severe disease.",
            "Biologic agents (e.g., TNF-alpha inhibitors, IL-17 inhibitors) for severe cases."
        ],
        "supportive_care": [
            "Managing associated psoriatic arthritis.",
            "Psychological support."
        ]
    },
    "Peptic Ulcer Disease (PUD)": {
        "goals": [
            "Heal the ulcer.",
            "Eradicate Helicobacter pylori if present.",
            "Prevent recurrence and complications."
        ],
        "first_line": [
            "Eradication of H. pylori with triple therapy (e.g., PPI + clarithromycin + amoxicillin/metronidazole).",
            "PPIs for ulcer healing."
        ],
        "second_line": [
            "Switching to a different H. pylori eradication regimen if the first fails.",
            "Surgery for complicated cases (e.g., perforation, bleeding that can't be controlled endoscopically)."
        ],
        "supportive_care": [
            "Discontinuation of NSAIDs if they are the cause.",
            "Lifestyle modifications (avoiding alcohol, smoking)."
        ]
    },
    "Atrial Fibrillation (Afib)": {
        "goals": [
            "Prevent stroke (thromboembolism).",
            "Control ventricular rate.",
            "Restore sinus rhythm if appropriate."
        ],
        "first_line": [
            "Stroke prevention: Oral anticoagulation (e.g., warfarin, DOACs) based on CHA2DS2-VASc score.",
            "Rate control: Beta-blockers (e.g., metoprolol) or calcium channel blockers (e.g., diltiazem)."
        ],
        "second_line": [
            "Rhythm control: Antiarrhythmic drugs (e.g., amiodarone, flecainide).",
            "Catheter ablation for symptomatic Afib refractory to medication."
        ],
        "supportive_care": [
            "Patient education on medication adherence and signs of bleeding.",
            "Cardioversion for rapid restoration of sinus rhythm."
        ]
    },
    "Peripheral Artery Disease (PAD)": {
        "goals": [
            "Relieve symptoms (claudication).",
            "Improve walking ability.",
            "Prevent cardiovascular events (MI, stroke).",
            "Prevent limb loss."
        ],
        "first_line": [
            "Aggressive risk factor modification: Smoking cessation, blood pressure and lipid control.",
            "Exercise program (supervised exercise therapy).",
            "Pharmacotherapy: Aspirin and cilostazol (for claudication)."
        ],
        "second_line": [
            "Angioplasty or surgical bypass for severe symptoms or critical limb ischemia."
        ],
        "supportive_care": [
            "Foot care and inspection to prevent ulcers.",
            "Pain management."
        ]
    },
    "Acute Kidney Injury (AKI)": {
        "goals": [
            "Identify and treat the underlying cause.",
            "Manage fluid and electrolyte imbalances.",
            "Prevent further kidney damage."
        ],
        "first_line": [
            "Fluid resuscitation for pre-renal AKI.",
            "Discontinuation of nephrotoxic medications.",
            "Management of hyperkalemia and metabolic acidosis."
        ],
        "second_line": [
            "Renal replacement therapy (dialysis) if there are severe electrolyte abnormalities, fluid overload, or uremia."
        ],
        "supportive_care": [
            "Close monitoring of urine output, creatinine, and electrolytes.",
            "Nutritional support."
        ]
    },
    "Nephrotic Syndrome": {
        "goals": [
            "Reduce proteinuria.",
            "Manage edema and hyperlipidemia.",
            "Prevent complications (e.g., thromboembolism, infection)."
        ],
        "first_line": [
            "Treating the underlying cause (e.g., immunosuppressants for minimal change disease).",
            "Symptomatic management: Diuretics for edema, ACE inhibitors/ARBs for proteinuria.",
            "Statins for hyperlipidemia."
        ],
        "second_line": [
            "Immunosuppressive therapy for steroid-resistant cases.",
            "Anticoagulation for high-risk patients to prevent thromboembolism."
        ],
        "supportive_care": [
            "Dietary sodium and fat restriction.",
            "Monitoring for signs of infection."
        ]
    },
    "Major Depressive Disorder (MDD)": {
        "goals": [
            "Achieve symptom remission.",
            "Restore social and occupational function.",
            "Prevent recurrence."
        ],
        "first_line": [
            "Pharmacotherapy: SSRIs are the most common first-line.",
            "Psychotherapy: Cognitive-Behavioral Therapy (CBT)."
        ],
        "second_line": [
            "Switching to a different class of antidepressant (e.g., SNRIs, bupropion, TCAs).",
            "Augmentation strategies (e.g., adding an atypical antipsychotic)."
        ],
        "supportive_care": [
            "Regular follow-up and monitoring for suicidal ideation.",
            "Lifestyle changes: exercise, healthy diet, sleep hygiene."
        ]
    },
    "Acute Myocardial Pericarditis": {
        "goals": [
            "Reduce pain and inflammation.",
            "Identify and treat the cause.",
            "Prevent complications (e.g., cardiac tamponade)."
        ],
        "first_line": [
            "NSAIDs (e.g., high-dose ibuprofen) are the mainstay of therapy.",
            "Colchicine to reduce symptoms and prevent recurrence."
        ],
        "second_line": [
            "Corticosteroids for refractory cases or when NSAIDs are contraindicated.",
            "Treatment of the underlying cause (e.g., antibiotics for bacterial pericarditis)."
        ],
        "supportive_care": [
            "Monitoring for signs of tamponade.",
            "Avoiding intense physical activity until symptoms resolve."
        ]
    },
    "Acute Glomerulonephritis": {
        "goals": [
            "Reduce inflammation of the glomeruli.",
            "Manage complications (hypertension, edema).",
            "Treat the underlying cause."
        ],
        "first_line": [
            "Management of hypertension and edema (e.g., diuretics, antihypertensives).",
            "Treating the underlying infection (e.g., antibiotics for post-streptococcal GN)."
        ],
        "second_line": [
            "Corticosteroids or immunosuppressants for certain types of glomerulonephritis (e.g., IgA nephropathy, rapidly progressive GN)."
        ],
        "supportive_care": [
            "Dialysis for severe AKI.",
            "Dietary salt and fluid restriction."
        ]
    },
    "Nephritic Syndrome": {
        "goals": [
            "Reduce inflammation.",
            "Manage hypertension and fluid overload.",
            "Treat underlying cause."
        ],
        "first_line": [
            "Symptom management: Diuretics for edema, antihypertensives for high blood pressure.",
            "Treatment of the underlying cause (e.g., immunosuppressants for lupus nephritis)."
        ],
        "second_line": [
            "Dialysis for severe fluid overload or uremia."
        ],
        "supportive_care": [
            "Fluid and salt restriction."
        ]
    },
    "Bipolar I Disorder": {
        "goals": [
            "Treat acute manic episodes.",
            "Prevent future manic and depressive episodes.",
            "Stabilize mood."
        ],
        "first_line": [
            "Acute mania: Mood stabilizers (e.g., lithium, valproate) and/or atypical antipsychotics (e.g., risperidone, olanzapine).",
            "Maintenance: Mood stabilizers are key for long-term prevention."
        ],
        "second_line": [
            "Combination therapy for refractory cases.",
            "ECT for severe or life-threatening mania."
        ],
        "supportive_care": [
            "Psychotherapy and psychoeducation.",
            "Adherence monitoring."
        ]
    },
    "Obsessive-Compulsive Disorder (OCD)": {
        "goals": [
            "Reduce the frequency and intensity of obsessions and compulsions.",
            "Improve daily functioning.",
            "Improve quality of life."
        ],
        "first_line": [
            "Pharmacotherapy: SSRIs (often at higher doses than for depression).",
            "Psychotherapy: Exposure and Response Prevention (ERP) is the gold standard CBT technique for OCD."
        ],
        "second_line": [
            "Tricyclic antidepressants (e.g., clomipramine).",
            "Augmentation with an atypical antipsychotic for resistant cases."
        ],
        "supportive_care": [
            "Support groups.",
            "Stress management."
        ]
    },
    "Gout": {
        "goals": [
            "Treat acute flares.",
            "Prevent future flares.",
            "Lower uric acid levels."
        ],
        "first_line": [
            "Acute flare: NSAIDs (e.g., indomethacin), colchicine, or corticosteroids.",
            "Prevention: Allopurinol or febuxostat to lower uric acid levels."
        ],
        "second_line": [
            "Uricosuric agents (e.g., probenecid) for patients who underexcrete uric acid.",
            "Biologics (e.g., canakinumab) for refractory cases."
        ],
        "supportive_care": [
            "Dietary changes (avoiding red meat, organ meat, and alcohol).",
            "Hydration."
        ]
    },
    "Fibromyalgia": {
        "goals": [
            "Manage chronic pain.",
            "Improve sleep and fatigue.",
            "Improve quality of life and function."
        ],
        "first_line": [
            "Aerobic exercise and physical therapy.",
            "Pharmacotherapy: TCAs (e.g., amitriptyline) for sleep, SNRIs (e.g., duloxetine) for pain, and gabapentinoids (e.g., pregabalin)."
        ],
        "second_line": [
            "Referral to pain management specialists.",
            "Psychological therapy (e.g., CBT)."
        ],
        "supportive_care": [
            "Sleep hygiene.",
            "Stress reduction."
        ]
    },
    "Chronic Pain Syndrome": {
        "goals": [
            "Reduce pain intensity.",
            "Improve functional ability and quality of life.",
            "Address psychosocial factors (depression, anxiety)."
        ],
        "first_line": [
            "Multidisciplinary approach: Physical therapy, CBT, and patient education.",
            "Pharmacotherapy: NSAIDs, antidepressants (e.g., SNRIs, TCAs), or gabapentinoids."
        ],
        "second_line": [
            "Referral to a pain management clinic for interventional procedures or advanced therapies."
        ],
        "supportive_care": [
            "Mindfulness and relaxation techniques.",
            "Managing co-morbid depression and anxiety."
        ]
    },
    "Diabetic Ketoacidosis (DKA)": {
        "goals": [
            "Correct hyperglycemia and acidosis.",
            "Replenish fluid and electrolytes.",
            "Identify and treat the precipitating cause."
        ],
        "first_line": [
            "IV fluid resuscitation (e.g., normal saline).",
            "Insulin drip to lower glucose and stop ketogenesis.",
            "Potassium replacement as needed."
        ],
        "second_line": [
            "Transition to subcutaneous insulin once acidosis resolves and patient is stable."
        ],
        "supportive_care": [
            "Hourly monitoring of blood glucose, electrolytes, and anion gap.",
            "Monitoring for complications like cerebral edema."
        ]
    },
    "Inflammatory Bowel Disease (IBD)": {
        "goals": [
            "Induce and maintain remission.",
            "Prevent flares and complications.",
            "Improve quality of life."
        ],
        "first_line": [
            "Aminosalicylates (5-ASA) for mild UC.",
            "Corticosteroids for acute flares.",
            "Immunomodulators for maintenance."
        ],
        "second_line": [
            "Biologic agents (e.g., infliximab, adalimumab) for moderate to severe disease.",
            "Surgery for refractory cases (colectomy for UC, resection for Crohn's)."
        ],
        "supportive_care": [
            "Nutritional support.",
            "Regular screening for complications."
        ]
    },
    "Rheumatic Fever": {
        "goals": [
            "Treat the initial strep infection.",
            "Suppress inflammation to prevent cardiac damage.",
            "Prevent future episodes."
        ],
        "first_line": [
            "Antibiotics (e.g., penicillin) to eradicate Group A Strep.",
            "Anti-inflammatory agents: NSAIDs for arthritis, corticosteroids for severe carditis.",
            "Penicillin prophylaxis for secondary prevention."
        ],
        "second_line": [
            "Surgery for severe valvular heart disease."
        ],
        "supportive_care": [
            "Bed rest during the acute phase.",
            "Monitoring for signs of carditis."
        ]
    },
    "Atrial Flutter": {
        "goals": [
            "Control ventricular rate.",
            "Prevent stroke.",
            "Restore sinus rhythm."
        ],
        "first_line": [
            "Rate control: Beta-blockers or calcium channel blockers.",
            "Anticoagulation for stroke prevention based on CHA2DS2-VASc score.",
            "Cardioversion for symptomatic or unstable patients."
        ],
        "second_line": [
            "Catheter ablation is the definitive treatment.",
            "Antiarrhythmic drugs (e.g., dofetilide) for rhythm control."
        ],
        "supportive_care": [
            "Patient education and adherence counseling."
        ]
    },
    "Ventricular Tachycardia": {
        "goals": [
            "Terminate the acute arrhythmia.",
            "Identify and treat the underlying cause.",
            "Prevent sudden cardiac death."
        ],
        "first_line": [
            "Acute: Cardioversion for unstable VT. Antiarrhythmic drugs (e.g., amiodarone, lidocaine) for stable VT.",
            "Long-term: ICD placement for patients with structural heart disease or high risk of sudden cardiac death."
        ],
        "second_line": [
            "Catheter ablation for recurrent VT.",
            "Coronary revascularization for ischemic heart disease."
        ],
        "supportive_care": [
            "Addressing underlying cause (e.g., electrolyte imbalance, ischemia).",
            "Beta-blockers for long-term prevention."
        ]
    },
    "Gastritis": {
        "goals": [
            "Reduce stomach inflammation.",
            "Alleviate symptoms (pain, nausea).",
            "Address the underlying cause."
        ],
        "first_line": [
            "Pharmacotherapy: PPIs or H2 blockers.",
            "If H. pylori is the cause, treat with triple therapy."
        ],
        "second_line": [
            "Discontinuation of NSAIDs or alcohol if they are the cause."
        ],
        "supportive_care": [
            "Dietary modifications (avoiding spicy, acidic, or fatty foods).",
            "Small, frequent meals."
        ]
    },
    "Gastroenteritis": {
        "goals": [
            "Prevent dehydration.",
            "Provide symptomatic relief.",
            "Eradicate the pathogen if bacterial."
        ],
        "first_line": [
            "Supportive Care: Oral rehydration therapy is the cornerstone of treatment.",
            "Antiemetics (e.g., ondansetron) for vomiting."
        ],
        "second_line": [
            "Antibiotics for specific bacterial infections (e.g., Salmonella, Shigella) in severe cases or high-risk patients.",
            "IV fluids for severe dehydration."
        ],
        "supportive_care": [
            "Patient education on infection control.",
            "Gradual return to a normal diet."
        ]
    }
}

if __name__ == "__main__":
    # Example of how to access the data
    disease = "Rheumatoid Arthritis (RA)"
    if disease in TREATMENTS:
        print(f"Treatment Goals for {disease}:")
        for goal in TREATMENTS[disease]["goals"]:
            print(f"- {goal}")
    else:
        print(f"No treatment information found for {disease}.")

