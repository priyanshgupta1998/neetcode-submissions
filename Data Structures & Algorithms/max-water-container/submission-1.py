class Solution:

  def maxArea(self, heights: list[int]) -> int:
    left, right = 0, len(heights) - 1
    max_water = 0

    while left < right:
      # Calculate water area for current pointers
      current_height = min(heights[left], heights[right])
      width = right - left
      current_area = current_height * width

      max_water = max(max_water, current_area)

      # Move the pointer pointing to the shorter line
      if heights[left] < heights[right]:
        left += 1
      else:
        right -= 1

    return max_water