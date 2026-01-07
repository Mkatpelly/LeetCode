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
    TreeNode* createBinaryTree(vector<vector<int>>& descriptions) {
        unordered_map<int, TreeNode*> mp;
        mp.reserve(descriptions.size() * 2);

        unordered_set<int> hasParent;
        hasParent.reserve(descriptions.size() * 2);

        for (auto &d : descriptions) {
            int parent = d[0], child = d[1], isLeft = d[2];

            if (!mp.count(parent)) mp[parent] = new TreeNode(parent);
            if (!mp.count(child))  mp[child]  = new TreeNode(child);

            if (isLeft) mp[parent]->left = mp[child];
            else        mp[parent]->right = mp[child];

            hasParent.insert(child);
        }

        // root = node that never appears as a child
        for (auto &d : descriptions) {
            int parent = d[0];
            if (!hasParent.count(parent)) return mp[parent];
        }
        return nullptr; // should not happen (tree is valid)
    }
};
