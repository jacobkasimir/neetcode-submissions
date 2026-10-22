class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> s; 
        for (int i : nums){
            if(s.contains(i)) return true; 
            else s.insert(i);
        }
        return false; 

    }
};