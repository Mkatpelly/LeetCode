class Solution:
    def minAbbreviation(self, target, dictionary):
        def backtrack(i,cur_str,cur_count):
            if i == len(target):
                if cur_count != 0: cur_str += [str(cur_count)]
                ans.append(cur_str)
                return 
            
            backtrack(i+1,cur_str + ([str(cur_count)] if cur_count else []) + [target[i]],0)
            backtrack(i+1,cur_str,cur_count+1)


        def function(abbr,s):
            i, j = 0, 0 

            while i < len(abbr) and j < len(s):
                if abbr[i].isdigit():
                    count = int(abbr[i])
                    i += 1 
                    j += count 
                else:
                    if abbr[i] != s[j]:
                        return False 

                    i += 1 
                    j += 1 

            return i == len(abbr) and j == len(s)

        
        ans = []

        backtrack(0,[],0)

        ans.sort(key = len)


        for i in ans:
            val = True 

            for d in dictionary:
                if function(i,d):
                    val = False
                    break 

            if val == True:
                return "".join(i)