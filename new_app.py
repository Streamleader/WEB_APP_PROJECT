import streamlit as st
import joblib
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import joblib

model = joblib.load('Car_selection_Model.joblib')
# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

st.subheader('selling price ')

#model = joblib.load('Car_selection_Model.joblib')


mile = st.number_input('Enter a Mileage value:')
age = st.number_input('Enter a age value:')


if st.button('submit'):


    data = pd.DataFrame()
    data['Mileage'] = [mile]
    data['Age(yrs)'] = [age]



    prediction = model.predict(data)

    st.write(prediction)




