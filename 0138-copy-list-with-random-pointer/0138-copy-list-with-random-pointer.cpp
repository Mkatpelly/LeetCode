#include <unordered_map>
using namespace std;


class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (!head) return nullptr;

        unordered_map<Node*, Node*> mp; // original -> copy

        // 1) create all nodes
        for (Node* cur = head; cur; cur = cur->next)
            mp[cur] = new Node(cur->val);

        // 2) wire next/random
        for (Node* cur = head; cur; cur = cur->next) {
            mp[cur]->next = cur->next ? mp[cur->next] : nullptr;
            mp[cur]->random = cur->random ? mp[cur->random] : nullptr;
        }

        return mp[head];
    }
};
