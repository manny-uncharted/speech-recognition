            
# Python program to translate
# speech to text and text to speech
 
 
import speech_recognition as sr
import pyttsx3
from py.functions import *
import nltk
# nltk.download('punkt')
# nltk.download('stopwords')
 
# Initialize the recognizer
r = sr.Recognizer()
 
# Function to convert text to
# speech
def SpeakText(command):
     
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
     
     
# Loop infinitely for user to
# speak
 
while(1):   
     
    # Exception handling to handle
    # exceptions at the runtime
    try:
         
        # use the microphone as source for input.
        with sr.Microphone() as source2:
             
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            print("Speak into the microphone")
            r.adjust_for_ambient_noise(source2, duration=0.2)
             
            #listens for the user's input
            audio2 = r.listen(source2)
             
            # Using google to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

            x_input = str(MyText)
            x_input, pred_class, pred_prob = make_prediction(x_input)
            print("Predicted class: ", pred_class)
            # print("Did you say ", x_input)
            SpeakText(pred_class)
            
             
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
         
    except sr.UnknownValueError:
        print("unknown error occurred")


# SpeakText(MyText)