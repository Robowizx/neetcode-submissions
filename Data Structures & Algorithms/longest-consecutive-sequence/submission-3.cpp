class Solution {
public:
    int longestConsecutive(vector<int>& nums) {

        
        int max_count = 0,count=1; 

        if (nums.size() > 0){
            max_count = 1;
            set<int> hash(nums.begin(),nums.end());
            auto prev = *hash.begin();

            for (auto it = ++hash.begin(); it != hash.end(); it++){
                if (*it == prev+1){
                    count++;
                    if (count > max_count){
                        max_count = count;
                    }
                }
                else{
                    count = 1;
                }
                prev = *it;
            }
        }

        return max_count;
        
    }
};
