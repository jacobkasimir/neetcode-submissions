class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> mp; // value -> index
        
        for (int i = 0; i < nums.size(); i++) {
            int goal = target - nums[i];
            
            if (mp.count(goal)) {
                return {mp[goal], i};
            }
            
            mp[nums[i]] = i;
        }
        
        return {};
    }
};