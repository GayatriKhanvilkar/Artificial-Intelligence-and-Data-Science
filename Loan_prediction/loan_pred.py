import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('loands.csv')
# print(df.head())
# print(df.describe()) #summarry of data

df['LoanAmount'].hist(bins=50) #there are some extreme values
plt.show()

df['ApplicantIncome'].hist(bins=50) #there are some extreme values. Can find outliers.
plt.show()

#categorical value distribution

fig = plt.figure(figsize=(8,4))
ax1 = fig.add_subplot(121)
ax1.set_xlabel('Credit-History')
ax1.set_ylabel('Count of Applicants')
ax1.set_title('Applicants by credit history')
temp1.plot(kind='bar')

#data wrangling
#missing values
print(df.apply(lambda x : sum(x.isnull()), axis=0)) #no. of missing values in each column

df['LoanAmount'].fillna(df['LoanAmount'].mean(), inplace=True) #filling missing values
print(df.apply(lambda x : sum(x.isnull()), axis=0))
df['Credit_History'].fillna(df['Credit_History'].mean(), inplace=True)

#basic operation to know more about data
print(df.dtypes)
print(df.mean())

#example of dataframe concatination
#identical structure
# one = pd.DataFrame(np.random.randn(5, 4))
# print(one)
# two = pd.DataFrame(np.random.randn(5, 4))
# print(two)
# print(pd.concat([one, two])) #Concatinate 2 dataframes

# do not have identical structure
# left = pd.DataFrame({'key': ['foo', 'bar'], 'lval': [1, 2]})
# print(left)
# right = pd.DataFrame({'key': ['foo', 'bar', 'bar'], 'rval': [3, 4, 5]})
# print(right)
# print(pd.concat([left, right]))
# print(pd.merge(left, right, on='key')) #fun. based on key


from sklearn.model_selection import KFold

from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn import metrics

X = df.iloc[:, [8, 10]].values #credit hitory nd loan amount
Y = df.iloc[:, 12].values #loan status

#splitting dataset
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=0) #sratified random sampling

pd.DataFrame(X).fillna(0)
# pd.DataFrame(Y).fillna()
#Logistic Regression
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state=0)
classifier.fit(X_train, Y_train)

Y_pred = classifier.predict(X_test) #Predicting Test set
# print(Y_pred)

#performance of model
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_test, Y_pred)
print(cm)

from sklearn.metrics import accuracy_score
print(accuracy_score(Y_test, Y_pred))

from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier()
rf.fit(X_train, Y_train)
Y_pred_r = rf.predict(X_test)
cm = confusion_matrix(Y_test, Y_pred_r)
print(cm)
print(accuracy_score(Y_test, Y_pred_r))

from sklearn.tree import DecisionTreeClassifier, export_graphviz
dt = DecisionTreeClassifier()
dt.fit(X_train, Y_train)
Y_pred_d = dt.predict(X_test)
cm = confusion_matrix(Y_test, Y_pred_d)
print(cm)
print(accuracy_score(Y_test, Y_pred_d))

from sklearn.naive_bayes import GaussianNB
nb = GaussianNB()
nb.fit(X_train, Y_train)
Y_pred_n = nb.predict(X_test)
cm = confusion_matrix(Y_test, Y_pred_n)
print(cm)
print(accuracy_score(Y_test, Y_pred_n))


