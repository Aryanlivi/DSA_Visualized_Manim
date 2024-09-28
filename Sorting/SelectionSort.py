

def SelectionSort(nums):
    for i in range(0,len(nums)):
        min_index=i
        for j in range(i+1,len(nums)):
            if(nums[j]<nums[min_index]):
                min_index=j
            
        if(min_index!=i):
            nums[min_index],nums[i]=nums[i],nums[min_index]
    return nums

def SelectionSort2(nums):
    for i in range(len(nums)-1,0,-1):
        max_index=0
        for j in range(1,i+1):
            if(nums[j]>nums[max_index]):
                max_index=j
        if(max_index!=i):
            nums[max_index],nums[i]=nums[i],nums[max_index]
    return nums

nums=[25,57,48,37,12,92,86,33]
print(SelectionSort(nums))