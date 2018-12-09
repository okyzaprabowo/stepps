from subprocess import Popen, PIPE, STDOUT
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.template import Context, loader
from django.core.serializers.json import DjangoJSONEncoder
from django.forms.models import model_to_dict
from collections import Counter
import json
import simplejson
import datetime
 
from dashboard.models import *

def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')

def default(o):
  if type(o) is datetime.date or type(o) is datetime.datetime:
    return o.isoformat()

def result_sc(request):
    steppsResults = SteppsResult.objects.filter(label = 'sc')[:5]
    result_list = list(steppsResults.values('keyword', 'freq_high', 'px_high', 'freq_medium', 'px_medium', 'freq_low', 'px_low', 'label', 'created_at'))
    return HttpResponse(simplejson.dumps(result_list, use_decimal=True, default=default))

def result_t(request):
    steppsResults = SteppsResult.objects.filter(label = 't')[:5]
    result_list = list(steppsResults.values('keyword', 'freq_high', 'px_high', 'freq_medium', 'px_medium', 'freq_low', 'px_low', 'label', 'created_at'))
    return HttpResponse(simplejson.dumps(result_list, use_decimal=True, default=default))

def result_e(request):
    steppsResults = SteppsResult.objects.filter(label = 'e')[:5]
    result_list = list(steppsResults.values('keyword', 'freq_high', 'px_high', 'freq_medium', 'px_medium', 'freq_low', 'px_low', 'label', 'created_at'))
    return HttpResponse(simplejson.dumps(result_list, use_decimal=True, default=default))

def result_pu(request):
    steppsResults = SteppsResult.objects.filter(label = 'pu')[:5]
    result_list = list(steppsResults.values('keyword', 'freq_high', 'px_high', 'freq_medium', 'px_medium', 'freq_low', 'px_low', 'label', 'created_at'))
    return HttpResponse(simplejson.dumps(result_list, use_decimal=True, default=default))

def result_pr(request):
    steppsResults = SteppsResult.objects.filter(label = 'pr')[:5]
    result_list = list(steppsResults.values('keyword', 'freq_high', 'px_high', 'freq_medium', 'px_medium', 'freq_low', 'px_low', 'label', 'created_at'))
    return HttpResponse(simplejson.dumps(result_list, use_decimal=True, default=default))

def result_st(request):
    steppsResults = SteppsResult.objects.filter(label = 'st')
    result_list = list(steppsResults.values('keyword', 'freq_high', 'px_high', 'freq_medium', 'px_medium', 'freq_low', 'px_low', 'label', 'created_at'))
    return HttpResponse(simplejson.dumps(result_list, use_decimal=True, default=default))

def login(request):
    template = loader.get_template('login.html')
    return render(request, 'login.html')

def calculate_result(request):
    # Select ALL Classified KEYWORDS
    keywords = ClassificationResult.objects.all()
    try:
        for key in keywords:
            # print(key.keyword)
            h_keyword_count = Crawling.objects.filter(caption_text__icontains=key.keyword, engagement__icontains='H').count()
            h_count = Crawling.objects.filter(engagement__icontains='H').count()
            if(h_keyword_count > 0):
                h_prob = h_keyword_count / h_count
            else:
                h_prob = 0
            m_keyword_count = Crawling.objects.filter(caption_text__icontains=key.keyword, engagement__icontains='M').count()
            m_count = Crawling.objects.filter(engagement__icontains='M').count()
            if(m_keyword_count > 0):
                m_prob = m_keyword_count / m_count
            else:
                m_prob = 0
            l_keyword_count = Crawling.objects.filter(caption_text__icontains=key.keyword, engagement__icontains='L').count()
            l_count = Crawling.objects.filter(engagement__icontains='L').count()
            if(l_keyword_count > 0):
                l_prob = l_keyword_count / l_count
            else:
                l_prob = 0
            stepps_result = {'keyword':key.keyword, 'freq_high':h_keyword_count, 'px_high':h_prob, 'freq_medium': m_keyword_count, 'px_medium':m_prob, 'freq_low':l_keyword_count, 'px_low':l_prob, 'label':key.label}
            print(stepps_result)
            stepps_object = SteppsResult(
                keyword = key.keyword,
                freq_high = h_keyword_count,
                px_high = h_prob,
                freq_medium = m_keyword_count,
                px_medium = m_prob,
                freq_low = l_keyword_count,
                px_low = l_prob,
                label = key.label
            )
            stepps_object.save()

    except Exception as e: print(e)
    return HttpResponse("{'response' :200}")

    