import streamlit as st
from pipeline.pipeline import AnimeRecommendationPipeline
from dotenv import load_dotenv
import time

load_dotenv()

st.set_page_config(page_title = "Aiops project",layout="wide")
st.title("anime recommender")

@st.cache_resource
def init_pipeline():
    return AnimeRecommendationPipeline()

pipeline = init_pipeline() # one-time initialize the pipeline

query = st.text_input("query")
if query:
    with st.spinner("fetching data ...",show_time=True):
        response=pipeline.recommend(query)
        st.markdown("Responses: ",unsafe_allow_html=True)
        st.write(response)

