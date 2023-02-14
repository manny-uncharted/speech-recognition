import streamlit as st
import requests
import os
from io import BytesIO
import streamlit.components.v1 as components
from st_custom_components import st_audiorec

import speech_recognition as sr
import pyttsx3
from py.functions import *
import nltk

from audio_output import *
from pydub import AudioSegment
from pydub.silence import split_on_silence




st.title('Abuse Voice Recognition')

wav_audio_data = st_audiorec()

if wav_audio_data is not None:
    # display audio data as received on the backend
    # st.audio(wav_audio_data, format='audio/wav')
    info = st.audio(wav_audio_data, format='audio/wav')
    silence_based_conversion(info)