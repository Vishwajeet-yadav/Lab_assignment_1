# Question 1
strg=input("Enter the string :")
print(strg[::-1])


# Question 2 (for loop)
x,y=(input("Enter the range of numbers: ").split())
num=int(input("Enter the number for divisibility: "))
x=int(x)
y=int(y)
for n in range(x,y+1):
    if n%num==0 :
        print(n)

# Question 2 (while loop)
# x=int(input("Enter the minimum value :"))
# y=int(input("Enter the maximum value: "))
# num=int(input("Enter the number for divisibility check :"))
# i=x
# while i<=y:
    # if i%num==0 :
        # print(i)
    # i+=1


# Question 3
s1=float(input("Enter the length of first side:"))
s2=float(input("Enter the length of second side:"))
s3=float(input("Enter the length of third side:"))
if s1+s2>s3 and s1+s3>s2 and s2+s3>s1 :
    s=(s1+s2+s3)/2
    area_triangle=(s*(s-s1)*(s-s2)*(s-s3))**(0.5)
    print(area_triangle)
else :
    print("Sides cannot form a triangle")


# Question 4
r1=int(input("Enter the no. of rows :"))
t=(r1//2)+1
l=r1//2
for i in range(1,t+1):
    for j in range(1,i+1):
        print("*",end="")
    print()
for q in range(l,0,-1):
    for r in range(q,0,-1):
        print("*",end="")
    print()


# Question 5
r2=int(input("Enter number of rows: "))
p=ord("A")
for rows in range(1,r2+1):
    for col in range(1,rows+1):
        print(chr(p),end="")
        p+=1
    print()


# Question 6
upper=int(input("Enter the maximum number of range: "))
lower=int(input("Enter the minimum number of range: "))
for n in range(lower,upper+1):
    for i in range(2,n):
        if n%i==0:
            break
    else :
        print(n)


# Question 7
accum=[]
for i in range(1,500):
    if i%7==0 and i%11==0:
        accum.append(i)
print("The numbers divisible by 11 and are multiple of 7 are :",accum)


# Question 8
pos=[]
neg=[]
odd=[]
even=[]
times={}
li=[]
for i in range(10):
    num=int(input("Enter the number: "))
    li.append(num)
    if num>0:
        pos.append(num)
    elif num<0 :
        neg.append(num)
    if num%2==0 :
        even.append(num)
    else :
        odd.append(num)
    if num not in times :
            times[num]=1
    else:
        times[num]+=1
print("Positive numbers are: ",pos)
print("Negative numbers are: ",neg)
print("Even numbers are: ",even)
print("Odd numbers are: ",odd)
print("Number of times each number occurs in the List",times)


# Question 9
n=int(input("Number of words: "))
list=[]
for i in range(n):
    word=input("Enter the word: ")
    list.append(word)
times1={}
for i in list :
    if i not in times1 :
        times1[i]=1
    else :
        times1[i]+=1
print("Number of occurences: ",times1)