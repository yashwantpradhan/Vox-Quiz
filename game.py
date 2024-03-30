import requests
import io
from PIL import Image
import streamlit as st
import random
#import pyttsx3
import speech_recognition as sr
import time
import threading
import pyaudio

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content


# def count_down(ts):
#    with st.empty():
#       while ts:
#         # mins, secs = divmod(ts, 60)
#         # time_now = '{:02d}'.format(secs)
#         time_now = '{}'.format(ts % 60)
#         st.header(f"{time_now}")
#         time.sleep(1)
#         ts -= 1
#         st.header("Time Up!")


def image_generation(image_text_input):
 # image_text_input=st.text_input(label="Input text")
 with st.spinner("Generating image..."):
      image_bytes=query({"inputs":image_text_input})
      image = Image.open(io.BytesIO(image_bytes))
      # image_path=image
      # result=classifier(images=image_path)
      st.image(image,width=500)
      # st.write(result)


#Function to convert text to speech
def speakText(command):
    engine=pyttsx3.init()
    newVoiceRate = 180
    engine.setProperty('rate',newVoiceRate)   
    engine.say(command)
    engine.runAndWait()
    

#Function to take audio as input
def audio_input():
 r = sr.Recognizer()
 with sr.Microphone() as source2:
    r.adjust_for_ambient_noise(source2,duration=0.2)
    try:
     audio2=r.listen(source2,timeout=10,phrase_time_limit=None)
     Mytext=r.recognize_google(audio2)
     Mytext=Mytext.lower()
     return Mytext
    except sr.UnknownValueError:
       return "Time Out"


st.header("____CAN YOU IDENTITY IT?____")
box=st.selectbox("SELECT GAME",["ANIMALS","BIRDS","INSECTS"])
col1,col2=st.columns(2, gap="large")
with col1:
    start_but = st.button('START')
with col2:
    stop_but=st.button('STOP')
placeholder=st.empty()
while(start_but):
  animal_container= animals = ["dog", "cat", "elephant", "tiger", "lion", "giraffe", "hippopotamus", "zebra", "kangaroo", "monkey", "panda", "crocodile", "alligator", "bear", "rabbit", "fox", "wolf", "deer", "squirrel", "raccoon", "moose", "bison", "horse", "cow", "sheep", "goat", "pig"]
  animal_name=random.choice(animal_container)                              #Python countdown timer
  bird_container=birds = ['crow', 'eagle', 'owl', 'sparrow', 'parrot', 'robin', 'pigeon', 'seagull', 'dove', 'woodpecker', 'swallow', 'blackbird', 'wren', 'finch', 'canary', 'heron', 'crane', 'stork', 'pelican', 'penguin', 'flamingo', 'swan', 'duck', 'goose', 'tern', 'swift', 'cuckoo']       #Text reader
  bird_name=random.choice(bird_container)                                  #Voice input #string matching or new modeil which generates caption
  insect_container=insects = ['ant', 'bee', 'beetle', 'butterfly', 'caterpillar', 'centipede', 'cockroach', 'cricket', 'dragonfly', 'earwig', 'firefly', 'flea', 'fly', 'grasshopper', 'ladybug', 'louse', 'moth', 'mosquito', 'praying mantis', 'termite', 'wasp', 'aphid', 'bedbug', 'butterfly', 'cicada', 'hornet', 'housefly', 'lacewing', 'leafhopper', 'millipede', 'midge',  'stick insect', 'stinkbug', 'thrips']
  insect_name=random.choice(insect_container)                               #some parameters which help to generate newimages every time,,,
  if box=="ANIMALS":
   with placeholder.container():
    image_generation(animal_name)
    time.sleep(2)
    with st.empty():
     st.text("Say your answer...")
     # speakText("Say your answer...")
     voice_input=audio_input()
    #  if voice_input=="Time Out":
    #     speakText("Time Out")
     st.text(voice_input)
    if(animal_name in voice_input):
        # speakText("Yes your answer is correct. This is a"+ animal_name)
        st.subheader(animal_name)
        placeholder.empty()  
    elif(voice_input=="Time Out"):
       # speakText(voice_input)
       # speakText("The correct answer is"+ animal_name)
       st.subheader(animal_name)
       placeholder.empty()
    else:
        # speakText("Incorrect")
        # speakText("This is a"+ animal_name)
        st.subheader(animal_name)
        placeholder.empty()
  elif box=="BIRDS":
    with placeholder.container():
     image_generation(bird_name)
     time.sleep(2)
     with st.empty():
      st.text("Say your answer...")
      # speakText("Say your answer...")
      voice_input = audio_input()
      st.text(voice_input)
     if (bird_name in voice_input):
        # speakText("Yes your answer is correct. This is a" + bird_name)
        st.subheader(bird_name)
        placeholder.empty()
     elif(voice_input=="Time Out"):
       # speakText(voice_input)
       # speakText("The correct answer is"+ bird_name)
       st.subheader(bird_name)
       placeholder.empty()
     else:
        # speakText("Incorrect")
        # speakText("This is a" + bird_name)
        st.subheader(bird_name)
        placeholder.empty()
  elif box=="INSECTS":
    with placeholder.container():
     image_generation(insect_name)
     time.sleep(2)
     with st.empty():
      st.text("Say your answer...")
      # speakText("Say your answer...")
      voice_input = audio_input()
      st.text(voice_input)
     if (insect_name in voice_input):
        # speakText("Yes your answer is correct. This is a" + insect_name)
        st.subheader(insect_name)
        placeholder.empty()
     elif(voice_input=="Time Out"):
       # speakText(voice_input)
       # speakText("The correct answer is"+ insect_name)
       st.subheader(insect_name)
       placeholder.empty()
     else:
        # speakText("Incorrect")
        # speakText("This is a" + insect_name)
        st.subheader(insect_name)
        placeholder.empty()










