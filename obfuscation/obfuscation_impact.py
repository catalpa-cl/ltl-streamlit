import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
import base64
import seaborn as sns
import matplotlib as plt
from matplotlib import pyplot

def obfuscate(strategy, mode, text):
    strategy + ": " + text

st.set_page_config("Obfuscation Impact Analyzer", None, "wide", "auto")
st.title('Obfuscation Impact Analyzer')

st.sidebar.write("Obfuscation strategies")
asterisks = st.sidebar.checkbox('Asterisks', True)
prefix = st.sidebar.checkbox('Prefix', True)
camelcase = st.sidebar.checkbox('CamelCase', True)
leetspeak = st.sidebar.checkbox('Leetspeak', True)

mode = st.sidebar.selectbox(
   'Obfuscation Mode',
    ["all", "random"]
)

text = st.text_input('Enter your post here', value='all scientists are bloody bastards')

# that can probably be done much nicer
if asterisks:
    obfuscate("asterisks", mode, text)
if prefix:
    obfuscate("prefix", mode, text)
if camelcase:
    obfuscate("camelcase", mode, text)
if leetspeak:
    obfuscate("leetspeak", mode, text)

classify = st.button('Classify')

if classify:
    st.write("everything is hate you bloody science bastard!!!")
