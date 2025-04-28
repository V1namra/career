import streamlit as st
import google.generativeai as genai

# Configure Gemini
genai.configure(api_key="AIzaSyCwQafuO1GiOXIcUSzxVXaS0O7zJfLzTgo")  # <-- Replace with your Gemini API key

# Load Gemini 1.5 Flash model
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# Streamlit App
def main():
    st.title("AI Career Prediction System 🚀 ")

    skills = st.text_input("Enter your skills (comma separated)", "")
    interests = st.text_input("Enter your interests (comma separated)", "")
    grades = st.slider("Academic Performance (%):", 0, 100, 60)

    if st.button("Predict Career"):
        with st.spinner('Thinking... 🤔'):
            prompt = f"""
            You are an AI Career Counselor.

            Based on the following candidate information:
            - Skills: {skills}
            - Interests: {interests}
            - Academic Performance: {grades}%

            Recommend:
            1. A suitable career title (just the job name).
            2. A short description (2-3 lines) explaining why this career fits the candidate.

            Keep the response friendly and simple.
            """

            response = model.generate_content(prompt)
            result = response.text

            st.subheader("🎯 Career Recommendation:")
            st.write(result.strip())

if __name__ == "__main__":
    main()
