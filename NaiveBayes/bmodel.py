# from sklearn.metrics import accuracy_score, precision_score, classification_report, confusion_matrix
# print "Accuracy:", accuracy_score(y_test, preds)
# print "Precision:", precision_score(y_test, preds)
# print classification_report(y_test, preds)
# print confusion_matrix(y_test, preds)

import numpy as np
from sklearn.naive_bayes import MultinomialNB
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

clf = MultinomialNB().fit(train_x, train_y)
y_score = clf.predict(test_x)

n_right = 0
for i in range(len(y_score)):
    if y_score[i] == test_y[i]:
        n_right += 1

# print("Accuracy: %.2f%%" % ((n_right/float(len(test_y)) * 100)))
print("Accuracy:", accuracy_score(test_y, y_score))
# print("Precision:", precision_score(test_y, y_score, average=None))
# print(classification_report(test_y, y_score))
# print(confusion_matrix(test_y, y_score))