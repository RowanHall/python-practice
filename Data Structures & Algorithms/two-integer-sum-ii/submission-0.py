class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        j = len(numbers)-1
        i = 0
        while (i!=j):
            sum_pointers = numbers[i] + numbers[j]
            if ( sum_pointers == target):
                return [i+1, j+1]
            elif (sum_pointers > target):
                j-=1
            else:
                i+=1
        return [-1,-1]