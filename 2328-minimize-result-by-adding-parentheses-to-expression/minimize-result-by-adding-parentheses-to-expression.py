class Solution:
    def minimizeResult(self, expression: str) -> str:
        left, right = expression.split('+')                             
        value = lambda s:eval(s.replace('(','*(').replace(')',')*').strip('*'))    
                                                                           
        lft = [ left[0:i]+'('+ left[i:] for i in range(  len(left )  )] 
        rgt = [right[0:i]+')'+right[i:] for i in range(1,len(right)+1)] 
        return  min([l+'+'+r for l in lft for r in rgt], key = value)