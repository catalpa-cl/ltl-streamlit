from io import StringIO
import streamlit as st
from annotated_text import annotated_text
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
import pandas as pd
import numpy as np
import random
import altair as alt

"""
# Essay Scoring Example

This page shows you interesting things about your essay
"""

option = st.sidebar.selectbox(
    'Select Mode',
     ["simple", "advanced"])


### POS Checkboxes
st.sidebar.write("Which POS Tags do you want to highlight?")
noun = st.sidebar.checkbox('Nouns')
verb = st.sidebar.checkbox('Verbs')
adj = st.sidebar.checkbox('Adjectives')


col1, col2 = st.beta_columns([3, 1])


essay_txt = col1.text_input('Enter your essay here', value='This is a nice example.')
uploaded_file = col1.file_uploader("Or choose a file to upload.")

if uploaded_file:
    essay_txt =  StringIO(uploaded_file.getvalue().decode("utf-8")).read()

tagged_text = pos_tag(word_tokenize(essay_txt), tagset='universal')

colors = {"VERB" : "#faa",
          "NOUN" : "#8ef",
          "ADJ" : "#afa"}

active_tags = []
if noun:
    active_tags.append("NOUN")
if verb:
    active_tags.append("VERB")
if adj:
    active_tags.append("ADJ")


annotations = []
for elem in tagged_text:
    word = elem[0]+" "
    tag = elem[1]

    if tag in active_tags:
        annotations.append((word,tag,colors[tag]))
    else:
        annotations.append(word)

length = len(essay_txt)
if option == "advanced":
    with col2:
        st.subheader("Statistics")
        st.write("Length in chars: ", length)
        st.write("Number of nouns:", len(list(elem for elem in annotations if elem[1] == "NOUN")))

with col1:
    annotated_text(*annotations)

df = pd.DataFrame(
    [random.randint(0,50) for i in range(100)],
    columns=['length']
)

base = alt.Chart(df)

bar = base.mark_bar().encode(
    x=alt.X('length', bin=True),
    y='count()'
)

rule = base.mark_rule(color='red').encode(
    x=alt.value(length),
    size=alt.value(3)
)

c = bar + rule
st.altair_chart(c, use_container_width=True)

import plotly.express as px
fig = px.histogram(df, x="length",
                   marginal="rug", # or violin, rug
                   hover_data=df.columns)
fig.update_layout(shapes=[
    dict(
      type= 'line',
      yref= 'paper', y0= 0, y1= 1,
      xref= 'x', x0=length, x1=length
    )
])
st.plotly_chart(fig, use_container_width=True)

#annotated_text(
#        "This ",
#        ("is", "verb", "#8ef"),
#        " some ",
#        ("annotated", "adj", "#faa"),
#        ("text", "noun", "#afa"),
#        " for those of ",
#        ("you", "pronoun", "#fea"),
#        " who ",
#        ("like", "verb", "#8ef"),
#        " this sort of ",
#        ("thing", "noun", "#afa"),
#    )
