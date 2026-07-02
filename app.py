import streamlit as st

st.set_page_config(
    page_title="SMS Spam Detector",
    page_icon="📩",
    layout="centered",
    initial_sidebar_state="collapsed"
)

import pickle
import nltk
import string

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

stemming = PorterStemmer()

#==============================================================
def transform_text(text):
    transform1=text.lower()
    transform2 = nltk.word_tokenize(transform1)
    a = []
    for element in transform2:
        if element.isalnum():
            a.append(element)
    b = []        
    for element in a:
        if element not in stopwords.words('english') and element not in string.punctuation:
            b.append(element)

    c = []
    for element in b:
        c.append(stemming.stem(element))


    return " ".join(c)
#==============================================================


tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))


st.title(" 📩 Email/SMS Spam Classifier")


input_text = st.text_area('Enter the Message 🗨')


if st.button("PREDICT",use_container_width=True):
    #step 1 preprocess
    transformed_sms = transform_text(input_text)
    #step 2 vectorize
    vector_input = tfidf.transform([transformed_sms])
    #step 3 predict
    result = model.predict(vector_input)[0]
    #step 4 display
    if result == 1:
        st.header("🚨 SPAM DETECTED!")
    else:
        st.header("✅ NOT SPAM")


