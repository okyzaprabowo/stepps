from subprocess import Popen, PIPE, STDOUT
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.template import Context, loader
from django.core.serializers.json import DjangoJSONEncoder
from django.forms.models import model_to_dict

import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score, precision_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfTransformer
import pandas as pd
from collections import Counter
import json
import simplejson
import datetime
 
from dashboard.models import *

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

def default(o):
  if type(o) is datetime.date or type(o) is datetime.datetime:
    return o.isoformat()

def result_sc(request):
    steppsResults = SteppsResult.objects.filter(label = 'sc')
    result_list = list(steppsResults.values('keyword', 'freq_high', 'px_high', 'freq_medium', 'px_medium', 'freq_low', 'px_low', 'label', 'created_at'))
    return HttpResponse(simplejson.dumps(result_list, use_decimal=True, default=default))

def result_t(request):
    steppsResults = SteppsResult.objects.filter(label = 't')
    result_list = list(steppsResults.values('keyword', 'freq_high', 'px_high', 'freq_medium', 'px_medium', 'freq_low', 'px_low', 'label', 'created_at'))
    return HttpResponse(simplejson.dumps(result_list, use_decimal=True, default=default))

def result_e(request):
    steppsResults = SteppsResult.objects.filter(label = 'e')
    result_list = list(steppsResults.values('keyword', 'freq_high', 'px_high', 'freq_medium', 'px_medium', 'freq_low', 'px_low', 'label', 'created_at'))
    return HttpResponse(simplejson.dumps(result_list, use_decimal=True, default=default))

def result_pu(request):
    steppsResults = SteppsResult.objects.filter(label = 'pu')
    result_list = list(steppsResults.values('keyword', 'freq_high', 'px_high', 'freq_medium', 'px_medium', 'freq_low', 'px_low', 'label', 'created_at'))
    return HttpResponse(simplejson.dumps(result_list, use_decimal=True, default=default))

def result_pr(request):
    steppsResults = SteppsResult.objects.filter(label = 'pr')
    result_list = list(steppsResults.values('keyword', 'freq_high', 'px_high', 'freq_medium', 'px_medium', 'freq_low', 'px_low', 'label', 'created_at'))
    return HttpResponse(simplejson.dumps(result_list, use_decimal=True, default=default))

def result_st(request):
    steppsResults = SteppsResult.objects.filter(label = 'st')
    result_list = list(steppsResults.values('keyword', 'freq_high', 'px_high', 'freq_medium', 'px_medium', 'freq_low', 'px_low', 'label', 'created_at'))
    return HttpResponse(simplejson.dumps(result_list, use_decimal=True, default=default))

def login(request):
    template = loader.get_template('login.html')
    return render(request, 'login.html')