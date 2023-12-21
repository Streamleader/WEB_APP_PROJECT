import streamlit as st
import requests
from streamlit_lottie import st_lottie


st.set_page_config(page_title="Pamela web",
                   page_icon=" :tada: ", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_coding = load_lottieurl(
    "https://lottie.host/d6157a2f-2210-4d08-87ce-b0ee86e63582/oFM955fky2.json")


# -----HEADER SECTION -----
with st.container():
    st.subheader("Hi i am Dimpho :wave:")
    st.title("And i just wanted make your day cute little stubborn thang.")
    st.write("bloom and get brighter")


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("TO PAMELA")
        st.write("##")

        st.write(
            """
            ake tsebe ke ngwaleng but just know that:
            - O botsana 
            - you real
            - And you gonn make a great engineer 
            - Most importantly ketlo nyala ka masepa 
            - Data scientist e bhoregileng ":laugh:"
         
            If you feeling lonely click below: 
            """
        )
        click_here = st.write(
            "[Click here >](https://www.youtube.com/watch?v=bxZ2-7LpHig)")
    with right_column:
        st_lottie(lottie_coding, height=500, key="coding")
