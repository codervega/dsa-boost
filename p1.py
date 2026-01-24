# write code to move all the zeros to the ends of the end
def move(arr):
    j = 0
    
    for i in range(len(arr)):
        if(arr[i] != 0):
            
            arr[i],arr[j] = arr[j],arr[i]
            j+=1
   
    
arr = [1,3,0,0,9,0,5,2,1,4,2,0,5,8]
move(arr)
print(arr)