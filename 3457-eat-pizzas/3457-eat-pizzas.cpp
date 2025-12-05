class Solution {
public:
    long long maxWeight(vector<int>& pizzas) {
        int n = pizzas.size();
        int nDays = n / 4;
        int nEvens = nDays / 2;
        int nOdds = nDays - nEvens;

        sort(pizzas.begin(), pizzas.end(), [](int p1, int p2) { return p1 > p2; });

        int idx = 0;
        long long total = 0;
        while (nOdds--) {
            total += pizzas[idx];
            idx++;
        }
        
        idx++;
        while (nEvens--) {
            total += pizzas[idx];
            idx += 2;
        }
        return total;
    }
};