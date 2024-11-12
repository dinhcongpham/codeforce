# https://leetcode.com/problems/most-beautiful-item-for-each-query/description/?envType=daily-question&envId=2024-11-12
# O(m * n^2): two loop each query
# O(max(m * log(n), nlog(n))): sort items -> track max_beauty(O(n)) -> binary search each query for position suitable of max_value (O(logn))

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key=lambda x: x[0])
        max_value = []
        max_beauty = 0
        for price, beauty in items:
            max_beauty = max(max_beauty, beauty)
            if not max_value:
                max_value.append((price, max_beauty))
            else:
                if max_value[-1][0] == price:
                    aaa = max_value[-1][1]
                    max_value.pop()
                    max_value.append((price, max(aaa, max_beauty)))
                    
                else:
                    max_value.append((price, max_beauty))
        
        ans = []

        for price in queries:
            # Locate the rightmost price <= query price
            idx = bisect_right(max_value, (price, float('inf'))) - 1
            if idx >= 0:
                ans.append(max_value[idx][1])  # Add max beauty within price range
            else:
                ans.append(0)  # If no price <= query, return 0

        return ans
