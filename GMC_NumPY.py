import numpy as np 


#getting the user input of data
n_students = int(input('Enter number of students:'))
n_subjects = int(input('Enter number of subjects:'))

#storing the data
marks= np.zeros((n_students,n_subjects))
names = []

#collecting the marks with loops
for i in range(n_students):
    names.append(input(f'Enter the name of the student {i+1}:'))

    for j in range(n_subjects):
        marks[i][j]=float(input(f'marks for subject {j+1}:'))


#calculating the total and percentages
totals = np.sum(marks,axis=1)
percentage = (totals/(n_subjects * 100)) * 100

# creating the loop 
def get_grade(pct):
    if pct >= 90 :return 'A+'
    elif pct >= 80: return 'A'
    elif pct >= 70: return 'B+'
    elif pct >= 60: return 'B'
    elif pct >= 50: return 'C'
    else:
        return 'F'

#displaying the results in table format
print(f'\n{'Name':<15} {'total_marks':>8} {'percentages':>12} {'Grade':>6}')
print('-' * 45)

for i in range(n_students):
    grade=get_grade(percentage[i])

    print(f'{names[i]:<15} {totals[i]:>8.0f} {percentage[i]:>11.2f}% {grade:>6}')