"""
@author: fred_
"""

import pandas as pd
base = pd.read_csv("glass.csv")

x = base.iloc[:, 0:9].values
y = base.iloc[:, [9]].values

import numpy as np
from sklearn.model_selection import StratifiedKFold
kfold = StratifiedKFold(n_splits=3, shuffle=True, random_state = 0)

from sklearn.naive_bayes import GaussianNB
resultadosNB = []
for indice_treino, indice_teste in kfold.split(x,np.ravel(y)):
    classificadorNB = GaussianNB()
    classificadorNB = classificadorNB.fit(x[indice_treino], y[indice_treino])

from sklearn.linear_model import LogisticRegression
resultadosRL = []
for indice_treino, indice_teste in kfold.split(x, np.ravel(y)):
    classificadorRL = LogisticRegression(max_iter = 2000)
    classificadorRL = classificadorRL.fit(x[indice_treino], y[indice_treino])


from sklearn.svm import SVC
resultadosSVM = []
for indice_treino, indice_teste in kfold.split(x, np.ravel(y)):
    classificadorSVM = SVC(kernel='linear')
    classificadorSVM= classificadorSVM.fit(x[indice_treino], y[indice_treino])


import pickle
pickle.dump(classificadorNB, open('naive_bayes_model.sav', 'wb'))
pickle.dump(classificadorRL, open('logistic_regression_model.sav', 'wb'))
pickle.dump(classificadorSVM, open('svm_model.sav', 'wb'))

















