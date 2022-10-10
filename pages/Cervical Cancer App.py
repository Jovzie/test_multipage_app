import streamlit as st
import joblib
import pandas as pd
st.image("ribbon.jpg")
st.title("Cervical Cancer Predictor")


data = pd.read_csv("pages/risk_factors_cervical_cancer.csv")

st.subheader("This test will use a machine learning model to predict whether you are likely to be diagnosed with cervical cancer based on all of the questions below. Please answer each of the following questions and then click on 'Predict'.")

col1, col2, col3 = st.columns(3)
age = int(col1.number_input("Enter your age:", step=1, min_value=0))
num_partners = int(col2.number_input("Enter your number of sexual partners:", step=1, min_value=0))
age_inter = int(col3.number_input("Enter your age of first sexual intercourse:", step=1, min_value=0))
num_preg = int(col1.number_input("Enter the number of pregnancies you've had:", step=1, min_value=0))
smokes = True if col2.selectbox("Do you smoke?:", ["Yes", "No"]) else False
smokes_year = int(col3.number_input("How many years have you smoked?", step=1, min_value=0))
smokes_per_year = int(col1.number_input("How many packs per year do you smoke?", step=1, min_value=0 ))
hormonal_contraceptives = True if col2.selectbox("Are you using hormonal contraceptives?", ["Yes", "No"]) == "Yes" else False
hormonal_years = int(col3.number_input("How many years have you been using hormonal contraceptives?", step=1, min_value=0))
IUD = True if col1.selectbox("Do you have an IUD?", ["Yes", "No"]) == "Yes" else False
IUD_years = int(col2.number_input("How many years have you had an IUD?", step=1, min_value=0))
STD = True if col3.selectbox("Have you ever had an STD?", ["Yes", "No"]) == "Yes" else False
STD_num = int(col1.number_input("How many STDs have you had?", step=1, min_value=0 ))
std_cond = True if col2.selectbox("Have you had condylomatosis?", ["Yes", "No"]) == "Yes" else False
std_ccond = True if col2.selectbox("Have you had cervical condylomatosis?", ["Yes", "No"]) == "Yes" else False
std_vcond = True if col3.selectbox("Have you had vaginal condylomatosis?", ["Yes", "No"]) == "Yes" else False
std_vpc = True if col1.selectbox("Have you had vaginal vulvo-perineal condylomatosis?", ["Yes", "No"]) == "Yes" else False
std_syp = True if col2.selectbox("Have you had syphilis?", ["Yes", "No"]) == "Yes" else False
std_pid = True if col3.selectbox("Have you had pelvic inflammatory disease?", ["Yes", "No"]) == "Yes" else False
std_gh = True if col1.selectbox("Have you had genital herpes?", ["Yes", "No"]) == "Yes" else False
std_mc = True if col2.selectbox("Have you had molluscum contagiosum?", ["Yes", "No"]) == "Yes" else False
std_a = True if col3.selectbox("Have you had AIDS?", ["Yes", "No"]) == "Yes" else False
std_h = True if col1.selectbox("Have you had HIV?", ["Yes", "No"]) == "Yes" else False
std_hb = True if col2.selectbox("Have you had Hepatitis B?", ["Yes", "No"]) == "Yes" else False
std_hpv = True if col3.selectbox("Have you had HPV?", ["Yes", "No"]) == "Yes" else False
total_std = int(col1.number_input("How many total STD diagnoses do you have right now?", step=1, min_value=0))
std_start = int(col2.number_input("How long in years has it been since your first diagnosis?", step=1, min_value=0))
std_last = int(col3.number_input("How long in years has it been since your last diagnosis?", step=1, min_value=0))
cin = True if col1.selectbox("Have you been diagnosed with CIN?", ["Yes", "No"]) == "Yes" else False
hpv = True if col2.selectbox("Have you been diagnosed with HPV?", ["Yes", "No"]) == "Yes" else False
dx = True if col3.selectbox("Have you ever received a Dx test?", ["Yes", "No"]) == "Yes" else False
hin = True if col1.selectbox("Have you ever received a Hinselmann test?", ["Yes", "No"]) == "Yes" else False
sch = True if col2.selectbox("Have you ever received a Schiller test?:", ["Yes", "No"]) == "Yes" else False
cit = True if col3.selectbox("Have you ever received a Citology test?:", ["Yes", "No"]) == "Yes" else False
bio = True if col1.selectbox("Have you ever received a Biopsy?", ["Yes", "No"]) == "Yes" else False



pipeline = joblib.load("pages/pipe.pkl")

model = joblib.load("pages/rfc_model.pkl")


if st.button("Predict"):
    input_data = pd.DataFrame(data=[[age, num_partners, age_inter, num_preg, smokes, smokes_year, smokes_per_year, \
    hormonal_contraceptives, hormonal_years, IUD, IUD_years, STD, STD_num, std_cond, std_ccond, std_vcond, std_vpc, std_syp, \
    std_pid, std_gh, std_mc, std_a, std_h, std_hb, std_hpv, total_std, std_start, std_last, cin, hpv, dx, hin, sch, cit, bio]],
    columns=data.drop(columns=["Dx:Cancer"]).columns)
    input_data = pipeline.transform(input_data)
    prediction = model.predict(input_data)
    if int(prediction[0]) == 0:
        st.write("The current model indicates that you are not likely to be diagnosed with cervical cancer.")
    else:
        st.write("The current model indicates that you may be likely to be diagnosed with cervical cancer.")


st.text("")
st.text("")
st.text("")
st.write("This test does not replace regular visits to your doctor.")