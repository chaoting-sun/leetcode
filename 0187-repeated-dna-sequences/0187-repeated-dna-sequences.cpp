class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        int n = s.size();
        if (n <= 10) return {};
        
        unordered_set<string> visited;
        unordered_set<string> visitedAgain;
        string current = s.substr(0, 10);
        visited.insert(current);

        for (int i = 10; i < n; i++) {
            string temp = current.substr(1);
            temp.push_back(s[i]);
            if (visited.count(temp)) {
                visitedAgain.insert(temp);
            }
            visited.insert(temp);
            current = temp;
        }
        vector<string> ans;
        for (const string& seq: visitedAgain) {
            ans.push_back(seq);
        }
        return ans;
    }
};



// AAAAACCCCC
// A -> 00
// T -> 01
// C -> 10
// G -> 11