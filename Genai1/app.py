import streamlit as st
from openai import OpenAI

f = open('API KEY _OPENAI.txt')
OPENAI_API_KEY = f.read()

# Initialize OpenAI client with the API key read from the file
client = OpenAI(api_key=OPENAI_API_KEY)

def main():
    st.set_page_config(page_title="GenAI App - AI Code Reviewer🧑‍💻", page_icon="🤖", layout="wide", initial_sidebar_state="collapsed")
    st.title("GenAI App - AI Code Reviewer🧑‍💻")

    # Input area for Python code
    prompt = st.text_area("Enter your Python code here", height=400)
    
    if st.button("Review Code👆"):
        if prompt:
            # Call OpenAI API to perform code review
            response = client.chat.completions.create(
                model="gpt-3.5-turbo-0613",
                messages=[
                    {"role": "system", "content": """You are a helpful AI Assistant and Code reviewer.
                    Find the Bugs and errors in the program and give me the corrected code."""},
                    {"role": "user", "content": prompt}
                ]
            )
            #
            st.subheader("Code Review Feedback")
            st.snow()
            st.write(response.choices[0].message.content)
        else:
            st.warning("Please enter Python code for review.")

if __name__ == "__main__":
    main()
