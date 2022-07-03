import string

def ispangram(sentence, alphabet=string.ascii_lowercase):
  if set(alphabet) <= set(sentence.lower()):
    print("Yes, its a pengram")
  else:
    print("No, its not a pengram")

ispangram(input('Enter any String: '))