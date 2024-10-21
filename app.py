from dotenv import load_dotenv
from PIL import Image 
import os
import streamlit as st #to create the interface of our application 
import google.generativeai as genai #genarativeAI
load_dotenv()



api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key = api_key)

def get_response_from_gemini(question,image):
    model = genai.GenerativeModel("gemini-1.5-flash")
    if question is not None:
       response = model.generate_content([question,image])
    else:
        response = model.generate_content(image)

    return response.text    


st.set_page_config(page_title = "Gemini chatbot")
st.header("GEMINI LLM APPLICATION ")
st.subheader("This is my Gemini llm application ")

question =st.text_input("write your question ", key = "question")
uploaded_file = st.file_uploader("choose your file ", type = ['jpg','jpeg','png'])

imge = " "

if uploaded_file is not None:
    imge = Image.open(uploaded_file)
    st.image(imge, caption= "uploaded image", use_column_width= True)

submit = st.button("submit")

if submit:
    output = get_response_from_gemini(question = question,image=imge)
    st.subheader("Response is : ")
    st.write(output)
    

