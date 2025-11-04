// Approach: Monotonic Stack
// Time: O(n)
// Space: O(n)

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

 class Solution {
public:
    vector<int> nextLargerNodes(ListNode* head) {
        vector<int> values;
        ListNode* curr = head;
        while (curr) {
            values.push_back(curr->val);
            curr = curr->next;
        }
        int n = values.size();
        vector<int> ans(n);
        stack<int> stk; // monotonic increasing
        for (int i = n - 1; i >= 0; i--) {
            while (!stk.empty() && values[i] >= values[stk.top()]) {
                stk.pop();
            }
            if (!stk.empty()) ans[i] = values[stk.top()];
            stk.push(i);
        }
        return ans;
    }
};


 
// class Solution {
// public:
//     vector<int> nextLargerNodes(ListNode* head) {
//         ListNode* current_node = head;
//         int length = 0;
//         while (current_node) {
//             length += 1;
//             current_node = current_node->next;
//         }
//         vector<int> answer(length, 0);

//         stack<pair<int, int>> value_stack; // index, value
//         current_node = head;
//         int current_index = 0;
//         while (current_node) {
//             while (!value_stack.empty() && value_stack.top().second < current_node->val) {
//                 answer[value_stack.top().first] = current_node->val;
//                 value_stack.pop();
//             }
//             value_stack.push({ current_index, current_node->val });
//             current_node = current_node->next;
//             current_index++;
//         }

//         return answer;
//     }
// };