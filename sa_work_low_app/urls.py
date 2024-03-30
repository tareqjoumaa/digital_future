from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('fixed_term/', views.fixed_term_contract, name='fixed_term_contract'),
    path('indefinite_term_contract/', views.calculate_indefinite_term_contract_benefits, name='calculate_indefinite_term_contract_benefits'), 
    path('result/<str:termination_benefits>/', views.result_page, name='result_page'),
]
