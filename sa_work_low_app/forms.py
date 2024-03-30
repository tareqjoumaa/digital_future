from django import forms

class FixedTermContractForm(forms.Form):
    REASONS_CHOICES = [
        ('expiration', 'Expiration of the contract'),
        ('employer_termination', 'Termination of the contract by the employer'),
        ('employer_termination_article_80', 'Termination of the contract by the employer in one of the cases mentioned in Article (80)'),
        ('compelling_reasons', 'Leaving work for compelling reasons'),
        ('marriage_or_birth', 'The worker terminates the employment contract within 6 months of marriage or 3 months of giving birth'),
        ('other_article_81', 'Leaving work for one of the cases mentioned in Article (81)'),
        ('other_cases', 'Termination of the contract by the worker or employer in cases other than those mentioned in Article (81)')
    ]
    salary = forms.FloatField(label='Salary')
    years_worked = forms.IntegerField(label='Years Worked')
    reason = forms.ChoiceField(label='Reason', choices=REASONS_CHOICES)



class IndefiniteTermContractForm(forms.Form):
    salary = forms.FloatField(label='Salary')
    years_worked = forms.FloatField(label='Years Worked')
    reason = forms.ChoiceField(choices=[
        ('expiration', 'The worker terminates the employment contract within 6 months of marriage or 3 months of giving birth'),
        ('employer_termination', 'Worker-employer agreement'),
        ('employer_termination_article_80', "Worker's resignation"),
        ('compelling_reasons', 'Leaving work without submitting resignation for cases other than those mentioned in Article (81)'),
        ('marriage_or_birth', 'Leaving work for one of the cases mentioned in Article (81)'),
        ('other_article_81', 'Leaving work for compelling reasons'),
        ('termination_by_employer', 'Termination of the contract by the employer'),
        ('other_cases', 'Termination of the contract by the employer in one of the cases mentioned in Article (80)'),
    ], label='Reason for termination')