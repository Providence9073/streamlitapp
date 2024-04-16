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
#st.header("Diabettes Prediction System")
age = st.slider("Age",0,100)
hyp = st.select_slider("hypertention",["Yes","No"])
bmi = st.slider("BMI",0.0,100.0)
hb = st.slider("  HbA1c_level",0.0,100.0)
glu =st.slider("Blood Sugar",0,100)
hd = st.select_slider("Hearth Disease",["Yes","No"])







if st.button("predict"):
   hyp_v, hd_v = let_to_num(hyp, hd)
   pre =  j.predict([[age,hyp_v,hd_v,bmi,hb,glu]])
   st.text_input("prediction result",num_to_let(pre))
#st.number_input()


