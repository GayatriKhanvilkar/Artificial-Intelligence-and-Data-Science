import pandas as pd

df = pd.read_csv(r"C:\Users\GAYATRI KHANVILKAR\PycharmProjects\Algorithms\BostonHousing\Train.csv")
# print(df.head())

columns = df.columns.values
# print(columns)

# Heatmap
import seaborn as sns
import  matplotlib.pyplot as plt
corr = df.corr()
# print(corr)

sns.heatmap(corr, annot=True) #to find Highly corelated attributes.
plt.show()

#Model 1
X = df[columns[0:14]] #Consider all attributes except ID.
Y = df[columns[-1]]
# print(X)
# print(Y)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, Y, train_size=0.8, random_state=1) # data splitting

from sklearn.linear_model import LinearRegression
lr = LinearRegression()  # object of model
lr.fit(x_train, y_train)
y_pred = lr.predict(x_test)
print(y_pred)

# from sklearn.metrics import accuracy_score
# accuracy = accuracy_score(y_test, y_pred)
# print(accuracy)

from  sklearn.metrics import mean_squared_error
print(mean_squared_error(y_test, y_pred))

from sklearn.metrics import r2_score
print(r2_score(y_test, y_pred))

#Model 2
x1 = df.iloc[:, [6, 13]] # Consider highly corelated with target attributes
# print(x)

x_train, x_test, y_train, y_test = train_test_split(x1, Y, train_size=0.8, random_state=1) # data splitting

lr = LinearRegression()  # object of model
lr.fit(x_train, y_train)
y_pred = lr.predict(x_test)

print(mean_squared_error(y_test, y_pred))
print(r2_score(y_test, y_pred))

#Model 3
x2 = df.iloc[:, [5, 8, 9, 13]] #Consider single attribute from pair of highly correlated attributes
# print(x2)
x_train, x_test, y_train, y_test = train_test_split(x2, Y, train_size=0.8, random_state=1) # data splitting

lr = LinearRegression()  # object of model
lr.fit(x_train, y_train)
y_pred = lr.predict(x_test)

print(mean_squared_error(y_test, y_pred))
print(r2_score(y_test, y_pred))
