class TextEditor(object):

    def __init__(self):
        self.left = []   # characters to the left of cursor
        self.right = []  # characters to the right of cursor (in reverse order)

    def addText(self, text):
        # Append each char of text to the left stack
        self.left.extend(list(text))

    def deleteText(self, k):
        # Delete at most k chars from the left of cursor
        k = min(k, len(self.left))
        for _ in range(k):
            self.left.pop()
        return k

    def cursorLeft(self, k):
        # Move cursor left by min(k, len(left)) positions
        k = min(k, len(self.left))
        for _ in range(k):
            self.right.append(self.left.pop())
        # Return last min(10, len(left)) chars to the left of cursor
        return ''.join(self.left[-10:])

    def cursorRight(self, k):
        # Move cursor right by min(k, len(right)) positions
        k = min(k, len(self.right))
        for _ in range(k):
            self.left.append(self.right.pop())
        # Return last min(10, len(left)) chars to the left of cursor
        return ''.join(self.left[-10:])


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)