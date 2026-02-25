salary = int(input("enter your salary :"))
if salary <30000:
    tax_on_salary = salary *(5/100)
if 30000< salary <70000:
    tax_on_salary = salary *(15/100)
if salary >70000:
    tax_on_salary = salary *(25/100)    

print(f"on the {salary} salary the tax amount is {tax_on_salary} only /-")