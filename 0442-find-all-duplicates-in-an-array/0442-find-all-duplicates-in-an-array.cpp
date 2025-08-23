class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        vector<int>ans;

        map<int,int>mpp;

        for(auto n:nums){
            if(mpp.count(n)==1){
                ans.push_back(n);
            }
            else{
                mpp[n]++;
            }
        }

        return ans;
    }
};