class Solution:
    def findComplement(self, num: int) -> int:

        for i in range(0,32):
            if(num&(1<<i))!=0:
                k=i

        for i in range(0,k+1):
            num=num^(1<<i)

        return num