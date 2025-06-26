# 2040. Kth Smallest Product of Two Sorted Arrays


# Method 1
# output : ❌ "Time Limit Exceeded"
# Description : Using Heap 
import heapq
nums1 = [2,5]
nums2 = [3,4]
k = 2
heap = []
import heapq
class Solution:
    def kthSmallestProduct(self, nums1, nums2, k):
        heap = []
        for num_1 in nums1:
            for num_2 in nums2:
                heapq.heappush(heap, num_1 * num_2)
        for i in range(k-1):
            heapq.heappop(heap)
        return(heap[0])



# Method 2
# output : ❌ "Time Limit Exceeded"


