from keras.datasets import mnist
import matplotlib.pyplot as plt
import numpy as np
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.utils import np_utils
from sklearn import preprocessing
import pickle
from keras.models import model_from_yaml



def classifier():
    """
    Creates an model for MNIST image classification with input dimension 784
    returns: Keras model
    """

    model = Sequential()
    model.add(Dense(num_pixels,input_dim=num_pixels,kernel_initializer='normal',activation='relu'))
    model.add(Dense(int(num_pixels/2),activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(int(num_pixels/2),activation='relu'))
    model.add(Dense(int(num_pixels/2),activation='relu'))

    model.add(Dense(num_classes,activation='softmax'))

    return model

def writeResultsToFile(events,filePath):
    """
    Writes events to pickle file. Ideally dump few objects where the objects could be any data structures
    containing other objects
    :param events:
    :param filePath:
    """
    print("Writing...")
    if filePath[-3:]!="pkl":
        filePath = filePath+".pkl"

    with open(filePath, "wb") as output:

        pickle.dump(events, output, pickle.HIGHEST_PROTOCOL)

def loadResultsFromFile(filePath,python2 = False):
    """
    Loads objects from pickle file
    :param filePath:
    :return: values in pickle file
    """
    load = []
    print("Loading...")
    with open(filePath, "rb") as file:
        hasNext = True
        if python2:

            load.append(pickle.load(file))
        else:
            load.append(pickle.load(file, encoding='latin1'))
        while hasNext:
            try:
                if python2:
                    load.append(pickle.load(file))
                else:
                    load.append(pickle.load(file, encoding='latin1'))
            except:
                hasNext = False

    if len(load) == 1:
        return load[0]
    else:
        return load

# flatten 28*28 images to a 784 vector for each image
(x_train, y_train), (x_test, y_test) = mnist.load_data()

num_pixels = x_train.shape[1] * x_train.shape[2]
x_train = x_train.reshape(x_train.shape[0], num_pixels).astype('float32')
x_test = x_test.reshape(x_test.shape[0], num_pixels).astype('float32')

# one hot encode outputs
y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)
num_classes = y_test.shape[1]

num_classes = 10


# Scale Data
scaler = preprocessing.MinMaxScaler(feature_range=(0,1))
scaler.fit(x_train)
x_train = scaler.transform(x_train)

scaler.fit(x_test)
x_test = scaler.transform(x_test)


# Create and compile model

model = classifier()
model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
model.fit(x_train,y_train,validation_data=(x_test, y_test), epochs=10, batch_size=200,verbose = 1)

# Export Model
yaml_string = model.to_yaml()
writeResultsToFile(yaml_string,"model_yaml.pkl")
model.save_weights('neural_net_weights')
