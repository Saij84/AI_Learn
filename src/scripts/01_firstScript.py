"""
Learn Python for Data Science #1
https://www.youtube.com/watch?v=T5pRlIbr6gg&list=PL2-dafEMk2A6QKz1mrk1uIGfHkC1zZ6UU
"""

from sklearn import tree
from sklearn import svm
from sklearn.metrics import accuracy_score

#Data: [height, weight, shoe size]
x = [[181,80,44], [177,70,43], [160,60,38], [154,54,37], [166,65,40],
     [190,90,47], [175,64,39], [177,70,40], [159,55,37], [171,75,42], [181,85,43]]

y = ['male', 'female', 'female', 'female', 'male', 'male', 'male', 'female', 'male', 'female', 'male']
z = ['male', 'female', 'female', 'female', 'male', 'female', 'male', 'female', 'male', 'male', 'male']


#Classefiers
clf_DTC = tree.DecisionTreeClassifier()
clf_SVM = svm.SVC(gamma='auto')

#Train model
clf_DTC = clf_DTC.fit(x, y)
clf_SVM = clf_SVM.fit(x, y)


#Test model
prediction_scores = {}

DTC_prediction = clf_DTC.predict(x)
DTC_score = accuracy_score(y, DTC_prediction)

print("DTC Prediction Score: {}".format(DTC_score*100))

"""
for data in x:
    prediction = clf_SVM.predict([data])
    print("SVM Prediction: {}".format(prediction))
"""