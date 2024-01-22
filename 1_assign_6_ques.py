'''6 WAP to create a list of 100 random numbers between 100 and 900. Count and print the:
(i) All odd numbers
(ii) All even numbers
(iii) All prime numbers
'''

import random

def prime_no(i):
    if(i<2):
        return False
    
    for num in range(2,int(i/2)):
        if i%num==0:
            return False
    return True


random_numbers = [random.randint(100,900) for _ in range(100)]
O=[i for i in random_numbers if i%2!=0]
E=[i for i in random_numbers if i%2==0]
P=[i for i in random_numbers if(prime_no(i))]    
count1 = len(E)
count2 = len(O)
count3 = len(P)

print(f'even no.s are\t\t {E} and \n counted as {count1}\n')
print(f'odd no.s are \t\t {O} and \n counted as {count2}\n')
print(f'prime no.s are \t\t {P} and \n counted as {count3}\n')


print(random_numbers)