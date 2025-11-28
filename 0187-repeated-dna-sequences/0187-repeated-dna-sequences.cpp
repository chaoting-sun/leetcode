// class Solution {
// public:
//     vector<string> findRepeatedDnaSequences(string s) {
//         int n = s.size();
//         if (n <= 10) return {};
        
//         unordered_set<string> visited;
//         unordered_set<string> visitedAgain;
//         string current = s.substr(0, 10);
//         visited.insert(current);

//         for (int i = 10; i < n; i++) {
//             string temp = current.substr(1);
//             temp.push_back(s[i]);
//             if (visited.count(temp)) {
//                 visitedAgain.insert(temp);
//             }
//             visited.insert(temp);
//             current = temp;
//         }
//         vector<string> ans;
//         for (const string& seq: visitedAgain) {
//             ans.push_back(seq);
//         }
//         return ans;
//     }
// };

class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        int n = s.size();
        if (n <= 10) return {};
        
        unordered_set<int> visited;
        unordered_set<int> visitedAgain;

        string current = s.substr(0, 10);
        visited.insert(seq2int(current));

        for (int i = 10; i < n; i++) {
            current = current.substr(1);
            current.push_back(s[i]);
            int encoded = seq2int(current);
            if (visited.count(encoded)) {
                visitedAgain.insert(encoded);
            }
            visited.insert(encoded);
        }
        vector<string> ans;
        for (const int& encoded: visitedAgain) {
            string decoded = int2seq(encoded);
            ans.push_back(decoded);
        }
        return ans;
    }

    int seq2int(string& seq) {
        int res = 0;
        for (int i = 0; i < 10; i++) {
            int shift = i * 2;
            if (seq[i] == 'A') {
                continue;
            } else if (seq[i] == 'T') {
                res |= (1 << shift);
            } else if (seq[i]== 'C') {
                res |= (1 << (shift + 1));
            } else {
                res |= (1 << shift);
                res |= (1 << (shift + 1));
            }
        }
        return res;
    }

    string int2seq(int encoded) {
        string res = "";
        for (int i = 0; i < 10; i++) {
            int bit1 = encoded & (1 << 1);
            int bit2 = encoded & (1 << 0);
            if (!bit1 && !bit2) res += 'A';
            else if (!bit1 && bit2) res += 'T';
            else if (bit1 && !bit2) res += 'C';
            else res += 'G';
            encoded >>= 2;
        }
        return res;
    }
};

// AAAAACCCCC
// A -> 00
// T -> 01
// C -> 10
// G -> 11

// string -> 32 bit integer
// 32 bit integer -> string