# Apply CNN on MNIST dataset
import matplotlib.pyplot as plt

from keras.datasets import mnist
(X_train, y_train), (X_test, y_test) = mnist.load_data(r'C:\Users\GAYATRI KHANVILKAR\PycharmProjects\DNN\tmp\mnist.npz')

plt.imshow(X_train[0], cmap='gray')
plt.show

X_train = X_train.reshape(-1, 28*28) #Flatten the image
X_test = X_test.reshape(-1, 28*28)

X_train = X_train.astype('float32') #Conver to float
X_test = X_test.astype('float32')
X_train /=255.0 #divide each pixel by 255

from keras.utils.np_utils import to_categorical
y_train_cat = to_categorical(y_train) #one hot encoding
y_test_cat = to_categorical(y_test)

# print(y_train_cat.shape)
# print(y_test_cat.shape)

X_train = X_train.reshape(-1, 28, 28, 1)
X_test = X_test.reshape(-1, 28, 28, 1)

print(X_train.shape)

from keras.layers import Conv2D, MaxPool2D, Activation, Flatten, Dense
from keras.models import Sequential


model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=(28, 28, 1), ))
model.add(MaxPool2D(pool_size=(2,2)))
model.add(Activation('relu'))

model.add(Flatten()) #flatten the image
model.add(Dense(128, activation='relu'))
model.add(Dense(10, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

model.summary()

model.fit(X_train, y_train_cat, batch_size=128, epochs=2, verbose=1, validation_split=0.3)

print(model.evaluate(X_test, y_test_cat))