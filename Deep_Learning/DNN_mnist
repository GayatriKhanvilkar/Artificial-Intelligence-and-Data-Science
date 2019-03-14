# Apply Neural Network on Pima dataset
import keras
import pandas as pd
import numpy as np

np.random.seed(2)
df = pd.read_csv("diabetes.csv")
print(df.head())
print(df.shape)

import seaborn as sns
_ = df.hist(figsize=(12, 10))

# sns.pairplot(df, hue='Outcome')

sns.heatmap(df.corr(), annot=True)

# print(df.info())
# print(df.describe())

from sklearn.preprocessing import StandardScaler
from keras.utils.np_utils import to_categorical
sc = StandardScaler()
X = sc.fit_transform(df.drop('Outcome', axis=1))
Y = to_categorical(df['Outcome'].values)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=22) # data splitting

from keras.layers import Dense
model = keras.Sequential()
model.add(Dense(10, input_dim=8, activation='relu')) #hidden layer with 10 neurons and 8 input neurons in input layer
model.add(Dense(20, activation='relu')) #hidden layer with 20 neurons
model.add(Dense(2, activation='softmax')) #output layer with 2 neuron

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(x_train, y_train, epochs=10, verbose=1, validation_split=0.1) #batch_size= no. of inputs at a time... epochs = no. of iterations for tranin

y_pred = model.predict(x_test)

y_test_class = np.argmax(y_test, axis=1)
y_pred_class = np.argmax(y_pred, axis=1)

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

print(pd.Series(y_test_class).value_counts())
print('accuracy = ', accuracy_score(y_test_class, y_pred_class))
print(classification_report(y_test_class, y_pred_class))
print(confusion_matrix(y_test_class, y_pred_class))
