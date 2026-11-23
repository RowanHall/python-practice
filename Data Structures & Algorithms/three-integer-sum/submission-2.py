class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        target = 0
        n = len(nums)
        for i in range(n):
            if nums[i]>target:
                break
            if (i>0 and nums[i] == nums[i-1]):
                continue
            j = i+1
            k = n-1
            while (j<k):
                sum_ptrs = nums[i] + nums[j] + nums[k]
                if (sum_ptrs == target):
                    res_list = [nums[i], nums[j], nums[k]]
                    result.append(res_list)
                    k -= 1
                    j += 1

                    while (j<k and nums[j] == nums[j-1]):
                        j+=1
                    while j<k and nums[k] == nums[k+1]:
                        k-=1
                elif (sum_ptrs > target):
                    k -= 1
                else:
                    j += 1

        return result