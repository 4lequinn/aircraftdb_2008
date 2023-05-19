from dataframe import *
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import r2_score

X_train, X_test, y_train, y_test = train_test_split(X,Y,test_size=.2,random_state=10)

# Internal
internal_regression = linear_model.LinearRegression()
internal_regression.fit(X,Y)
internal_predict = internal_regression.predict(X)
print('Internal')
print('R2',r2_score(Y,internal_predict))


# External 
external_regression = linear_model.LinearRegression()
external_regression.fit(X_train,y_train)
external_predict = external_regression.predict(X_test)
print('External')
print('R2',r2_score(y_test,external_predict))