from pydantic import BaseModel
import streamlit as st
import requests
import pandas as pd

df = pd.read_csv('BankNote_Authentication.csv')

head = df[['variance','skewness','curtosis','entropy']].head(10)
tail = df[['variance','skewness','curtosis','entropy']].tail(10)
st.image("Pakistan-75-Rupees-2023-UNC-P-New-Design-Commemorative-166232515888-400x380.jpg",width=600)
PEHLA, DUSRA, = st.columns(2)
with PEHLA:
    st.subheader('FAKE NOTES VALUES')
    st.write(head)
with DUSRA:
    st.subheader('REAL NOTES VALUES')
    st.write(tail)
st.subheader('Predict Here')
class BankNote1(BaseModel):
    variance : float
    skewness : float
    curtosis : float
    entropy : float


variance = st.number_input('Enter Variance')
skewness = st.number_input('Enter Skewness')
curtosis = st.number_input('Enter Curtosis')
entropy = st.number_input('Enter Entropy')

if st.button('Predict'):
    data = BankNote1(variance=variance, skewness=skewness, entropy=entropy, curtosis=curtosis)
    response = requests.post('http://localhost:8000/predict', json=data.dict())

    prediction = response.json()['prediction']

    st.write(f'The predicted bank note is: {prediction}')