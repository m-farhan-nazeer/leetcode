
# def findKthLargest( nums, k):
#     """
#     :type nums: List[int]
#     :type k: int
#     :rtype: int
#     """
#     for i in range(k):
#         max = float("-inf")
#         for j in range (len(nums)):
#             if nums[j]> max:
#                 max = nums[j]
#                 index = j
#         if i < k-1:
#             nums[index]= float("-inf")
#     print(nums)
#     return nums[index]

# print(findKthLargest([3,2,1,5,6,4],2))

def pivotIndex( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    sum = 0
    for val in nums:
        sum+=val
    j= len(nums)-1
    right = 0
    while j>=0:
        print("sum",sum-nums[j])
        print("right",right)
        if sum-nums[j]  == right:
            return j
        right+=nums[j]

        sum-=nums[j]
        
        j-=1
    return -1
print(pivotIndex([1,7,3,6,5,6]))

