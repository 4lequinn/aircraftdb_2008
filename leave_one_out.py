from dataframe import *
from sklearn.model_selection import train_test_split, LeaveOneOut
from sklearn import linear_model


X_train, X_test, y_train, y_test = train_test_split(X,Y,test_size=.2,random_state=1)

regression = linear_model.LinearRegression()

loo = LeaveOneOut()

for train_index, test_index in loo.split(X):
    X_train, X_test = X.loc[train_index,], X.loc[test_index,]
    y_train, y_test = Y[train_index], Y[test_index]
    regression.fit(X_train,y_train)
    predicts = regression.predict(X_test)
    print('Error -',(y_test - predicts[0])**2)

