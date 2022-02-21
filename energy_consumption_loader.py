import numpy as np
import pickle

def predictor(loaded_model, values, normal_values=[23, 36, 80], normal_energy=48.55):
    normal_values = np.asarray(normal_values)
    values = np.asarray(values)
    difference = normal_values - values

    predicted_difference = loaded_model.predict(difference.reshape(1, 3))[0][0]

    return(normal_energy - predicted_difference)
