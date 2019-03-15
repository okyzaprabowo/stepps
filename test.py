import json
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from datetime import datetime
import os.path
from SWChecker.SWChecker import SWChecker
from OHelper.Prosa import Prosa
import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score, precision_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfTransformer
import pandas as pd
from collections import Counter
from modulenorm.modNormalize import normalize
from modulenorm.modTokenizing import tokenize
from rake_nltk import Rake

# create stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()

# Stopword Removal
stop_factory = StopWordRemoverFactory()
stopword = stop_factory.create_stop_word_remover()
data = stop_factory.get_stop_words()

# Standar Word Checker
dictFile = os.path.dirname(os.path.realpath(__file__))+"/improveDict.txt"
swChecker = SWChecker(dictFile)
prosaHelper = Prosa()
usenorm = normalize()

sentence = "q cinta lo tp lo kaga sejak weekend lalu" 
# text_norm = usenorm.enterNormalize(sentence) # normalisasi enter, 1 revw 1 baris
# # text_norm = usenorm.lowerNormalize(text_norm) # normalisasi huruf besar ke kecil
# text_norm = usenorm.repeatcharNormalize(text_norm) # normalisasi titik yang berulang
# text_norm = usenorm.linkNormalize(text_norm) # normalisasi link dalam text
# text_norm = usenorm.spacecharNormalize(text_norm) # normalisasi spasi karakter
# text_norm = usenorm.ellipsisNormalize(text_norm) # normalisasi elepsis (…)

# tok = tokenize() # panggil modul tokenisasi
# text_norm = tok.WordTokenize(text_norm) # pisah tiap kata pada kalimat

# text_norm = usenorm.spellNormalize(text_norm) # cek spell dari kata perkata
# text_norm = usenorm.wordcNormalize(text_norm,2) # menyambung kata (malam-malam) (param: textlist, jmlh_loop)
# text_norm = usenorm.stemmingNormalize(text_norm,'word') # mengubah ke bentuk kata dasar (text, type_data)

# text_norm = ' '.join(text_norm) # menggabung kalimat tokenize dengan separate spasi

# text_norm = usenorm.emoticonNormalize(text_norm) # menggabung struktur emoticon yang terpisah ([: - )] = [:-)])

# print(text_norm)

print("Raw -> ", sentence)
standardSentence = swChecker.check(sentence)
print("standardSentence -> ", standardSentence)
stopwordsSentence = stopword.remove(standardSentence)
print("stopwordsSentence -> ", stopwordsSentence)
normalizeSentence = prosaHelper.normalize(stopwordsSentence)
print("normalizeSentence -> " ,normalizeSentence)
stemmedSentence = stemmer.stem(normalizeSentence)
print("stemmedSentence -> ", stemmedSentence)

# df = pd.read_csv('/home/vagrant/code/InstaCrawler/stepps/NaiveBayes/alltab.tsv', sep='\t', lineterminator='\r')

# counter = Counter(df['label'].tolist())
# top_10_varieties = {i[0]: idx for idx, i in enumerate(counter.most_common(10))}
# df = df[df['label'].map(lambda x: x in top_10_varieties)]

# description_list = df['text'].tolist()
# varietal_list = [top_10_varieties[i] for i in df['label'].tolist()]
# varietal_list = np.array(varietal_list)

# count_vect = CountVectorizer()
# x_train_counts = count_vect.fit_transform(description_list)


# tfidf_transformer = TfidfTransformer()
# x_train_tfidf = tfidf_transformer.fit_transform(x_train_counts)

# train_x, test_x, train_y, test_y = train_test_split(x_train_tfidf, varietal_list, test_size=0.3)

# clf = LinearSVC().fit(train_x, train_y)
# y_score = clf.predict(test_x)

# print("Accuracy:", accuracy_score(test_y, y_score))
# print("Precision:", precision_score(test_y, y_score, average=None))
# # print(classification_report(test_y, y_score))
# print(confusion_matrix(test_y, y_score))

# # array prediction
# print(clf.predict(count_vect.transform(stemmedSentence.split())))

# r = Rake() # Uses stopwords for english from NLTK, and all puntuation characters.Please note that "hello" is not included in the list of stopwords.

# text='Hello World'
# a=r.extract_keywords_from_text(sentence)
# b=r.get_ranked_phrases()
# c=r.get_ranked_phrases_with_scores()
# print(b)
# print(c)
