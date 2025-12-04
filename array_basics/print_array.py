#Given an array, print all elements, and then print their sum.

def print_array():
  inp = int(input('Enter the size of array you want: '))
  arr=[]
  for i in range(inp):
    arr.append(int(input(f'ener element no.{i}: ')))
  sum=0
  try:
    for i in arr:
      print(i)
      sum += i
  except ValueError as e:
    print(f'{e} You were supposed to enter the  integer value')
    break
  print('Total of the integer of your elemens: ', sum)
  
print_array()