import pandas as pd
import numpy
numpy.random.seed(0)

df = pd.read_csv('amazon_cells_labelled.txt', names=['sentence', 'label'], sep='\t')
print(df.head())

from sklearn.model_selection import train_test_split

sentences = df['sentence'].values
y = df['label'].values

sentences_train, sentences_test, y_train, y_test = train_test_split(sentences, y, test_size=0.25, random_state=1000)

from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer()
vectorizer.fit(sentences_train)

X_train = vectorizer.transform(sentences_train)
X_test = vectorizer.transform(sentences_test)
#print(X_train)

from sklearn.linear_model import LogisticRegression

lr = LogisticRegression()
lr.fit(X_train, y_train)
score = lr.score(X_test, y_test)
print(f'Accuracy of Logistic Regression Algorithm {score}')

from sklearn import neighbors

k = neighbors.KNeighborsClassifier(n_neighbors=5)
k.fit(X_train, y_train)
score = k.score(X_test, y_test)
print(f'Accuracy of KNN Algorithm {score}')

from sklearn.tree import DecisionTreeClassifier

dt = DecisionTreeClassifier(criterion='entropy')
dt.fit(X_train, y_train)
score = dt.score(X_test, y_test)
print(f'Accuracy of Decision Tree Algorithm {score}')

from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier()
rf.fit(X_train, y_train)
score = rf.score(X_test, y_test)
print(f'Accuracy of Random Forest Algorithm {score}')


