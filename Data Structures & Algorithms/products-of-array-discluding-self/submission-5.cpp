class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
       vector<int> out,prefix,suffix;
       int pre_acc = 1, post_acc = 1;

       for(int i=0; i<nums.size(); i++){
         prefix.push_back(pre_acc);
         suffix.push_back(post_acc);
         pre_acc *= nums[i];
         post_acc *= nums[nums.size()-1-i];
       }

       for(int i=0; i<nums.size(); i++){
            out.push_back(prefix[i]*suffix[nums.size()-1-i]);
       } 

       return out;

    }
};
