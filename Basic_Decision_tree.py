# Importing the libraries
"""

import pandas as pd

"""# Importing the datasets"""

music_data = pd.read_csv('music.csv')

music_data

"""# Preparing the data"""

#input set
x = music_data.drop( columns=["genre"])
print(x)

y = music_data["genre"]
y

from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
model.fit(x,y)
music_data

predictions = model.predict([[21,1],[22,0]])
predictions

"""train_test_split with different train and test sets to check accurancy 

"""

from sklearn.model_selection import train_test_split
x_Train, x_Test, y_Train,y_Test = train_test_split(x, y, test_size = 0.2)

model = DecisionTreeClassifier()
model.fit(x_Train,y_Train)
predictions = model.predict(x_Test)
predictions

from sklearn.metrics import accuracy_score
score = accuracy_score(y_Test,predictions) 
score

from sklearn.model_selection import train_test_split
x_Train, x_Test, y_Train,y_Test = train_test_split(x, y, test_size = 0.5)

model = DecisionTreeClassifier()
model.fit(x_Train,y_Train)
predictions = model.predict(x_Test)

from sklearn.metrics import accuracy_score
score = accuracy_score(y_Test,predictions) 
score

from sklearn.model_selection import train_test_split
x_Train, x_Test, y_Train,y_Test = train_test_split(x, y, test_size = 0.8)

model = DecisionTreeClassifier()
model.fit(x_Train,y_Train)
predictions = model.predict(x_Test)

from sklearn.metrics import accuracy_score
score = accuracy_score(y_Test,predictions) 
score

from sklearn.model_selection import train_test_split
x_Train, x_Test, y_Train,y_Test = train_test_split(x, y, test_size = 0.2)

model = DecisionTreeClassifier()
model.fit(x_Train,y_Train)
predictions = model.predict(x_Test)

from sklearn.metrics import accuracy_score
score = accuracy_score(y_Test,predictions) 
score
