class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int accumalator = 1;
        int zero_count = 0;
        vector<int> out;

        for (int i : nums){
            if (i !=0){
                accumalator *= i;
            }
            else{
                zero_count++;
            }    
        }

        if(zero_count){
            if (zero_count > 1){
                vector<int> null(nums.size(),0);
                return null;
            }
            else{
                for (int i=0; i<nums.size();i++){
                    if (nums[i] == 0){
                        out.push_back(accumalator);
                    }
                    else{
                        out.push_back(0);
                    }
                }
            }        
        }
        else{
            for (int i=0; i< nums.size(); i++){
                    out.push_back(accumalator/nums[i]);          
            }
        }
            
        return out;
    }
};
