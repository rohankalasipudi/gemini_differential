# main.py

# This file serves as the main entry point for the symptom analysis application.
# It uses data from 'symptoms.py' and 'treatments.py' to provide a
# differential diagnosis and corresponding treatment plan.

# Import the necessary modules.
from symptoms import analyze_symptoms, DATA
from treatments import TREATMENTS

def run_diagnosis():
    """
    Prompts the user for symptoms, runs the diagnostic analysis, and
    displays the results, including potential diseases and their treatments.
    """
    print("Welcome to the Differential Diagnosis & Treatment Companion!")
    print("-" * 50)
    print("Please enter a list of symptoms you are experiencing, separated by commas.")
    print("Example: fever, cough, joint pain, fatigue")
    print("You can also type 'list symptoms' to see all available symptoms.")
    print("-" * 50)

    user_input = input("Your symptoms: ").strip()

    if user_input.lower() == "list symptoms":
        print("\nAvailable Symptoms:")
        # Display the symptoms in a clean, multi-column format.
        symptoms = sorted(DATA["symptoms"])
        num_cols = 4
        col_width = max(len(s) for s in symptoms) + 2
        for i, symptom in enumerate(symptoms):
            print(f"{symptom:<{col_width}}", end="")
            if (i + 1) % num_cols == 0:
                print()
        print("\n" + "-" * 50)
        return

    # Process user symptoms and get the differential diagnosis.
    user_symptoms = [s.strip().lower() for s in user_input.split(',')]
    disease_scores = analyze_symptoms(user_symptoms)

    if not disease_scores:
        print("\nNo matching diseases found for the provided symptoms. Please try again.")
        return

    # Sort the diseases by score in descending order and display the top results.
    sorted_diseases = sorted(disease_scores.items(), key=lambda item: item[1]['score'], reverse=True)
    
    print("\n" + "=" * 50)
    print("Differential Diagnosis and Treatment Plan")
    print("=" * 50)
    
    for i, (disease, data) in enumerate(sorted_diseases):
        score = data['score']
        symptoms_matched = data['symptoms_matched']
        total_symptoms = data['total_symptoms']
        differentiating_factors = data['differentiating_factors']
        
        print(f"\n({i+1}) Potential Disease: {disease}")
        print(f"  - Match Score: {score} out of {total_symptoms} known symptoms.")
        print(f"  - Matched Symptoms: {', '.join(symptoms_matched)}")
        print(f"  - Differentiating Factors: {differentiating_factors}")

        # Check for and display the treatment plan for the disease.
        if disease in TREATMENTS:
            treatment_data = TREATMENTS[disease]
            print("\n  ** Treatment Plan **")
            print(f"  Goals: {', '.join(treatment_data['goals'])}")
            print(f"  First-Line Therapy: {', '.join(treatment_data['first_line'])}")
            print(f"  Second-Line Therapy: {', '.join(treatment_data['second_line'])}")
            print(f"  Supportive Care: {', '.join(treatment_data['supportive_care'])}")
        else:
            print("\n  - Treatment information not available for this disease.")
        
        print("\n" + "-" * 50)

if __name__ == "__main__":
    run_diagnosis()

