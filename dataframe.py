import pandas as pd

path = './aircraft_db_2008.csv'
data = pd.read_csv(path)

df = data.dropna(subset=['ArrDelay'])
df = df.sample(frac=1).head(5000)

df = df.reset_index()

X = df[['AirTime','Distance','DepDelay']]
Y = df['ArrDelay']

