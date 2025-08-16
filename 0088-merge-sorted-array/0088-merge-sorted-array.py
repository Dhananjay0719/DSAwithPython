class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #Approach:Add all elem from nums2 and then Sort nums1
        i=0
        while (i<n):
            nums1[(m+n)-1-i]=nums2[i]
            i+=1
        
        for i in range(m+n):
            for j in range(m+n-1):
                if(nums1[j]>nums1[j+1]):
                    nums1[j],nums1[j+1]=nums1[j+1],nums1[j]

        return nums1
        