class Solution {
public:
    string lastSubstring(string s) {
        int i=0, j=1, k=0, n=s.length();
        while (j+k<n){
            if(s[i+k] == s[j+k]) {
                k++;
                continue;
            }
            else if (s[i+k] > s[j+k]) j += k+1;
            else {
                i = max(i+k+1, j);
                j = i+1;
            }
            k = 0;
        }
        return s.substr(i);
    }
};