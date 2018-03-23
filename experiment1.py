import numpy as np
from sklearn.datasets import load_iris
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict
from sklearn import metrics
import mex_framework


@mex_framework.author_name
def set_author_name():
    author = 'Igor Costa'
    return author

@mex_framework.author_email
def set_author_email():
    author_email = 'igor@igor.com'
    return author_email

@mex_framework.organization
def set_organization():
    organization = 'Instituto Militar de Engenharia'
    return organization

@mex_framework.hardware
def set_hardware_info():
    cache = "CACHE_3MB"
    cpu = "INTEL_COREI7"
    hd = "SSD"
    memory = "SIZE_16GB"
    os = "MacOS"
    return  {'cpu': cpu, 'memory': memory, 'hd': hd, 'cache': cache, 'os': os}


iris = load_iris()

X = iris.data
y = iris.target

@mex_framework.dataset_name
def set_dataset_name():
    name = 'Iris'
    URI = 'http://archive.ics.uci.edu/ml/datasets/Iris'
    description = 'This is perhaps the best known database to be found in the pattern recognition literature. ' \
                  'Fisher\'s paper is a classic in the field and is referenced frequently to this day. (See Duda & Hart, for example.) ' \
                  'The data set contains 3 classes of 50 instances each, where each class refers to a type of iris plant. One class is linearly ' \
                  'separable from the other 2; the latter are NOT linearly separable from each other.'
    return  {'name': name,'uri': URI,'description': description }


#train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)


clf = SVC(kernel='linear', C=1).fit(X_train,y_train)


y_pred = clf.predict(X_test)
#accuracies = metrics.accuracy_score(y_test, y_pred)

clf.fit(X,y)

new_data = [[1,2,3,4],
            [4,3,2,1],
            [4,2,1,3],
            [3,1,4,2],
            [2,2,4,4],
            ]

predictions  = clf.predict(new_data) # 0 - Setosa, 1 - Versicolor, 2 - Virginica
print predictions 

predicted = cross_val_predict(clf,X,y)
#accuracies = cross_val_score(clf, X, y)


accuracies = metrics.accuracy_score(y, predicted)
print accuracies


@mex_framework.algorithm
def set_algorithm():
    algorithmID = 'Support Vector Machine'
    algorithmClass = 'SupportVectorMachines'
    executionType = 'SINGLE'
    measure = 'ACCURACY'
    measureValue = accuracies
    phase = 'TRAIN'
    return { "algorithmClass": algorithmClass,
             "algorithmID": algorithmID,
             "executionType": executionType,
             "measure": measure,
             "measureValue": accuracies,
             "phase": phase}

@mex_framework.sampling_method
def set_sampling_method():
    aSM = 'CROSS_VALIDATION'
    return {'aSM': aSM, 'trainSize':70, 'testSize':30}



set_author_name()
set_author_email()
set_organization()
set_dataset_name()
set_hardware_info()
set_algorithm()
set_sampling_method()




