class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}
        result = []
        for i in range(len(nums)) :
            compliment = target - nums[i]
            if compliment in count:
                a,b = i,count[compliment]

            count[nums[i]] = i 
        if a > b:
            result.append(b)
            result.append(a)
        else:
            result.append(a)
            result.append(b)

        
        return result