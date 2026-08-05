class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # Pairs create karke position ke descending order me sort kar rahe hain
        pair = [[p, s] for p, s in zip(position, speed)]
        stack = []

        for p, s in sorted(pair, reverse=True):
            # Calculate time to reach target
            time = (target - p) / s
            stack.append(time)

            # Agar piche wali car ka time aage wali car se kam/equal hai,
            # toh woh aage wali fleet me merge ho jayegi (pop current car time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)