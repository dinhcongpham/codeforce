# https://leetcode.com/problems/count-the-number-of-fair-pairs/description/?envType=daily-question&envId=2024-11-13

class Solution:
    def countFairPairs(self, v: List[int], lower: int, upper: int) -> int:
        v.sort()  # Step 1: Sort the list in ascending order.
        
        ans = 0  # Step 2: Initialize a counter to store the total number of fair pairs.
        
        # Step 3: Iterate through each element in the sorted list except the last element.
        for i in range(len(v) - 1):
            # Step 4: Find the smallest index `low` such that `v[i] + v[low] >= lower`.
            low = bisect_left(v, lower - v[i], i + 1)
            
            # Step 5: Find the largest index `up` such that `v[i] + v[up - 1] <= upper`.
            up = bisect_right(v, upper - v[i], i + 1)
            
            # Step 6: The number of fair pairs with `v[i]` as one element is `up - low`.
            ans += up - low
        
        # Step 7: Return the final count of fair pairs.
        return ans

## v = [1, 3, 4, 1, 5] | lower = 5, upper = 7
## sort -> v = [1, 1, 3, 4, 5]
# loop 1: i = 0, v[i] = 1
  # -> search_left(v, 4, 1) = 3
  # -> search_right(v, 6, 1) = 5
  # ans += 5 - 3 = 2
## loop -> i = len(v) - 1