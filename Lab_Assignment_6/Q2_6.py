def check_palindrome(string):
   if string==string[::-1]:
     return f"Yes, {string} is a palindrome"
   else:
     return f"No, {string} is not a palindrome"

word=input("Enter any string: ")
word=word.replace(" ","")

print(check_palindrome(word))