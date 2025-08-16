class Solution {
public:
    int majorityElement(vector<int>& nums) {
      //moore voting algo
      int n=nums.size();
      int candidate=0,vote=0;
      for(int i=0;i<n;i++)
      {
        if(vote==0){
            vote=1;
            candidate=nums[i];
        }
        else{
            if(candidate==nums[i]){
                vote++;
            }
            else{
                vote--;
            }
        }
      }
      return candidate;
    }
};