import collections
import heapq
from cmath import inf
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], initial_location: int, target_dst: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for flight in flights:
            src, dest, price = flight
            edges[src].append([dest, price])
        # [[price, dest, stops]]
        lowestPrice = float(inf)
        pq = [[0, initial_location, -1]]
        #print(pq)
        while pq:
            price, area, stops = heapq.heappop(pq)
            #print(price, area, stops)
            if area == target_dst:
                return price
            if stops >= k:
                continue
            for new_dest, additional_cost in edges[area]:
                total_price = price + additional_cost
                heapq.heappush(pq, [total_price, new_dest, stops + 1])
        return -1

print(
    # Solution.findCheapestPrice('',
    #                            3,
    #                            [[0, 1, 100], [1, 2, 100], [0, 2, 500]],
    #                            0,
    #                            2,
    #                            1
    #                            ),

    Solution.findCheapestPrice('',
                               5,
                               [[4, 1, 1], [1, 2, 3], [0, 3, 2], [0, 4, 10], [3, 1, 1], [1, 4, 3]],
                               2,
                               1,
                               1
                               )
)
