import pickle
import request
import config
import numpy as np
from fastapi import FastAPI

App = FastAPI()

crop_recommendation_model_path = 'APP\model\RandomForest.pkl'
crop_recommendation_model = pickle.load(
    open(crop_recommendation_model_path, 'rb'))


@ App.route('/crop-predict', methods=['POST'])
def crop_prediction():
   
    if request.method == 'POST':
        N = int(request.form['nitrogen'])
        P = int(request.form['phosphorous'])
        K = int(request.form['pottasium'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])
        humidity = float(request.form['humedad relativa en %'])
        temperature = int(request.form['Temperatura en celsius'])
        Ganacia_seco = int(request.form['Peso temporada seca'])
        Ganacia_agua = int(request.form['Peso temporada lluviosa'])

               
        data = np.array([[N, P, K, temperature, humidity, ph, rainfall, humidity, temperature,Ganacia_seco, Ganacia_agua]])
        my_prediction = crop_recommendation_model.predict(data)
        final_prediction = my_prediction[0]

        return(final_prediction)

if __name__ == "__main__":
    App.run("main:App", port= 8000)      


