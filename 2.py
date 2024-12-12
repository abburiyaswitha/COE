basic_salary=int(input("Enter your basic salary: "))
if basic_salary < 1000:
    hra=int(basic_salary * 0.67)
    da=int(basic_salary * 0.73)
elif 10000 <= basic_salary <= 20000:
    hra=int(basic_salary * 0.69)
    da=int(basic_salary * 0.76)
elif basic_salary > 20000:
    hra=int(basic_salary * 0.73)
    da=int(basic_salary * 0.89)
gross_salary = basic_salary + hra + da
print("Your gross salary is:{gross_salary}")
