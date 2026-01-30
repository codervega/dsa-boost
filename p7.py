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

# optimal approch using sliding window
#program 

def subarrlen(arr,k):
    max_len = 0
    sum = 0
    left = 0
    for i in range(len(arr)):
        sum = sum + arr[i]
        if(sum == k):
            max_len = max(max_len,i-left+1)
        while (sum > k and left <= i):
            sum = sum - arr[left]
            left = left + 1 
    
    return max_len
    
arr = [2,1,2,1,1,1,1,1]
print(subarrlen(arr,5))

