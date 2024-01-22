'''D is a dictionary defined as D= {1:'One', 2:'Two', 3:'Three', 4: “Four', 5:'Five'}.
(i) WAP to add new entry in D; key=6 and value is “Six'
(ii) WAP to remove key=2.
(iii) WAP to check if 6 key is present in D.
(iv) WAP to count the number of elements present in D.
(v) WAP to add all the values present D.
'''

D= {1:'One', 2:'Two', 3:'Three', 4: 'Four', 5:'Five'}

D[6]='Six'

print(D.keys())
print(D.values())


del D[1]

# to check key is present or not
print(4 in D)

print(D)

print(len(D))

sum='tan'
for value in D.values():
    sum = sum+value


print(sum)