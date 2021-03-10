import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
import base64
import seaborn as sns
import matplotlib as plt
from matplotlib import pyplot

st.set_page_config("SAS Dataset Analyzer", None, "wide", "auto")
st.title('SAS Dataset Analysis')
#st.title('Model Statistics')

col1, col2 = st.beta_columns(2)

with col1:

    #option = st.sidebar.selectbox(
    #    'Select Mode',
    #     ["simple", "advanced"])

    st.header('Upload your dataset')
    uploaded_file = st.file_uploader("Choose a file")
    dataframe = None
    if uploaded_file:
        dataframe = pd.read_csv(uploaded_file, delimiter="\t")
        #st.write(dataframe)

    if dataframe is not None:
        st.header('Dataset Statistics')
        #Label Distribution bar chart
        st.subheader('Label Distribution')
    #label_data = pd.DataFrame(
        #np.random.randint(low=0,high=1000,size=5),
        #columns=['Label Frequency'])
        st.bar_chart(dataframe['label'])

        st.subheader('Length Distribution')
        length_data = pd.DataFrame(
            np.random.randint(low=0,high=1000,size=30),
            columns=['Length Frequency'])

        st.bar_chart(length_data)


# Duplicates



st.sidebar.header('Configuration')

# Einstelloptionen
# Language
option = st.sidebar.selectbox(
    'Which language?',
     ['German','English'])
#'You selected: ', option

# Numerical Data?
labels = st.sidebar.radio(
    "Label type?",
    ('Categorical', 'Numeric - discrete', 'Numeric continuous'))

# Features
#token_n_grams = st.sidebar.checkbox('token n-grams')
#pos_n_grams = st.sidebar.checkbox('POS n-grams')
#length_features = st.sidebar.checkbox('length')

#if token_n_grams:
     #st.write('Great!')

# Features, Option 2
options = st.sidebar.multiselect(
    'Which features do you want to use',
    ['token n-grams', 'Char n-grams', 'Answer length'],
    ['token n-grams'])

#st.write('You selected:', options)

#Algorithm?
algorithm = st.sidebar.radio(
    "Algorithm?",
    ('SVM', 'Regression', 'Decision Tree'))


#Analyze Button
st.sidebar.button('Train model')


with col2:
    # option = st.sidebar.selectbox(
    #    'Select Mode',
    #     ["simple", "advanced"])

    st.header('Model Statistics')
    st.subheader('Learning Curve')
    #st.line_chart
    chart_data = pd.DataFrame({
        'data': [10,20,30,40,50,10,20,30,40,50,10,20,30,40,50],
        'performance': [2,5,7,10,12,1,2,4,5,6,0,1,2,2,5],
        'condition': ['best', 'best', 'best', 'best', 'best', 'avg', 'avg', 'avg', 'avg', 'avg', 'worst', 'worst', 'worst', 'worst', 'worst']
    })

    custom_chart = alt.Chart(chart_data).mark_line().encode(
        x='data',
        y='performance',
        color=alt.Color('condition',
                        scale=alt.Scale(
                            domain=['best','avg','worst'],
                            range=['green','blue','red'])
                        )
    ).properties(
        width=600,
        height=300
    )

    st.altair_chart(custom_chart)

    dims = (5,4)
    fig, ax = pyplot.subplots(figsize=dims)
    data = {'y_Actual':    [1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0],
            'y_Predicted': [1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0]
            }
    df = pd.DataFrame(data, columns=['y_Actual','y_Predicted'])
    confusion_matrix = pd.crosstab(df['y_Actual'], df['y_Predicted'], rownames=['Actual'], colnames=['Predicted'])
    sns.heatmap(confusion_matrix, annot=True,ax=ax)
    st.pyplot(fig)


# CV




# Download Model
def get_model_download_link(df):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a href="data:file/csv;base64,{b64}">Download csv file</a>'

#st.markdown(get_model_download_link(dataframe), unsafe_allow_html=True)

#st.markdown(
#        f"""
##<style>
#    .reportview-container .main .block-container{{
#        max-width: 80vw
#    }}
#</style>