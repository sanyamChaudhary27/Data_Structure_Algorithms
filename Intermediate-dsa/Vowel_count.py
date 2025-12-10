## COUNT THE NO. OF VOWELS IN A STRING 

def total_vowels(string):
  vowels = ['a', 'e', 'i', 'o', 'u']
  nots = ['and', 'in', 'us', 'ok']
  lst = list(string.split(" "))
  count = 0
  for i in lst:
    if i[0].lower() in vowels and i not in nots:
      count+=1
  return count
  
print(f'Toatal vowels: {total_vowels("Hello My name is Sanyam Chaudhary and I live in New Delhi with my parents and also with my sister")}')