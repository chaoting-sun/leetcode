class Solution {
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        unordered_map<string,int> freq;
        for (string& word: words) {
            freq[word]++;
        }
        vector<pair<string, int>> wordFreq;
        for (auto& [w, f]: freq) {
            wordFreq.push_back({ w, f });
        }
        sort(wordFreq.begin(), wordFreq.end(), [](pair<string,int>& wf1, pair<string,int>& wf2) {
            if (wf1.second == wf2.second) return wf1.first < wf2.first;
            return wf1.second > wf2.second;
        });
        vector<string> ans;
        for (int i = 0; i < k; i++) ans.push_back(wordFreq[i].first);
        return ans;
    }
};