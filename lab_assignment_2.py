#Project1
# For a given input string “Python is a case sensitive language”. Write python
# code for the following:
# a. Find the length of the input string.
# b. Reverse the order of the string in one line code.
# c. Using Slice function store “a case sensitive” in new string.
# d. Replace “a case sensitive” with “object oriented”.
# e. Find index of substring “a” in the given input string.
# f. Remove the white spaces from the given input string.

print("Q1:", ' \n')

string = input("Please Enter Any String:")
print(string)

#[a] (size of string)
print("a. Size of string is: ", len(string))

#[b] (reverse string)
b = string[::-1] # we can also type fantastic[0:35:-1]
print("b. The reversed string is: ", b)

#[c] (slicing string)
c = slice(10, 26)
print("c. String after slicing: ", string[c])

#[d] (replace substring)
d = string.replace('a case sensitive', 'object oriented')
print("d. Replacing substring: ", d)

#[e] (finding index of substring)
e = string.find('a') # we can also type e = string.index('a')
print("e. The index of 'a' is: ", e)

#[f] (removing spaces from the string)
f = string.replace(' ','')
print("f. Removing white spaces: ", f, end="\n")

#Project2
# Store your name, SID, department name and CGPA into different variables.
# With the help of String formatting print the following output:
# Hey, ABC Here!
# My SID is 2110XXXX
# I am from XYZ department and my CGPA is 9.9

print("Q2:", '\n')

Name='Vishwajeet'
SID='21102047'
Department='Civil'
CGPA=9.9
print("Hey, %s Here! \nMy SID is %s \nI am from %s department and my CGPA is %f." % (Name, SID, Department, CGPA), end='\n')

#Project3
# For a=56 and b=10 with the help of bitwise operators calculate the following:
# a. a&b
# b. a|b
# c. a^b
# d. Left shift both a and b with 2 bits.
# e. Right shift a with 2 bits and b with 4 bits.

print("Q3:", '\n')

a=56
b=10

print("a & b=", (a & b))
print("a | b=", (a | b))
print("a ^ b=", (a ^ b))
print("Left shift both a and b with 2 bits : a=",a<<2, "b=", b<<2)
print("Right shift a with 2 bits and b with 4 bits : a=", a>>2, "b=", b>>4, end='\n')

#Project4
# Write a python program to check if the word “name” is present in the string
# entered by the user (Print : “Yes” or “No”).

print("Q4:", '\n')

str = str(input("Enter the string:"))
print(str)
word = "name"

if word in str:
    print('Yes')
else:
    print("No")
print(end='\n')

#Project5
# For any three lengths, there is a simple test to see if it is possible to form a
# triangle. If any of the three lengths is greater than the sum of the other two,
# then you cannot form a triangle. Otherwise, Enter three sides of a triangle,
# converts them to integers, and to check whether the given input lengths can
# form a triangle or not (Print : “Yes” or “No”).[Don’t use if else here].

print("Q5:", '\n')

side_a = int(input("Enter the 1st side of the triangle : "))
side_b = int(input("Enter the 2nd side of the triangle : "))
side_c = int(input("Enter the 3rd side of the triangle : "))
# if side_a > side_b + side_c or side_b > side_a + side_c or side_c > side_a + side_b:
#     print('Yes')
# else:
#     print('No')
# print(end='\n')
triangle =(side_a,side_b,side_c)
triangle1 = sorted(triangle)
# check = triangle1[0] + triangle1[1] > triangle1[2]
while triangle1[0] + triangle1[1] > triangle1[2]:
    print('Yes')
    break
else:  print('No')
#Project6
# Given two numbers ‘a’ and b’. Write a program to count number of bits
# needed to be flipped to convert ‘a’ to ‘b’.

print("Q6:", '\n')

inpnum1 = int(input("Enter first number:"))
inpnum2 = int(input("Enter second number:"))

num = inpnum1 ^ inpnum2

i = 0
while (num != 0):
    num = num & (num - 1)
    i = i + 1
print("Num of bits needed to be flipped to convert a to b is:", i)