## find max of an array 

def max(arr: list):
  try:
    high = arr[0]
  except IndexError:
    raise IndexError('The array can not be empty')
  for i in arr:
    if i>=high:
      high = i
  
  return high
  
arr = [-1, -2, -3, -4, -5]
print(max(arr))