class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hm={}
        for i in range(0,len(nums)):
            if nums[i] not in hm.keys():
                hm[nums[i]]=1
            else:
                hm[nums[i]]+=1

        for key, value in hm.items():
            if value>1:
                return True
        return False

        