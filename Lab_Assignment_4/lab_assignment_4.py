#Q.1
marks=float(input("Enter Marks: "))
if(marks<25):
    print(" Grade F ")
elif(marks>=25 and marks<45):
    print(" Grade E ")
elif(marks>=45 and marks<50):
    print(" Grade D ")
elif(marks>=50 and marks<60):
    print(" Grade C ")
elif(marks>=60 and marks<80):
    print(" Grade B ")
elif(marks>=80 ):   
    print(" Grade A ")
else:
    print(" ERROR ")


#Q.2
year = int(input("Enter a year: "))

if year % 4 == 0 :
    print(year ,"is a Leap Year")
elif year % 100 == 0 :
    print(year ,"is not a Leap Year")
elif year % 400 == 0 :
    print(year ,"is a Leap Year")
else :
    print(" ERROR ")


#Q.3
import random
for i in range(10):
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    print(f"Question {i+1}:",end="")
    user_output = int(input(f"{num1}X{num2}="))
    if user_output == (num1*num2):
        print("Right!")
    else:
        print(f"Wrong.The right answer is {num1*num2}.")


#Q.4
x=200
for candies in range(x):

    if candies % 5 == 2:
       if candies % 6 == 3:
          if candies % 7 == 2:
             print(candies, 'candies are in the bowl!')
             break