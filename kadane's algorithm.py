##KADANE'S ALGORITHM for MAXIMUM SUBARRAY SUM


import sys
def max_subarray_sum(arr,n): 
	
    max_sum_so_far = -sys.maxsize 
    curr_sum = 0
    idx,s=0,0
    for i in range(n): 
        curr_sum = curr_sum + arr[i] 
        if (max_sum_so_far < curr_sum): 
            max_sum_so_far = curr_sum
            idx=arr.index(arr[i])

        if curr_sum < 0: 
            curr_sum = 0
    for i in range(idx,-1,-1):
        if s==max_sum_so_far:
            break
        else:
            s+=arr[i]
            sidx=arr.index(arr[i])

    print("The maximum subarray sum is:- ",max_sum_so_far," and it lies in the range",sidx,"to", idx) 


arr = [-3, 10, 5, -20, 4, 11, -5, 7]
max_subarray_sum(arr,len(arr))


