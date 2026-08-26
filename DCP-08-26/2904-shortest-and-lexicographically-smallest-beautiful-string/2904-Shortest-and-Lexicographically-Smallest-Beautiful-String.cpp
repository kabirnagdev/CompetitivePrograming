class Solution {
public:
    string shortestBeautifulSubstring(string s, int k) {
        std::string ans = "";
        int left = 0;
        int ones_count = 0;

        for (int right = 0; right < s.length(); ++right) {
            if (s[right] == '1') {
                ones_count++;
            }

            while (ones_count == k) {
                if (s[left] == '1') {
                    std::string current_str = s.substr(left, right - left + 1);

                    if (ans.empty() || current_str.length() < ans.length() || 
                       (current_str.length() == ans.length() && current_str < ans)) {
                        ans = current_str;
                    }

                    ones_count--;
                }
                left++;
            }
        }

        return ans;
    }
};