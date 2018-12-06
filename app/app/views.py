from subprocess import Popen, PIPE, STDOUT
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.template import Context, loader

import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score, precision_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfTransformer
import pandas as pd
from collections import Counter
 
def index(request):
    if request.method == 'GET':
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

        template = loader.get_template('index.html')
        results="49.06%"
        # Context is a normal Python dictionary whose keys can be accessed in the template index.html
        context = {
            'accuracy': n_right/float(len(test_y)) * 100,
            'precision': precision_score(test_y, y_score, average=None),
        }

        return render(request, 'index.html', context=context)

def result_sc(request):
    return JsonResponse([
        {
            "id": 1,
            "keyword": "Ciwidey",
            "freq_high": "10",
            "px_high": "0.03",
            "freq_medium": "1",
            "px_medium": "0.01",
            "freq_low": "0",
            "px_low": "0.00",
        },
        {
            "id": 2,
            "keyword": "Bandung",
            "freq_high": "10",
            "px_high": "0.03",
            "freq_medium": "1",
            "px_medium": "0.01",
            "freq_low": "0",
            "px_low": "0.00",
        },
        {
            "id": 3,
            "keyword": "Jakarta",
            "freq_high": "10",
            "px_high": "0.03",
            "freq_medium": "1",
            "px_medium": "0.01",
            "freq_low": "0",
            "px_low": "0.00",
        }
    ], safe=False)

def result_t(request):
    return JsonResponse([
        {
            "id": 1,
            "keyword": "Ciwidey",
            "freq_high": "10",
            "px_high": "0.03",
            "freq_medium": "1",
            "px_medium": "0.01",
            "freq_low": "0",
            "px_low": "0.00",
        },
        {
            "id": 2,
            "keyword": "Bandung",
            "freq_high": "10",
            "px_high": "0.03",
            "freq_medium": "1",
            "px_medium": "0.01",
            "freq_low": "0",
            "px_low": "0.00",
        },
        {
            "id": 3,
            "keyword": "Jakarta",
            "freq_high": "10",
            "px_high": "0.03",
            "freq_medium": "1",
            "px_medium": "0.01",
            "freq_low": "0",
            "px_low": "0.00",
        }
    ], safe=False)

def result_e(request):
    return JsonResponse([
        {
            "id": 1,
            "keyword": "Ciwidey",
            "freq_high": "10",
            "px_high": "0.03",
            "freq_medium": "1",
            "px_medium": "0.01",
            "freq_low": "0",
            "px_low": "0.00",
        },
        {
            "id": 2,
            "keyword": "Bandung",
            "freq_high": "10",
            "px_high": "0.03",
            "freq_medium": "1",
            "px_medium": "0.01",
            "freq_low": "0",
            "px_low": "0.00",
        },
        {
            "id": 3,
            "keyword": "Jakarta",
            "freq_high": "10",
            "px_high": "0.03",
            "freq_medium": "1",
            "px_medium": "0.01",
            "freq_low": "0",
            "px_low": "0.00",
        }
    ], safe=False)

def result_pu(request):
    return JsonResponse([
        {
            "id": 1,
            "keyword": "Prabowo",
            "freq_high": "10",
            "px_high": "0.03",
            "freq_medium": "1",
            "px_medium": "0.01",
            "freq_low": "0",
            "px_low": "0.00",
        },
        {
            "id": 2,
            "keyword": "Jokowi",
            "freq_high": "10",
            "px_high": "0.03",
            "freq_medium": "1",
            "px_medium": "0.01",
            "freq_low": "0",
            "px_low": "0.00",
        },
        {
            "id": 3,
            "keyword": "Ban Kie Mon",
            "freq_high": "10",
            "px_high": "0.03",
            "freq_medium": "1",
            "px_medium": "0.01",
            "freq_low": "0",
            "px_low": "0.00",
        }
    ], safe=False)

def result_pr(request):
    return JsonResponse([
        {
            "id": 1,
            "keyword": "Ciwidey",
            "freq_high": "10",
            "px_high": "0.03",
            "freq_medium": "1",
            "px_medium": "0.01",
            "freq_low": "0",
            "px_low": "0.00",
        },
        {
            "id": 2,
            "keyword": "Bandung",
            "freq_high": "10",
            "px_high": "0.03",
            "freq_medium": "1",
            "px_medium": "0.01",
            "freq_low": "0",
            "px_low": "0.00",
        },
        {
            "id": 3,
            "keyword": "Jakarta",
            "freq_high": "10",
            "px_high": "0.03",
            "freq_medium": "1",
            "px_medium": "0.01",
            "freq_low": "0",
            "px_low": "0.00",
        }
    ], safe=False)

def result_st(request):
    return JsonResponse([
        {
            "id": 1,
            "keyword": "Ciwidey",
            "freq_high": "10",
            "px_high": "0.03",
            "freq_medium": "1",
            "px_medium": "0.01",
            "freq_low": "0",
            "px_low": "0.00",
        },
        {
            "id": 2,
            "keyword": "Bandung",
            "freq_high": "10",
            "px_high": "0.03",
            "freq_medium": "1",
            "px_medium": "0.01",
            "freq_low": "0",
            "px_low": "0.00",
        },
        {
            "id": 3,
            "keyword": "Jakarta",
            "freq_high": "10",
            "px_high": "0.03",
            "freq_medium": "1",
            "px_medium": "0.01",
            "freq_low": "0",
            "px_low": "0.00",
        }
    ], safe=False)

def login(request):
    template = loader.get_template('login.html')
    return render(request, 'login.html')