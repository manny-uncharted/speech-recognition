import speech_recognition as sr
import pyttsx3
from py.functions import *
import nltk
import os
import streamlit as st
# nltk.download('punkt')
# nltk.download('stopwords')
from pydub import AudioSegment
from pydub.silence import split_on_silence

# Initialize the recognizer
r = sr.Recognizer()


def SpeakText(command):
     
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()




# a function that splits the audio file into chunks
# and applies speech recognition
def silence_based_conversion(path = "Recording.wav"):
  
    # open the audio file stored in
    # the local system as a wav file.
    song = AudioSegment.from_wav(path)
  
    # open a file where we will concatenate  
    # and store the recognized text
    fh = open("recognized.txt", "w+")
    song.export("song.wav", bitrate ='192k', format ="wav")
  
    #     # the name of the newly created chunk
    filename = 'song'+'.wav'
  
    #     print("Processing chunk "+str(i))
  
    #     # get the name of the newly created chunk
    #     # in the AUDIO_FILE variable for later use.
    file = filename
  
        # create a speech recognition object
    r = sr.Recognizer()

    try:
        with sr.AudioFile(file) as source:
            # remove this if it is not working
            # correctly.
            r.adjust_for_ambient_noise(source)
            audio_listened = r.listen(source)
            
            # try converting it to text
            rec = r.recognize_google(audio_listened)
            rec = rec.lower()
            # print(rec)
            
            x_input = str(rec)
            print(x_input)
            x_input, pred_class, pred_prob = make_prediction(x_input)
            st.text("{}, Prediction probability {}".format(pred_class, pred_prob))
            # SpeakText(pred_class)

    # catch any errors.
    except sr.UnknownValueError:
        print("Could not understand audio")

    except sr.RequestError as e:
        print("Could not request results. check your internet connection")

    