import streamlit as st
import requests
import os
from io import BytesIO
import streamlit.components.v1 as components
import speech_recognition as sr
import pyttsx3
from py.functions import *
import nltk

from audio_output import *
from pydub import AudioSegment
from pydub.silence import split_on_silence




st.title('Abuse Voice Recognition')

wave = st.file_uploader("Upload a file", type=["wav"])

if wave is not None:
    # display audio data as received on the backend
    # st.audio(wav_audio_data, format='audio/wav')
    # wav_audio_data = AudioSegment.from_wav(wav_audio_data)
    # wav_audio_data.export("audio.wav", format="wav")
    info = st.audio(wave, format='audio/wav')
    silence_based_conversion(wave)