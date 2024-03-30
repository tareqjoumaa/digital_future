from django.shortcuts import render, redirect
from .forms import FixedTermContractForm, IndefiniteTermContractForm
from .utils import calculate_termination_benefits, calculate_Indefinite_term_contract_benefits
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')


def fixed_term_contract(request):
    if request.method == 'POST':
        form = FixedTermContractForm(request.POST)
        if form.is_valid():
            salary = form.cleaned_data['salary']
            years_worked = form.cleaned_data['years_worked']
            reason = form.cleaned_data['reason']
            if reason in ['employer_termination_article_80', 'other_cases']:
                termination_benefits = 0
            else:
                termination_benefits = calculate_termination_benefits(salary, years_worked)
            return redirect('result_page', termination_benefits=termination_benefits)
    else:
        form = FixedTermContractForm()
    return render(request, 'fixed_term_contract.html', {'form': form})


def result_page(request, termination_benefits):
    termination_benefits = float(termination_benefits)
    return render(request, 'result_page.html', {'termination_benefits': termination_benefits})



def calculate_indefinite_term_contract_benefits(request):
    if request.method == 'POST':
        form = IndefiniteTermContractForm(request.POST)
        if form.is_valid():
            salary = form.cleaned_data['salary']
            years_worked = form.cleaned_data['years_worked']
            reason = form.cleaned_data['reason']
            if reason in ['compelling_reasons', 'other_cases']:
                termination_benefits = 0.0
            else:
                termination_benefits = calculate_Indefinite_term_contract_benefits(salary, years_worked)
            return render(request, 'result_page.html', {'termination_benefits': termination_benefits})
    else:
        form = IndefiniteTermContractForm()
    return render(request, 'indefinite_term_contract.html', {'form': form})