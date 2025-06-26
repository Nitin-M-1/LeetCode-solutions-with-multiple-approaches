# 2311. Longest Binary Subsequence Less Than or Equal to K
# 
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        stringLength = 0
        for i in range(len(s)- 1, -1, -1):
            print(s[i])
            if s[i] == '0':
                stringLength += 1
            else:
                bitV = 1 << (len(s)- i - 1)
                if k - bitV  >= 0:
                    stringLength += 1
                    k -= bitV
        return stringLength