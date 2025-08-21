class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        setOutOfList=set(nums)
        print(len(setOutOfList))
        if(len(setOutOfList)==len(nums)):
            return False
        else:
            return True
        