import math
def fun(x):
 for j in range (1,x+1):
   for i in range (0,j):
    print(math.comb(j-1,i), end=(' '))
   print(end=('\n'))
r = int(input("Enter the number of rows: "))
fun(r)