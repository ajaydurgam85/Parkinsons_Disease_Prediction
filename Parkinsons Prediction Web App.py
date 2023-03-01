# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 00:15:17 2023

@author: Ajay
"""

import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('C:/Users/Ajay/Desktop/ML-Project-6=(Parkinsons Disease Prediction)/parkinson_train_model.sav','rb'))

def Parkinsons_Prediction(input_data):
    
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshape = input_data_as_numpy_array.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshape)
    print(prediction)

    if (prediction[0]==0):
        return "The Person is Healthy"
        
    else:
        return "The Person has Parkinsons Disease"
    
def main():
    
    st.title("Parkinsons Prediction Web App")
    

    
    MDVPFo = st.text_input("Enter MDVP:Fo(Hz)")
    MDVPFhi = st.text_input("Enter MDVP:Fhi(Hz)")
    MDVPFlo = st.text_input("Enter MDVP:Flo(Hz)")
    MDVPJitter = st.text_input("Enter MDVP:Jitter")
    MDVPJitter2 = st.text_input("Enter  MDVP:Jitter(Abs)")
    MDVPRAP = st.text_input("Enter MDVP:RAP")
    MDVPPPQ = st.text_input("Enter MDVP:PPQ")
    JitterDDP = st.text_input("Enter Jitter:DDP")
    MDVPShimmer = st.text_input("Enter MDVP:Shimmer")
    MDVPShimmer2 = st.text_input("Enter MDVP:Shimmer(dB)")
    ShimmerAPQ3 = st.text_input("Enter Shimmer:APQ3")
    ShimmerAPQ5 = st.text_input("Enter Shimmer:APQ5")
    MDVPAPQ = st.text_input("Enter  MDVP:APQ")
    ShimmerDDA = st.text_input("Enter Shimmer:DDA")
    NHR = st.text_input("Enter NHR")
    HNR = st.text_input("Enter  HNR")
    RPDE = st.text_input("Enter RPDE")
    DFA = st.text_input("Enter DFA")
    spread1 = st.text_input("Enter spread1")
    spread2 = st.text_input("Enter spread2")
    D2 = st.text_input("Enter D2")
    PPE = st.text_input("Enter PPE")
    
    Disease = ''
    
    if st.button("Parkinsons Predict Result"):
        
        Disease = Parkinsons_Prediction([MDVPFo,MDVPFhi,MDVPFlo,MDVPJitter,MDVPJitter2,MDVPRAP,MDVPPPQ,JitterDDP,MDVPShimmer,MDVPShimmer2,ShimmerAPQ3,ShimmerAPQ5,MDVPAPQ,ShimmerDDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE])
        
        
        
        st.success(Disease)
        
if __name__=='__main__':
    main()
    