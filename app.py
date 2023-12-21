#

import streamlit as st
import requests
from streamlit_lottie import st_lottie


st.set_page_config(page_title="My web page",
                   page_icon=" :tada: ", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_coding = load_lottieurl(
    "https://lottie.host/5c548922-c780-4868-b7a4-6bb781eb7bdb/kbVog1Zi5e.json")


# -----HEADER SECTION -----
with st.container():
    st.subheader("Hi i am Dimpho :wave:")
    st.title("A Data Scienctist from South Africa.")
    st.write(
        "I intend to present to you the beauties of Data science in this Morden life ")


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("ABOUT DATA SCIENCE:")
        st.write("##")

        st.write(
            """
            What is data science?

Data science is the study of data to extract meaningful insights for business.
It is a multidisciplinary approach that combines principles and practices from the fields of mathematics, statistics, artificial intelligence, 
and computer engineering to analyze large amounts of data. 
This analysis helps data scientists to ask and answer questions like what happened, 
why it happened, what will happen, and what can be done with the results.
            
            Why is data science important?

Data science is important because it combines tools, methods, and technology to generate meaning from data.
Modern organizations are inundated with data; there is a proliferation of devices that can automatically collect and store information.
Online systems and payment portals capture more data in the fields of e-commerce, medicine, finance, and every other aspect of human life.
We have text, audio, video, and image data available in vast quantities.  
           
             - KEY PIONTS/USE OF DATA SCIENCE:
            - Obtain data
            - Scrub data
            - Explore data 
            - Model data
            - Interpret results
         
            To Learn more: 
             """
        )
        click_here = st.write(
            "[Click here >](https://www.ibm.com/topics/data-science)")
    with right_column:
        st_lottie(lottie_coding, height=500, key="coding")


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with right_column:
        st.header("CREDITS:")
        st.write("##")
