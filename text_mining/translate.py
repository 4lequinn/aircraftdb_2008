from googletrans import Translator

translator = Translator()

print(translator.detect('Hola, esto es un texto de prueba'))


# Traducir lista de peliculas
movies = ['Las dos torres', 'El retorno del rey','El señor de los anillos','El hombre araña']
translations = []

for movie in movies:
    translation = translator.translate(movie,dest='ja')
    translations.append(translation)

for translation in translations:
    print(translation.origin, '->', translation.text)
