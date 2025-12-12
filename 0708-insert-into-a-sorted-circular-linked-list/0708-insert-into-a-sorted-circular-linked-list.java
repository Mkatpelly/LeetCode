/*
// Definition for a Node.
class Node {
    public int val;
    public Node next;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _next) {
        val = _val;
        next = _next;
    }
};
*/

class Solution {
    public Node insert(Node head, int insertVal) {
        Node newNode = new Node(insertVal);
        if (head == null) {
            newNode.next = newNode;
            return newNode;
        }

        Node current = head;

        while (true) {
            if (current.val <= insertVal && insertVal <= current.next.val) {
                break;
            }
            if (current.val > current.next.val && (insertVal < current.next.val || insertVal > current.val)) {
                break;
            }
            current = current.next;
            if (current == head) {
                break;
            }
        }
        newNode.next = current.next;
        current.next = newNode;
        return head;
    }
}