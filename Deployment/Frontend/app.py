import streamlit as st
import requests
from PIL import Image

st.set_page_config(layout="centered", page_icon="🔥", page_title="Burn Rate Predictor")
st.title("🔥 Burn Rate Predictor 🔥")
st.subheader('This app estimate your burn rate')

image = Image.open('employee-burnout-avoiding-tips.png')
st.image(image, use_column_width=True)

col1, col2 = st.columns(2)

with col1:
    Gender = st.selectbox("Select Gender Type", ['Male', 'Female'])
    Company_Type = st.selectbox("Select Company Type", ['Service', 'Product'])

with col2:
    WFH_Setup_Available = st.selectbox("Does your company allow Work from Home ? ", ['Yes', 'No'])
    Designation = st.number_input("What's your Designation ?", min_value=0, max_value=5, step=1)

Resource_Allocation = st.slider("Amount of Resource Allocated to the Employee", min_value=0, max_value=10)

Mental_Fatigue_Score = st.slider("Level of Fatigue Mentally the Employee is Facing", min_value=0.0, max_value=10.0)


# inference
data = {'Gender':Gender,
        'Company_Type':Company_Type,
        'WFH_Setup_Available': WFH_Setup_Available,
        'Designation':Designation,
        'Resource_Allocation':Resource_Allocation,
        'Mental_Fatigue_Score':Mental_Fatigue_Score}

URL = "https://kamil-riyadi-ftds-009-p1m2.herokuapp.com/predict"

# komunikasi
r = requests.post(URL, json=data)

Predict =  st.button('Predict Burn Rate')
if Predict:

    res = r.json()

    if res['code'] == 200:
        st.snow()
        st.title('Your estimated burn rate is :')
        st.title(res['result']['prediction'])
    else:
        st.write("Whoops, something went wrong")
        st.write(f"description : {res['result']['error_msg']}")