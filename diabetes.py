import pickle as pk
import streamlit as st
import joblib as jb

def let_to_num (a,b):
    if a == "Yes" and b == "Yes":
        a = 1
        b = 1
    elif b == "Yes" and a == "No":
        b = 1
        a = 0
    elif b == "No" and a == "Yes":
        b = 0
        a = 1
    else:
        a,b = 0,0
    return a,b

def num_to_let (x):
    if x == 0:
        x = "No"
    else:
        x = "Yes"
    return x

m = pk.load(open("diabettes_model.pkl","rb"))
j = jb.load("finalized_model.sav")

st.title("Diabettes Prediction System")
st.header("Diabettes Prediction System")
age = st.text_input("input the value for Age")
bmi = st.text_input("input the value for Bmi")
hyp = st.selectbox("hypertention",["Yes","No"])
hd = st.selectbox("Hearth Diseas",["Yes","No"])
hb = st.text_input("input the value for HbA1c_leve")
glu = st.text_input("input the value for blood_glucose_level")



if st.button("predict"):
   hyp_v, hd_v = let_to_num(hyp, hd)
   pre =  j.predict([[age,hyp_v,hd_v,bmi,hb,glu]])
   st.text_input("prediction result",num_to_let(pre))
#st.number_input()


