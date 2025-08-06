# main.py

import symptoms

def main():
    """
    Main function to run the symptom analysis tool.
    """
    print("Welcome to the Medical Symptom Analyzer!")
    print("Please enter your symptoms, separated by commas (e.g., fever, cough, headache).")
    
    user_input = input("\nEnter your symptoms: ")
    
    # Split the input string into a list of symptoms
    user_symptoms = [s.strip() for s in user_input.split(',')]
    
    # Analyze the symptoms using the function from symptoms.py
    results = symptoms.analyze_symptoms(user_symptoms)
    
    # Sort the results by score in descending order
    sorted_results = sorted(results.items(), key=lambda item: item[1]['score'], reverse=True)
    
    print("\n--- Diagnostic Report ---")
    
    if not sorted_results:
        print("No matching diseases found for the symptoms provided.")
    else:
        for disease, data in sorted_results:
            match_percentage = (data['score'] / data['total_symptoms']) * 100
            print(f"\nPotential Disease: {disease}")
            print(f"  - Match Score: {data['score']} out of {data['total_symptoms']} symptoms matched ({match_percentage:.1f}%)")
            print(f"  - Symptoms Matched: {', '.join(data['symptoms_matched'])}")
            print(f"  - Differentiating Factors: {data['differentiating_factors']}")
            
    print("\n-------------------------")
    print("Disclaimer: This is an educational tool and not a substitute for professional medical advice.")

if __name__ == "__main__":
    main()
