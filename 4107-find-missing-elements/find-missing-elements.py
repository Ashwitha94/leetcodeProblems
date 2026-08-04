class Solution(object):
    def findMissingElements(self, nums):
        ans = []
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] > 1:
                for j in range(nums[i] + 1, nums[i + 1]):
                    ans.append(j)
        return ans