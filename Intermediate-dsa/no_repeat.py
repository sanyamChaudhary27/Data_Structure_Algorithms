##    RETURN THE LONGEST LENGTH OF A STRING WITH NO REPEAT

def no_repeaat(li):
  last_seen ={}
  left_pointer = 0
  max_length=0
  for right, char in enumerate(li):
    if char in last_seen and last_seen[char]>=left_pointer:
      left_pointer = last_seen[char]
    last_seen[char]=right
    current_window = right-left_pointer+1 
    max_length = max(max_length, current_window)
  return max_length
  
print(no_repeaat('ajKiraatMzaHusnKaAankhonSeLijiye'))