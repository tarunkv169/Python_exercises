''' 1 A class with 10 students wants to produce some information from the results of the four
standard tests in Maths, Science, English and IT. Each test is out of 100 marks. The
information output should be the highest, lowest and average mark for each test and the
highest, lowest and average mark overall. Write a program in Python to complete this task. '''


# def information_output(all_score):
#     highest = max(all_score)
#     lowest = min(all_score)
#     average = sum(all_score)/len(all_score)

#     return highest,lowest,average

# def main():
#     no_of_students = int(input('enter the no. of students '))
#     subjects = ['math','sci','eng','IT']
#     all_score = {subject:[] for subject in subjects}

#     for student in range(1,no_of_students+1):
#         name = input(f'\n\nenter the name of [{student}] student  ')
#         print(f'\nenter the marks of {name} in each subject---:--')
#         for subject in subjects:
#             marks = int(input(f'\t\tenter the marks in {subject}: '))
#             all_score[subject].append(marks)

#     overall = []  
#     for subject in subjects:
#         highest,lowest,average = information_output(all_score[subject])
        
#         print(f'\nhighest marks in {subject} is {highest} \t lowest marks in {subject} is {lowest} \t average marks in {subject} is {average} ')
        
#         overall.extend(all_score[subject])

#     overall_highest,overall_lowest,overall_average = information_output(overall)
#     print(f'\noverall_highest marks in {subject} is {overall_highest} \t overall_lowest marks in {subject} is {overall_lowest} \t overall_average marks in {subject} is {overall_average} ')

    

# if __name__=='__main__':
#     main()






def info_output(all_marks):
    highest = max(all_marks)
    lowest = min(all_marks)
    average = sum(all_marks)/len(all_marks)

    return highest,lowest,average

def main():
    no_of_students= int(input('enter the total no. of students '))
    subjects = ['eng','math','sci','IT']
    all_marks = {subject:[] for subject in subjects}

    for student in range(1,no_of_students+1):
        name = input(f'enter the name of {student}\'s student: ')
        print(f'\tenter the marks of {name} in each subject ')
        for subject in subjects:
            marks =int(input(f'\t\tenter the marks in {subject}: '))
            all_marks[subject].append(marks)

    overall=[]
    for subject in subjects:
        highest,lowest,average = info_output(all_marks[subject])
        print(f'highest marks in {subject} is {highest} \t  lowest marks in {subject} is {lowest} \t average marks in {subject} is {average} ')
        overall.extend(all_marks[subject])

    highest,lowest,average = info_output(overall)
    print(f'higest of overall is {highest} \tlowest of overall is {lowest} \t average of overall is {average}')



if __name__ == '__main__':
    main()
 