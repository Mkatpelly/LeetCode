class Node(object):
    __slots__ = ("key", "val", "freq", "prev", "next")
    def __init__(self, key, val, freq=1):
        self.key = key
        self.val = val
        self.freq = freq
        self.prev = None
        self.next = None


class DoublyLinkedList(object):
    def __init__(self):
        self.head = Node(None, None)  # dummy head
        self.tail = Node(None, None)  # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def appendleft(self, node):
        # insert node right after head (most recent)
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def remove(self, node):
        # remove an existing node
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
        self.size -= 1

    def pop(self):
        # remove and return LRU node (before tail)
        if self.size == 0:
            return None
        node = self.tail.prev
        self.remove(node)
        return node


class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.size = 0
        self.minFreq = 0
        self.keyToNode = {}      # key -> Node
        self.freqToList = {}     # freq -> DoublyLinkedList

    def _update_freq(self, node):
        """Move node from freq f to f+1 list."""
        f = node.freq
        lst = self.freqToList[f]
        lst.remove(node)

        # If this was the only node with minFreq, increase minFreq
        if f == self.minFreq and lst.size == 0:
            self.minFreq += 1

        node.freq += 1
        f2 = node.freq
        if f2 not in self.freqToList:
            self.freqToList[f2] = DoublyLinkedList()
        self.freqToList[f2].appendleft(node)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.keyToNode:
            return -1
        node = self.keyToNode[key]
        self._update_freq(node)
        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.capacity == 0:
            return

        if key in self.keyToNode:
            node = self.keyToNode[key]
            node.val = value
            self._update_freq(node)
            return

        # Need to insert a new key
        if self.size == self.capacity:
            # evict LFU (and LRU among them)
            lst = self.freqToList[self.minFreq]
            node_to_remove = lst.pop()
            del self.keyToNode[node_to_remove.key]
            self.size -= 1

        # insert new node with freq 1
        new_node = Node(key, value, freq=1)
        self.keyToNode[key] = new_node
        if 1 not in self.freqToList:
            self.freqToList[1] = DoublyLinkedList()
        self.freqToList[1].appendleft(new_node)
        self.minFreq = 1
        self.size += 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)