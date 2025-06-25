# 2200. Find All K-Distant Indices in an Array


# Method 1
nums = [1,1000,1,1000]
key = 1
k = 1
class Solution:
    def findKDistantIndices(self, nums, key, k):
        result = [] 
        for index, value in enumerate(nums):
            if value == key:
                if len(result) == 0:
                    if index - k < 0:
                        for i in range(0, index + k + 1 if index + k < len(nums) else len(nums)):
                            result.append(i)
                    else:
                        for i in range(index - k, index + k + 1 if index + k < len(nums) else len(nums)):
                            result.append(i)
                else:
                    if index - k <= result[-1]:
                        for i in range(result[-1] + 1, index + k + 1 if index + k < len(nums) else len(nums)):
                            result.append(i)
                    else:
                        for i in range(index - k + 1, index + k + 1 if index + k < len(nums) else len(nums)):
                            result.append(i)
        return result
                    
                
                



obj = Solution()
print(obj.findKDistantIndices(nums, key, k))
        



