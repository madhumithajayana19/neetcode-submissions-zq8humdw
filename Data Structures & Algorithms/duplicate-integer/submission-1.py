class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hm={}
        for i in range(0,len(nums)):
            if nums[i] not in hm.keys():
                hm[nums[i]]=1
            else:
                return True
        return False