#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

'''features_train = features_train[:len(features_train)/100]
labels_train = labels_train[:len(labels_train)/100]'''


#########################################################
### your code goes here ###
print("Support vector machine")
clf = SVC(kernel="rbf", C=11000)
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
acc = accuracy_score(labels_test, pred)
print(acc)

#count the number of chris(1) predicted mail
sums = (pred == 1).sum()
print(sums)

'''x=[10,26,50]
pred_l = []
for i in x:
    predx = clf.predict(features_test[i])
    pred_l.append(predx)'''



#########################################################
