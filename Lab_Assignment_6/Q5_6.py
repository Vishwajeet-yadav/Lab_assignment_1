def fun(string):
 string1=string.split('-')
 # print(string1)
 string2 = sorted(string1)
 # print(string2)
 string3 = ('-').join(map(str,string2))
 print(string3)

s=input("Enter any hyphen seperated sequence: ")
fun(s)