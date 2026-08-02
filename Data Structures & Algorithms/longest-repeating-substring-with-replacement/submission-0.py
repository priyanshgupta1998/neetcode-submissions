class Solution:

  def characterReplacement(self, s: str, k: int) -> int:
    count = {}
    left = 0
    max_freq = 0

    for right in range(len(s)):
      count[s[right]] = count.get(s[right], 0) + 1
      max_freq = max(max_freq, count[s[right]])

      # If current window size requires more than k replacements
      if (right - left + 1) - max_freq > k:
        count[s[left]] -= 1
        left += 1  # Shift window by 1 without shrinking max window achieved

    # Maximum valid length will automatically be window size at the end
    return len(s) - left