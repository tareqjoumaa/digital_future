def calculate_termination_benefits(salary, years_worked):
    if years_worked < 5:
        termination_benefits = (salary / 2) * years_worked
    else:
        termination_benefits = (salary / 2) * 5 
        termination_benefits += (salary) * (years_worked - 5) 
    
    return termination_benefits



def calculate_Indefinite_term_contract_benefits(salary, years_worked):
    if years_worked < 2:
        termination_benefits = 0
    elif years_worked < 5:
        termination_benefits = (salary / 2) * years_worked * 0.3333
    elif years_worked < 10:
        termination_benefits = (salary / 2) * 5 + (salary) * (years_worked - 5)
        termination_benefits = termination_benefits * 0.666
    else:
        termination_benefits = (salary / 2) * 5 + (salary) * (years_worked - 5)
    return termination_benefits
   
    
