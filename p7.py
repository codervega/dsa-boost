# program to find length of maxium sub array 


def longestsubarray(arr,k):
    max_len = 0
    
    for i in range(len(arr)):
        sumsubarr = 0
        for j in range(i,len(arr)):
            sumsubarr +=arr[j]
            if(sumsubarr == k):
                max_len = max(max_len,j-i+1)
                
    return max_len
            


arr = [1,2,1,4]
k = 4
print(longestsubarray(arr,k))

