from dataframe import *
from sklearn.model_selection import KFold
from sklearn.metrics import r2_score
import numpy as np
from sklearn import linear_model

kf = KFold(n_splits=10,shuffle=True)

print(kf.get_n_splits(X))

regression = linear_model.LinearRegression()

results = []

for train_index, test_index in kf.split(X):
    X_train, X_test = X.loc[train_index,], X.loc[test_index,]
    y_train, y_test = Y[train_index], Y[test_index]
    regression.fit(X_train,y_train)
    predicts = regression.predict(X_test)
    print('R2',r2_score(y_test,predicts))
    results.append(r2_score(y_test,predicts))
print('R2 Medio',np.mean(results))