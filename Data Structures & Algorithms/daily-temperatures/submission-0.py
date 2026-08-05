class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0] * len(temperatures)
        stack = []  # Pairs or indices: index store karte hain

        for i, temp in enumerate(temperatures):
            # Monotonic Stack condition: jab tak current temp pichle stored temps se bada hai
            while stack and temp > temperatures[stack[-1]]:
                prev_i = stack.pop()
                res[prev_i] = i - prev_i

            stack.append(i)

        return res