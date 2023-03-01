# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 00:11:41 2023

@author: Ajay
"""

import numpy as np
import pickle

loaded_model = pickle.load(open('C:/Users/Ajay/Desktop/ML-Project-6=(Parkinsons Disease Prediction)/parkinson_train_model.sav','rb'))

input_data= (116.34200,581.28900,94.24600,0.00267,0.00002,0.00115,0.00148,0.00345,0.01300,0.11700,0.00631,0.00789,0.01144,0.01892,0.00680,25.02300,0.528485,0.663884,-6.359018,0.116636,2.152083,0.138868)
input_data_as_numpy_array = np.asarray(input_data)
input_data_reshape = input_data_as_numpy_array.reshape(1,-1)
prediction = loaded_model.predict(input_data_reshape)
print(prediction)

if (prediction[0]==0):
    print("The Person is Healthy")
    
else:
    print("The Person has Parkinsons Disease")