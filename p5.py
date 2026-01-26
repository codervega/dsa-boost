# finding the most consicutivce ones in an array 

def maxcountones(arr):
  count = 0
  max_count = 0
  for num in arr:
    if(num != 1 ):
      count = 0
    else:
      count += 1
      if(max_count < count):
        max_count = count
  return max_count
      


arr = [1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1]
max_ones = maxcountones(arr)
print("maximum consicutive ones are :" ,max_ones)
