import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import r2_score

path = './aircraft_db_2008.csv'
data = pd.read_csv(path)

df = data.dropna(subset=['ArrDelay'])
df = df.sample(frac=1).head(1000)

X = df[['AirTime','Distance','DepDelay']]
Y = df['ArrDelay']



