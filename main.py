# main.py

import streamlit as st
import symptoms

def main():
    """
    Main function for the Streamlit symptom analysis tool.
    """
    # --- UI Elements ---
    st.title("Medical Symptom Analyzer")
    st.write("This is an educational tool. It is not a substitute for professional medical advice.")
    st.write("Please enter your symptoms below, separated by commas (e.g., fever, cough, headache).")
    
    # Text input field for user symptoms
    user_input = st.text_input("Enter symptoms:")
    
    # A button to trigger the analysis
    if st.button("Analyze Symptoms"):
        if not user_input:
            st.warning("Please enter at least one symptom.")
            return

        # Split the input string into a list of symptoms
        user_symptoms = [s.strip() for s in user_input.split(',')]
        
        # Analyze the symptoms using the function from symptoms.py
        results = symptoms.analyze_symptoms(user_symptoms)
        
        # Sort the results by score in descending order
        sorted_results = sorted(results.items(), key=lambda item: item[1]['score'], reverse=True)
        
        # --- Display the Diagnostic Report ---
        st.subheader("Diagnostic Report")
        
        if not sorted_results:
            st.info("No matching diseases found for the symptoms provided.")
        else:
            for disease, data in sorted_results:
                match_percentage = (data['score'] / data['total_symptoms']) * 100
                
                # Use markdown to format the output for better readability
                st.markdown(f"**Potential Disease:** `{disease}`")
                st.markdown(f"**Match Score:** `{data['score']} out of {data['total_symptoms']}` symptoms matched ({match_percentage:.1f}%)")
                st.markdown(f"**Symptoms Matched:** {', '.join(data['symptoms_matched'])}")
                st.markdown(f"**Differentiating Factors:** {data['differentiating_factors']}")
                st.markdown("---") # Add a separator between diseases
                
if __name__ == "__main__":
    main()
