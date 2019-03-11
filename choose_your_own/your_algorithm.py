#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.metrics import accuracy_score

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

## K Nearest Neighbors 
knnclf = KNeighborsClassifier()
knnclf.fit(features_train, labels_train)
pred = knnclf.predict(features_test)
knnacc = accuracy_score(labels_test, pred)
print(knnacc)
prettyPicture(knnclf, features_test, pred)
# accuracy = 0.92

rfclf = RandomForestClassifier()
rfclf.fit(features_train, labels_train)
pred = rfclf.predict(features_test)
rfacc = accuracy_score(labels_test, pred)
print(rfacc)
prettyPicture(rfclf, features_test, pred)
#accuracy = 0.92

abclf = AdaBoostClassifier()
abclf.fit(features_train, labels_train)
pred = abclf.predict(features_test)
abacc = accuracy_score(labels_test, pred)
print(abacc)
prettyPicture(abclf, features_test, pred)
#accuracy =0.924



try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
