import streamlit as st
from sklearn.preprocessing import LabelEncoder
import pandas as pd 
import joblib
import numpy as np



video=f"""
  <style>
  .vid{{
      position: fixed;
	  right: 0;
	  bottom: 0;
      min-width: 100%; 
	  min-height: 100%;
    
  }}
  </style>
  
 <video autoplay loop muted class="vid">
 <source src="https://cdn.discordapp.com/attachments/1294905019388395563/1300155687204032593/7821854-hd_1920_1080_30fps.mp4?ex=671fcfd7&is=671e7e57&hm=9b89bb05e400563040993eaaf953374419d51570d72366f4fb33861cfeb753dd&">

  </video>

"""

st.markdown(video,unsafe_allow_html=True)

st.header(f":blue[Loan Approval Prediction System]")
col1,col2,col3=st.columns(3)
with col1:
    edu=st.text_input("Education",placeholder="Graduate/Not Graduate")
    employee=st.text_input("Self-Employed",placeholder="Yes/No")
    income=st.text_input("income_annum",placeholder="Enter income")
    loan=st.text_input("loan_amount",placeholder="Enter loan amount")
with col2:
    term=st.text_input("loan_term",placeholder="Enter the duration of loan")
    cibil=st.text_input("cibil_score",placeholder="Enter the cibil score")
    assets=st.text_input("residential_assets_value",placeholder="Enter the residential assets")
    comm=st.text_input("commercial_assets_value	",placeholder="Enter commercial assets")
with col3:
    luxury=st.text_input("luxury_assets_value",placeholder="Enter luxury assets")
    bank=st.text_input("bank_asset_value",placeholder="Enter Bank Assets value")
if edu=="Graduate":
    edu=0
elif edu=="Not Graduate":
    edu=1
else :
    st.warning("Invalid input of Education", icon="⚠️")
    

if employee=="Yes":
    employee=1
elif employee=="No":
    employee=0
else :
    st.warning("Invalid input of Employee", icon="⚠️")




try:
    edu = float(edu)
    employee = int(employee)
    income = int(income)
    loan = int(loan)
    term = int(term)
    cibil = int(cibil)
    assets = int(assets)
    comm = int(comm)
    luxury = int(luxury)
    bank = int(bank)
    # furnish = int(furnish)
    # road = int(road)
    li=[ edu,employee,income,loan,term,cibil,assets,comm,luxury,bank]
except ValueError:
    st.error("Please make sure all inputs are valid numbers.")
    
df=pd.read_excel('modifyloan.xlsx')

encoder=LabelEncoder()

# df['Education'] = encoder.fit_transform(df['Education'])
# df['Self-Employed'] = encoder.fit_transform(df['Self-Employed'])
# df['income_annum'] = encoder.fit_transform(df['income_annum'])
# df['prefarea'] = encoder.fit_transform(df['prefarea'])
# df['furnishingstatus'] = encoder.fit_transform(df['furnishingstatus'])
# df['hotwaterheating'] = encoder.fit_transform(df['hotwaterheating'])
# df['airconditioning'] = encoder.fit_transform(df['airconditioning'])


if st.button("View"):
  
    
    # li.insert(0,li[0][0])
    # st.write(li)

    arr= np.array(li)
    # st.write(arr)
    model=joblib.load('A-B-Loan.pkl')
    answer=model.predict([arr])
    if answer[0]==0:
        app="Approved"
    else:
        app="Rejected"
    st.subheader(f":blue[Your Loan is  {app}]")


    