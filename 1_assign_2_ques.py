'''Write a Python Program to input basic salary of an employee and calculate its Gross salary
according to following: 
Basic Salary <= 10000 : HRA = 20%, DA = 80% 
Basic Salary <=20000 : HRA = 25%, DA = 90% 
Basic Salary > 20000 : HRA = 30%, DA = 95%. '''


def calculate(basic):

    if(basic<=10000):
        hra = 10000*(20/100)
        da = 10000*(80/100)
    elif(basic<=20000):
        hra = 10000*(25/100)
        da = 10000*(90/100)
    else:
        hra = 10000*(30/100)
        da = 10000*(95/100)

    return hra,da


def main():

    basic_salary = float(input('enter the basic salary '))

    hra,da = calculate(basic_salary)

    gross_salary = basic_salary + hra + da

    print(f'gross salary is {gross_salary}')

if __name__ == '__main__':
    main()





