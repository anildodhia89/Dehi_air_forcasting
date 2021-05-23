# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 19:48:56 2021

@author: AniDod
"""

import pandas as pd
import numpy as np
import streamlit as st 
import datetime


st.title('Model Deployment: Forcasting')

st.sidebar.header('User Input Parameters')

def user_input_features():

    
  
    DAT = st.sidebar.date_input("Insert Date",datetime.date(2018,4,20),datetime.date(2018,1,1),datetime.date(2018,4,30))
    #DAT = st.sidebar.date_input("Insert Date",datetime.date(3,30,2018),datetime.date(1,1,2018),datetime.date(4,30,2018))
     #HR1= st.sidebar.time_input("Hour",value=00)
    HR = st.sidebar.number_input("Hour",min_value=0,max_value=23)
   # hour_to_filter = st.slider('hour', 0, 23, 17)

    data = {
            
            'DAT':DAT,
             'HR':HR
          #  'hour_to_filter':hour_to_filter,
            }
    
    features = pd.DataFrame(data,index = [0])
    return features 
    
df1 = user_input_features()
st.subheader('User Input parameters')
st.write(df1)


#df = pd.read_csv("C:/Deployment/forecasting.csv", error_bad_lines=False,encoding='latin-1')
df = pd.read_csv("C:/Deployment/forecasting.csv")
#df = pd.read_excel("C:/Deployment/forecasting.xlsx")


X=df["Date"].astype(str)

#from datetime import datetime

df1["period"] = df1["DAT"].astype(str)+' '+df1["HR"].astype(str)

Z=df1['period'] + str(':00')
#Z

df["Indexes"]= df["Date"].str.find(Z[0])
R=df["Indexes"]

Q=df.groupby('Indexes')

P=df.groupby(['Date'])['Indexes'].count()[0]

try:
     if P > 0: 
       #print('Predicted Result')  
       #print(Q.get_group(0))
       st.subheader('Predicted Result')  
       st.write(Q.get_group(0))
#else :
        #st.subheader('No data available')    
except:
        st.subheader('No data available')  
        
        