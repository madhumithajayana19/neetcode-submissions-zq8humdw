class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm={}
        for num in nums:
            hm[num]=nums.index(num)
        for i in range(0, len(nums)):
            if target-nums[i] in hm:
                return [i, hm[target-nums[i]]]