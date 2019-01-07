"""
Learn Python for Data Science #1
https://www.youtube.com/watch?v=T5pRlIbr6gg&list=PL2-dafEMk2A6QKz1mrk1uIGfHkC1zZ6UU
"""

from sklearn import tree
from sklearn.svm import SVC
from sklearn.neighbors.nearest_centroid import NearestCentroid
from sklearn.ensemble import RandomForestClassifier
import numpy as np

from sklearn.metrics import accuracy_score

#Data: [height, weight, shoe size]
x = [[181,80,44], [177,70,43], [160,60,38], [154,54,37], [166,65,40],
     [190,90,47], [175,64,39], [177,70,40], [159,55,37], [171,75,42], [181,85,43]]

y = ['male', 'female', 'female', 'female', 'male', 'male', 'male', 'female', 'male', 'female', 'male']

#Classefiers
clf_DTC = tree.DecisionTreeClassifier()
clf_SVM = SVC()
clf_NC = NearestCentroid()
clf_RFC = RandomForestClassifier()

#Train model
clf_DTC.fit(x, y)
clf_SVM.fit(x, y)
clf_NC.fit(x, y)
clf_RFC.fit(x, y)


#Test model
prediction_scores = {}

DTC_prediction = clf_DTC.predict(x)
DTC_score = accuracy_score(y, DTC_prediction)*100
print("DTC Prediction Score: {}".format(DTC_score))

SVM_prediction = clf_SVM.predict(x)
SVM_score = accuracy_score(y, SVM_prediction)*100
print("SVM Prediction Score: {}".format(SVM_score))

NC_predictions = clf_NC.predict(x)
NC_score = accuracy_score(y, NC_predictions)*100
print("NC Prediction Score: {}".format(NC_score))

RFC_predictions = clf_RFC.predict(x)
RFC_score = accuracy_score(y, RFC_predictions)*100
print("RFC Predcition Score: {}".format(RFC_score))

bestModel = np.argmax([SVM_prediction, NC_predictions, RFC_predictions])
print(bestModel)