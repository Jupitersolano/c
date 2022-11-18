import pickle
import requests
import config
import numpy as np
from fastapi import FastAPI

App = FastAPI()

crop_recommendation_model_path = 'APP\model\RandomForest.pkl'
crop_recommendation_model = pickle.load(
    open(crop_recommendation_model_path, 'rb'))


@ App.route('/crop-predict', methods=['POST'])
def crop_prediction():
   
    if requests.method == 'POST':
        N = int(requests.form['nitrogen'])
        P = int(requests.form['phosphorous'])
        K = int(requests.form['pottasium'])
        ph = float(requests.form['ph'])
        rainfall = float(requests.form['rainfall'])
        humidity = float(requests.form['humedad relativa en %'])
        temperature = int(requests.form['Temperatura en celsius'])
        Ganacia_seco = int(requests.form['Peso temporada seca'])
        Ganacia_agua = int(requests.form['Peso temporada lluviosa'])

               
        data = np.array([[N, P, K, temperature, humidity, ph, rainfall, humidity, temperature,Ganacia_seco, Ganacia_agua]])
        my_prediction = crop_recommendation_model.predict(data)
        final_prediction = my_prediction[0]

        return(final_prediction)

if __name__ == "__main__":
    App.run("main:App", port= 8000)      


