from typing import List

def partition(nums:List,left,right):
    i=left
    j=right
    #choose the first item as pivot
    pivot=nums[left]
    while(i<j):
        #get item greater than pivot moving left to right
        while(i<right and nums[i]<=pivot):
            i+=1
        #get item smaller than pivot moving right to left
        while(j>left and nums[j]>pivot):
            j-=1
        #if left pointer is at left side of right pointer then swap item
        if i<j:
            nums[i],nums[j]=nums[j],nums[i]
    #if left pointer is at the right side of right pointer, swap right pointer and pivot
    nums[j],nums[left]=nums[left],nums[j]
    
    return j
        
def quicksort(nums:List,left,right):
    #To check if sub_array length is greater than 1
    if(left<right):
        pivot_pos=partition(nums,left,right)
        #left-subarray
        quicksort(nums,left,pivot_pos-1)
        #right-subarray
        quicksort(nums,pivot_pos+1,right)
    return nums

nums=[25,57,48,37,12,92,86,33]
print(quicksort(nums,0,len(nums)-1))