class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        i=1
        k=0

        for i in range(len(nums)):

            if(nums[k]!=nums[i]):
                nums[k+1]=nums[i]
                k=k+1

        return k+1

        