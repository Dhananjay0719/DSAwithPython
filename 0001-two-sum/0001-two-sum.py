class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #search for the complement of the number

        compList={}

        for i,num in enumerate(nums):
            complement=target-nums[i]

            if(complement in compList):
                return [compList[complement],i]
            
            compList[num]=i

        return []