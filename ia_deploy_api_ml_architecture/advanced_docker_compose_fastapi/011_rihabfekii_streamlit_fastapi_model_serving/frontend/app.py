#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
[env]
# Conda Environment
conda create --name streamlit_fastapi_model_serving python=3.9.13
conda info --envs
source activate streamlit_fastapi_model_serving
conda deactivate

# if needed to remove
conda env remove -n [NAME_OF_THE_CONDA_ENVIRONMENT]
conda env remove -n streamlit_fastapi_model_serving

# update conda 
conda update -n base -c defaults conda

# to export requirements
pip freeze > requirements.txt

# to install
pip install -r requirements.txt

# other module
pip install streamlit
pip install watchdog
pip install requests

# [path]
cd /Users/brunoflaven/Documents/01_work/blog_articles/ia_deploy_api_ml_architecture/advanced_docker_compose_fastapi/009_davidefiocco_streamlit_fastapi_model_serving/

# launch the app
streamlit run ui.py


"""

import streamlit as st
import requests

#***************************** Start HTML configuration *****************************

st.set_page_config(page_title ="AI service App",initial_sidebar_state="expanded", layout="wide", page_icon="💦")
  
# change the color of button widget
Color = st.get_option("theme.secondaryBackgroundColor")
s = f"""
<style>
div.stButton > button:first-child {{background-color: #fffff ; border: 2px solid {Color}; border-radius:5px 5px 5px 5px; }}
<style>
"""
st.markdown(s, unsafe_allow_html=True)

def fetch_name(letter):
	base_url = "http://backend.docker:8000/generate_name?starts_with={}".format(letter)
	resp = requests.get(base_url)
	return resp.json()
	

def main():
	st.title("AI service App Docker rihabfekii Water potability prediction 💦")

	letter = st.text_input("Enter a letter")
	if st.button("Retrieve"):

		# st.write(letter)
		
		results = fetch_name(letter)
		st.json(results)



if __name__ == '__main__':
	main()
	