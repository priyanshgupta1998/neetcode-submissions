class Solution:

  def lengthOfLongestSubstring(self, s: str) -> int:
    char_map = {}  # char -> last seen index
    left = 0
    res = 0

    for right in range(len(s)):
      # If character is already seen and inside current window
      if s[right] in char_map:
        left = max(left, char_map[s[right]] + 1)

      char_map[s[right]] = right
      res = max(res, right - left + 1)

    return res