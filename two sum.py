class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {} # stores: {value: index}
        for i, n in enumerate(nums):
            complement = target - n
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[n] = i
