class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        sort(points.begin(), points.end(), [](vector<int>& p1, vector<int>& p2) {
            return p1[0] < p2[0];
        });
        int arrows = 0;
        int firstEnd = INT_MAX;
        for (auto& p: points) {
            int start = p[0], end = p[1];
            if (firstEnd < start) {
                arrows++;
                firstEnd = end;
            } else {
                firstEnd = min(firstEnd, end);
            }
        }
        return arrows + 1;
    }
};