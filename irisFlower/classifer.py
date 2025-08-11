import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("IRIS.csv")


"""
print(data.head())
print(data.isna().sum())
print(data.shape)
"""

X = data.iloc[:,:-1].values
y = data.iloc[:,-1].values


#Setting up train and test sets
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,random_state=1)

#Scaling data with standardscaler
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()

X_train = ss.fit_transform(X_train)
X_test = ss.transform(X_test)

#Importing the classifier and training the dataset
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=100, max_depth=10, min_samples_split=2, random_state=42)

classifier.fit(X_train,y_train)

y_prediction = classifier.predict(X_test)

#print(y_prediction)



#Checking the accuracy of the trained model
from sklearn.metrics import accuracy_score,confusion_matrix

confus_matrix = confusion_matrix(y_test,y_prediction)
ac_score = accuracy_score(y_test,y_prediction)

print(confus_matrix)
print(ac_score)


#Data visualization
print(data.columns)
ax = sns.scatterplot(data=data,x="petal_length",y="petal_width",hue="species")
ax.set_title("Petal Length & Width")
plt.show()