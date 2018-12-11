from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('dashboard/', views.index, name='index'),
    path('sc/get/', views.result_sc, name='result_sc'),
    path('t/get/', views.result_t, name='result_t'),
    path('e/get/', views.result_e, name='result_e'),
    path('pu/get/', views.result_pu, name='result_pu'),
    path('pr/get/', views.result_pr, name='result_pr'),
    path('st/get/', views.result_st, name='result_st'),
    path('calculate/', views.calculate_result, name='calculate_result'),
]