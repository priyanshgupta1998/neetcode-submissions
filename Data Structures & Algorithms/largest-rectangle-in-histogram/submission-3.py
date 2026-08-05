class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        maxArea = 0
        stack = []  # Store pairs: (start_index, height)

        for i, h in enumerate(heights):
            start = i
            # Jab tak stack non-empty hai aur top height current height se badi hai
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                # Pop hue bar ka max possible area compute karo
                maxArea = max(maxArea, height * (i - index))
                # Current height choti hone ke bawajood piche wale index tak expand ho sakti hai
                start = index

            stack.append((start, h))

        # Stack me bache hue elements histogram ke end (len(heights)) tak extend hote hain
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea