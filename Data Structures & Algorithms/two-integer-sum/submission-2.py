class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevhash = {}
        
        for i in range(0,len(nums),1):
            difference = target - nums[i]
            if difference in prevhash:
                j = prevhash[difference]
                return [j, i]
            prevhash[nums[i]] = i
