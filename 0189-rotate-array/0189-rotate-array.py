class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        rotated=[-1]*n
        rotates=k%n
        for i in range(len(nums)):
            rotated[(i+k)%n]=nums[i]

        for i in range(len(nums)):
            nums[i]=rotated[i]