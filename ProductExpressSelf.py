class Solution(object):
    def productExceptSelf(self, nums):
        table = {}
        counter = 1
        for i in range(len(nums)):
            table[i] = counter
            counter *= nums[i]

        counter2 = 1
        for j in range(len(nums) - 1, -1, -1):
            table[j] = table[j] * counter2
            counter2 *= nums[j]

        return table.values()

        """
        :type nums: List[int]
        :rtype: List[int]
        """
