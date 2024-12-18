import numpy as np
from keras.models import Sequential
from keras.layers import Dense, LSTM

def build_traffic_flow_model(input_shape):
    model = Sequential()
    model.add(LSTM(50, return_sequences=True, input_shape=input_shape))
    model.add(LSTM(50))
    model.add(Dense(1))

    model.compile(optimizer='adam', loss='mse')
    return model
