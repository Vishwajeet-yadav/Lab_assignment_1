print("Q1:")
'''Write a Python program to find average of three numbers entered by the user'''

a = int(input("First Number: "))

b = int(input("Second number: "))

c = int(input("Third number: "))

average = (a+b+c)/3

print("The average of these numbers is", average)

print("Q2:")
"""Write a python program to compute a person's income tax. Assume following
tax laws:
• All taxpayers are charged a flat tax rate of 20%.
• All taxpayers are allowed a $10,000 standard deduction.
• For each dependent, a taxpayer is allowed an additional $3,000 deduction.
• Gross income must be entered to the nearest penny.
Gross Income and the number of dependents must be asked from the user.
Hint:
Taxable income = Gross Income - Standard deduction - (Dependent deduction
* No. of dependents)
Tax = Taxable Income * Tax Rate"""

Gross_Income = float(input("Gross Income = "))
Number_of_dependents = int(input("Number of dependents = "))
Standard_deduction = 10000
Dependent_deduction = 3000

Taxable_income = Gross_Income - Standard_deduction - (Dependent_deduction * Number_of_dependents)

Tax_Rate = 20/100

Tax = Taxable_income * float(Tax_Rate)

print("Person's Income Tax =", Tax)

print("Q3:")
"""Write a python program to store different data type values into a list.
(For an example: Student [SID, Name, Gender, Course Name, CGPA]).
Note: Use Gender values: ‘F’, ‘M’, ‘U’ (For Unknown).
CGPA should have floating type values (example: 7.5)"""

SID = int(input("SID:"))
Name = input("Name:")
Gender = input("Gender:")
Course_Name = input("Course Name:")
CGPA = float(input("CGPA:"))

Student = [SID, Name, Gender, Course_Name, CGPA]

print("Student" + str(Student), '\n')

print("Q4:")
"""Write a python program to enter marks of 5 students into a list and display
them in sorted manner."""

student1 = float(input("Enter the marks of Student 1:"))
student2 = float(input("Enter the marks of Student 2:"))
student3 = float(input("Enter the marks of Student 3:"))
student4 = float(input("Enter the marks of Student 4:"))
student5 = float(input("Enter the marks of Student 5:"))

marks = [student1, student2, student3, student4, student5]
marks.sort()
print(marks,'\n')


print("Q5:")
'''List: color ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
a. Write a Python program to print a specified list after removing 4th element.
Expected output: color [Red', 'Green', 'White', 'Pink', 'Yellow']
b. Remove ‘Black’ and ‘Pink’ from the list and replace them with ‘Purple’.
Do that in one line code.'''

color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print("The provided list is ", color, '\n')

# removing the 4th term and returning modified list
color.pop(3)
print(" The modified list a is ", color)

# replacing 'Black' and 'Pink' with 'Purple'
color2 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color2[3:5] = ['Purple']
print("The modified list b is  ", color2)
