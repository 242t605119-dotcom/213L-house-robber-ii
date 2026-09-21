class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_linear(houses):
            prev = 0
            curr = 0

            for money in houses:
                prev, curr = curr, max(curr, prev + money)

            return curr

        # Case 1: Exclude the first house
        case1 = rob_linear(nums[1:])

        # Case 2: Exclude the last house
        case2 = rob_linear(nums[:-1])

        return max(case1, case2)
