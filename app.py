import streamlit as st 
import os 
from lib.utils import * 

st.set_page_config(page_title='BoneTumor Vision', layout="wide")
current_directory = os.getcwd()
st.header(":hand: Welcome To BoneTumor Vision ")
st.info("""
BoneTumor Vision is an advanced medical imaging application designed to empower healthcare 
professionals with cutting-edge diagnostic capabilities. This versatile tool combines 
the power of two critical functions: tumor detection and bone-related object detection.
""")
        
model_task = st.sidebar.selectbox("Select your task :" , 
                          ["bone fracture detection" , 
                           "Tumor Detection and Classification"])



if model_task == "bone fracture detection" : 
    model_name_path = f"{current_directory}/bone_fracture_detection/"
    if os.path.exists(model_name_path) :
        model , categories = usemodel(model_name_path)
    else : 
        print("Run 'python Download_weights.py first'")


elif model_task == "Tumor Detection and Classification" : 
    model_name_path = f"{current_directory}/tumor_detection/"
    if os.path.exists(model_name_path) :
        model , categories = usemodel(model_name_path)
    else : 
        print("Run 'python Download_weights.py first'")

save_name = st.sidebar.text_input("Enter your image save name:")
st.sidebar.text("Press Enter to apply")


min_score_thresh=st.slider("Select your threshold Value :", min_value=0.1, max_value=1.0 , value=0.3)

image_up = st.file_uploader("Upload Your Image:")

if image_up : 
    image_name = image_up.name
    current_directory = os.getcwd()
    img_path = f"{current_directory}/{image_name}"
    if st.button('Start Detection') : 
        if save_name : 
            with st.spinner("In progress..") : 
                run(model=model ,categories=categories, 
                    image_path=img_path, 
                    save_name=save_name , 
                    min_score_thresh=min_score_thresh)
                st.image(f"/results/{save_name}.png")
        else : 
            print("Entre image result name first 'Example: result1'")