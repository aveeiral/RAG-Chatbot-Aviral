import streamlit as st
import speech_recognition as sr
from gtts import gTTS
import os

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening...")
        try:
            audio = recognizer.listen(source, timeout=25)
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Could not understand the audio."
        except sr.RequestError:
            return "Could not request results. Check your internet connection."

def text_to_speech(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    tts.save("response.mp3")
    return "response.mp3"

st.title("🗣️ Voice Bot")

if st.button("Start Talking"):
    user_text = recognize_speech()
    st.write("You said:", user_text)
    
    # Simple response logic
    if "hello" in user_text.lower():
        response = "Hello! How can I assist you today?"
    else:
        response = "I heard you say: " + user_text
    
    audio_file = text_to_speech(response)
    st.audio(audio_file, format='audio/mp3')