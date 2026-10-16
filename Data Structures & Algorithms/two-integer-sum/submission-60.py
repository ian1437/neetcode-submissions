class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #building the dictionary
        seen = []
        for index, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return([seen.index(diff),index])
            else:
                seen.append(num)