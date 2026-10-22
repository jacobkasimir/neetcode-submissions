class Solution {
public:
    bool isAnagram(string s, string t) {
        int seens[26] = {0};
        int seent[26]= {0}; 

        for(char c : s){
            seens[c-'a']++; 
        }
        cout << seens[0] << " "; 
        for(char b : t) {
            seent[b-'a']++;
        }
        cout << seent[0]; 
        for(int i = 0 ; i < 26; i++ ){
            if (seens[i] != seent[i]) return false; 
        }
        return true; 
    }
};
