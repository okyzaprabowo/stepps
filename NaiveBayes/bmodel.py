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

df = pd.read_csv('/home/vagrant/code/InstaCrawler/stepps/NaiveBayes/alltab.tsv', sep='\t', lineterminator='\r')

counter = Counter(df['label'].tolist())
top_10_varieties = {i[0]: idx for idx, i in enumerate(counter.most_common(10))}
df = df[df['label'].map(lambda x: x in top_10_varieties)]

description_list = df['text'].tolist()
varietal_list = [top_10_varieties[i] for i in df['label'].tolist()]
varietal_list = np.array(varietal_list)

count_vect = CountVectorizer()
x_train_counts = count_vect.fit_transform(description_list)


tfidf_transformer = TfidfTransformer()
x_train_tfidf = tfidf_transformer.fit_transform(x_train_counts)

train_x, test_x, train_y, test_y = train_test_split(x_train_tfidf, varietal_list, test_size=0.3)

clf = LinearSVC().fit(train_x, train_y)
y_score = clf.predict(test_x)

print("Accuracy:", accuracy_score(test_y, y_score))
print("Precision:", precision_score(test_y, y_score, average=None))
# print(classification_report(test_y, y_score))
print(confusion_matrix(test_y, y_score))
s = "ready stock produk fossil authentic promo disc 50 produk dapat promonya hanya di koleksifossil authentic promo brakhir tinggal 09 12 2018"

# array prediction
print(clf.predict(count_vect.transform(s.split())))


