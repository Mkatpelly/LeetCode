# The read4 API is already defined for you.
# @param buf4, List[str]
# @return an integer
# def read4(buf4):

class Solution(object):
    def __init__(self):
        self.itr = self.read_chars()
        
    def read_chars(self):
        buf4 = ['']*4
        while True:
            bytes_read = read4(buf4)
            if bytes_read == 0:
                return
            for i in range(bytes_read):
                yield buf4[i]

    def read(self, buf, n):
        """
        :type buf: List[str]
        :type n: int
        :rtype: int
        """
        for i in range(n):
            try:
                buf[i] = next(self.itr)
            except StopIteration:
                return i
        return i+1