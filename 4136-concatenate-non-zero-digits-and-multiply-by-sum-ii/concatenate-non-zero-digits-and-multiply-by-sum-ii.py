class Solution(object):
    def sumAndMultiply(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        MOD = 10**9 + 7
        n = len(s)
        

        non_zero_sum = [0] * (n + 1)
        prefix_x = [0] * (n + 1)
        count = [0] * (n + 1)
        
        for i in range(n):
            digit = int(s[i])
            non_zero_sum[i+1] = non_zero_sum[i]
            prefix_x[i+1] = prefix_x[i]
            count[i+1] = count[i]
            
            if digit != 0:
                non_zero_sum[i+1] += digit
                prefix_x[i+1] = (prefix_x[i+1] * 10 + digit) % MOD
                count[i+1] += 1
        
        # Precompute powers of 10 up to max possible length (n)
        max_len = n
        pow10 = [1] * (max_len + 1)
        for i in range(1, max_len + 1):
            pow10[i] = (pow10[i-1] * 10) % MOD
        
        def get_x(l, r):
            # Get the number x formed by non-zero digits in s[l:r+1]
            # and the sum of its digits
            total_sum = non_zero_sum[r+1] - non_zero_sum[l]
            if total_sum == 0:
                return 0, 0
            
            # Number of non-zero digits in [l, r]
            cnt = count[r+1] - count[l]
            
            # x = (prefix_x[r+1] - prefix_x[l] * 10^cnt) mod MOD
            x = (prefix_x[r+1] - (prefix_x[l] * pow10[cnt]) % MOD) % MOD
            if x < 0:
                x += MOD
            return x, total_sum
        
        # Answer each query
        answer = []
        for l, r in queries:
            x, digit_sum = get_x(l, r)
            res = (x * digit_sum) % MOD
            answer.append(res)
        
        return answer