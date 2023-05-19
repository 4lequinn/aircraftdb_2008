from sklearn.neural_network import MLPClassifier
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler

from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import pandas as pd

path = './aircraft_db_2008.csv'
data = pd.read_csv(path)

df = data.dropna(subset=['AirTime','Distance','TaxiIn','TaxiOut','DepDelay'])
df = df.sample(frac=1).head(1000)

X =  df[['AirTime','Distance','TaxiIn','TaxiOut','DepDelay']]
Y = df['ArrDelay']

X_train, X_test, y_train, y_test = train_test_split(X,Y,test_size=.2,random_state=1)

scaler = StandardScaler()
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

clf = MLPRegressor(solver='lbfgs',alpha=1e-5,hidden_layer_sizes=(1000,),learning_rate='adaptive')
#clf = MLPRegressor(solver='lbfgs',alpha=1e-5,hidden_layer_sizes=(1000,),learning_rate='adaptive')
#clf = MLPRegressor(solver='lbfgs',alpha=1e-5,hidden_layer_sizes=(1000,),max_iter=1000000)
#clf = MLPRegressor(solver='lbfgs',alpha=1e-5,hidden_layer_sizes=(1000,),warm_start=True)
#clf = MLPRegressor(solver='lbfgs',alpha=1e-5,hidden_layer_sizes=(5,),activation='relu')

model = clf.fit(X_train,y_train)

predictions = model.predict(X_test)
print('R2 -',r2_score(y_test,predictions))