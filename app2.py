import streamlit as st
import joblib
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import joblib


# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("PHONE", "E-MAIL", "MESSAGE")


if add_selectbox == 'PHONE'
    st.number_input("ENTER YOUR PHONE NUMBER")


mile=st.number_input('Enter a Mileage value:')
age=st.number_input('Enter a age value:')


if st.button('PREDICT'):

    data=pd.DataFrame()
    data['Mileage']=[mile]
    data['Age(yrs)']=[age]

    model=joblib.load('Car_selection_Model.joblib')

    prediction=model.predict(data)

    st.write(prediction)


if st.button('PREDICT'):
