from math import ceil
def partition(nums):
    #Base Case
    if(len(nums)<=1):
        return nums
    
    split_idx=len(nums)//2
    left_part=partition(nums[0:split_idx])
    right_part=partition(nums[split_idx::])
    
    return merge(left_part,right_part)
    

def merge(left_part,right_part):
    new=[]
    i=0
    j=0
    while i<len(left_part) and j<len(right_part):
        if(left_part[i]<right_part[j]):
            new.append(left_part[i])
            i+=1
        else:
            new.append(right_part[j])
            j+=1
            
    new.extend(left_part[i:])
    new.extend(right_part[j:])
    return new
            
def mergeSort(nums): 
    sorted_list=partition(nums)
    return sorted_list
    
    
nums=[2,6,4,3,1,8,9,5]
print(mergeSort(nums))