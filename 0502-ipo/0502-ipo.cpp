class Solution {
public:
    int findMaximizedCapital(int k, int w, vector<int>& profits, vector<int>& capital) {
        int n = profits.size();
        
        priority_queue<int> pq; // max heap; profit
        
        vector<pair<int,int>> projects(n); // capital, profit
        for (int i = 0; i < n; i++) {
            projects[i] = { capital[i], profits[i] };
        }
        sort(projects.begin(), projects.end());

        int totalCapital = w;
        int validProjectIdx = 0;
        for (int i = 0; i < k; i++) {
            while (validProjectIdx < n && totalCapital >= projects[validProjectIdx].first) {
                pq.push(projects[validProjectIdx].second);
                validProjectIdx++;
            }
            if (pq.empty()) break;
            totalCapital += pq.top();
            pq.pop();
        }
        return totalCapital;
    }
};