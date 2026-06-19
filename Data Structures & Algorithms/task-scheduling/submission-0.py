class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        max_heap = []
        q = deque()
        for task in freq.keys():
            heapq.heappush(max_heap, (-freq[task], task))
        time = 0
        while True:
            if not max_heap and not q:
                return time
            time += 1
            if q and q[0][2] < time:
                task_freq, task, new_time = q.popleft()
                heapq.heappush(max_heap, (task_freq, task))
            if max_heap:
                task_freq, task = heapq.heappop(max_heap)
                task_freq += 1
                if task_freq != 0:
                    q.append((task_freq, task, time + n))
