from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        q = deque()  # Store indices
        res = []

        for i in range(len(nums)):
            # 1. Out of window indices ko front se remove karo
            if q and q[0] <= i - k:
                q.popleft()

            # 2. Current element se choti saari values ko back se pop karo
            while q and nums[q[-1]] <= nums[i]:
                q.pop()

            # 3. Current element ka index append karo
            q.append(i)

            # 4. Pehli valid window poori hone ke baad result collect karo
            if i >= k - 1:
                res.append(nums[q[0]])

        return res