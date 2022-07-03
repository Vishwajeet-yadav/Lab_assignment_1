def fun(num):
   c=0
   for i in range (1,num):
       if num%i==0:
           c+=i
   if c==num:
       print(f"Yes, {num} is a perfect number")
   else:
        print(f"No, {num} is not a perfect number")
num=int(input("Enter the number: "))
fun(num)
