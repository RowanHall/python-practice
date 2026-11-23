class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevmap = {} #map of prev visited num/indices in nums

        for i in range(0,len(nums),1):
            difference = target - nums[i]
            if difference in prevmap:
                return [prevmap[difference], i]
            prevmap[nums[i]] = i