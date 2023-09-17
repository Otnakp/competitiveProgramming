from heapq import heappush, heappop
from typing import List, Dict, Tuple

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        def dijkstra(graph: Dict[Tuple[int, int], Dict[Tuple[int, int], int]], start: Tuple[int, int], end: Tuple[int, int]) -> int:
            heap = [(0, start)]
            distances = {node: float('inf') for node in graph}
            distances[start] = 0
            visited = set()

            while heap:
                (cost, current) = heappop(heap)
                if current in visited:
                    continue
                visited.add(current)

                if current == end:
                    return cost

                for neighbor, weight in graph[current].items():
                    distance = max(cost, weight)

                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        heappush(heap, (distance, neighbor))

        # Existing code to create graph
        graph = {}
        for i in range(len(heights)):
            for j in range(len(heights[i])):
                graph[(i,j)] = {}
        for i in range(len(heights)):
            for j in range(1, len(heights[i])):
                w = abs(heights[i][j] - heights[i][j-1])
                graph[(i,j-1)][(i, j)] = w
                graph[(i,j)][(i, j-1)] = w

            if i < len(heights) - 1:
                for j in range(len(heights[i])):
                    w = abs(heights[i+1][j] - heights[i][j])
                    graph[(i,j)][(i+1,j)] = w
                    graph[(i+1,j)][(i,j)] = w

        # Use Dijkstra to find path of minimum effort
        return dijkstra(graph, (0, 0), (len(heights) - 1, len(heights[0]) - 1))

s = Solution()
m = [[1, 2, 3], [3, 8, 4], [5, 3, 5]]
result = s.minimumEffortPath(m)
print(result)



