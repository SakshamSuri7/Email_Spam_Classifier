import pickle
import streamlit as st
# import pythoncom
# from win32com.client import Dispatch


# def speak_text(text):
#     pythoncom.CoInitialize()
#     speak=Dispatch("SAPI.SpVoice")
#     speak.speak(text)


model = pickle.load( open("spam.pkl","rb"))
cv = pickle.load( open("vectorizer.pkl","rb"))

def predict_spam(text):
    data=[text]
    vect=cv.transform(data).toarray()
    prediction = model.predict(vect)
    return prediction[0]

st.title("Email Spam Classification Model")
st.write("Enter the text of an email or message and the models will predict whether it is Spam or Not Spam.")

msg=st.text_input("Type your email/message here:")

if st.button("Predict"):
    if msg.strip() == "":
        st.warning("Please enter some text")
    else:
        result = predict_spam(msg)

        if result==1:
            st.error("This is a spam email")
            # speak_text("This is a spam email")
        else:
            st.success("This is not a spam email")
            # speak_text("This is not a spam email")


