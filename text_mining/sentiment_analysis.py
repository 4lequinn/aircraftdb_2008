from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import RegexpTokenizer
import pandas as pd

list1 = ['Bueno','Malo','Bueno','Bueno','Malo']
list2 = [
    'Lo recomendaría a todos mis amigos',
    'El peor producto que he comprado nunca',
    'Me encanta, muy buen producto',
    'Excelente servicio, lo recomiendo',
    'No lo recomiendo para nada'
    ]

df = pd.DataFrame({'Sentimiento':list1,'Valoracion':list2})

#token = RegexpTokenizer(r'[a-zA-Z0-9]+')
#cv = CountVectorizer(lowercase=True, ngram_range=(1,2), tokenizer=token.tokenize)
#text_counts = cv.fit_transform(df['Valoracion'])


cv = CountVectorizer(lowercase=True, ngram_range=(1,2), token_pattern=r'[a-zA-Z0-9]+')
text_counts = cv.fit_transform(df['Valoracion'])

print(text_counts)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    text_counts,df['Sentimiento'],test_size=0.5,random_state=1
)

from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics

clf = MultinomialNB().fit(X_train,y_train)

predicted = clf.predict(X_test)

print('MultinomialNB Accuray',metrics.accuracy_score(y_test,predicted))

print(y_test)

print(predicted)
