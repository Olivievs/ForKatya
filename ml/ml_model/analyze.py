import numpy as np
import pandas as pd
import os
import pickle

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

loaded_model = pickle.load(open(os.path.join(__location__, 'Overweight_model.p'), "rb"))

def analyze_obesity(arr: list)->int:
    global loaded_model
    X = pd.DataFrame(np.array(arr).reshape(1, 16), columns = ["Gender", "Age", "Height", "Weight",
                                                              "family_history_with_overweight",
                                                              "FAVC", "FCVC", "NCP","CAEC", "SMOKE",
                                                              "CH2O", "SCC" ,"FAF", "TUE", "CALC", "MTRANS"
                                                              ]
                     )
    prediction = loaded_model.predict(X)
    return prediction[0]