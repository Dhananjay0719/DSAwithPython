class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        n=len(nums)
        candidate=0 
        vote=0
        for i in range(len(nums)):
           if (vote==0):
               vote=1
               candidate=nums[i]
            
           else:
               if(nums[i]==candidate):
                   vote+=1
               else:
                   vote-=1
        
        return candidate
        