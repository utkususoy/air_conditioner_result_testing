import numpy as np
import pickle

def predictor(values, normal_values=[23, 36, 80], normal_energy=48.55):
    normal_values = np.asarray(normal_values)
    values = np.asarray(values)
    difference = normal_values - values

    loaded_model = pickle.load(open('Energy_Consumption_Model/EnergyConsumptionModel.pkl', 'rb'))
    
    predicted_difference = loaded_model.predict(difference.reshape(1, 3))[0][0]

    return(normal_energy - predicted_difference)


predictor([22, 40, 70])
