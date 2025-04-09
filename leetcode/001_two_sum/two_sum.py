class Solution:
    def twoSum(nums: list[int], target: int) -> list[int]:
        # print(nums, target)
        for num in nums:
            otherNum = target - num
            if otherNum in nums and nums.index(num) != nums.index(otherNum):
                # print(nums.index(num), nums.index(otherNum))
                return nums.index(num), nums.index(otherNum)
            elif (otherNum == num):
                if len([index for index, value in enumerate(nums) if value == num]) > 1:
                    return [index for index, value in enumerate(nums) if value == num]

print(Solution.twoSum([3,2,4], 6))


# Results: Accepted 63 / 63 testcases passed
# Runtime: 443
# ms
# Beats
# 32.67%

# Memory
# 18.33
# MB
# Beats
# 87.34%
# Analyze Complexity

