import nltk
from nltk.corpus import stopwords

print('-----------------')
print('STOPWORDS: (nltk)')
print('-----------------')

# Download der Liste
nltk.download('stopwords')

# In den Stopword kann für diverse Sprachen eine Liste erstellt werden
stopwords_englisch = stopwords.words('english')
stopwords_german = stopwords.words('german')
# usw.
print('')
print('Stopwords englisch:', stopwords_englisch)
print('')
print('Stopwords german:', stopwords_german)

print('-----------------')
print('')
search_string = input('Exit => press any button')

