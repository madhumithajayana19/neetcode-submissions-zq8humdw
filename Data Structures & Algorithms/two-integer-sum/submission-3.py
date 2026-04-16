class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm={}
        for i in range(0, len(nums)):
            hm[nums[i]]=i
        for i in range(0, len(nums)):
            if target-nums[i] in hm:
                return [i, hm[target-nums[i]]]