#include <bits/stdc++.h>
using namespace std;

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *l, TreeNode *r) : val(x), left(l), right(r) {}
 * };
 */

class Solution {
public:
    int ans = 0;

    int dfs(TreeNode* node) {
        if (!node) return 0;

        int leftLen = dfs(node->left);
        int rightLen = dfs(node->right);

        int extendLeft = 0, extendRight = 0;

        if (node->left && node->left->val == node->val) {
            extendLeft = leftLen + 1;   // +1 edge to left child
        }
        if (node->right && node->right->val == node->val) {
            extendRight = rightLen + 1; // +1 edge to right child
        }

        ans = max(ans, extendLeft + extendRight); // path through node
        return max(extendLeft, extendRight);      // best downward path
    }

    int longestUnivaluePath(TreeNode* root) {
        ans = 0;
        dfs(root);
        return ans;
    }
};
