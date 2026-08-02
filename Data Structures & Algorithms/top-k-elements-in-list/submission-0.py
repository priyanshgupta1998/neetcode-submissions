from collections import Counter


class Solution:

  def topKFrequent(self, nums: list[int], k: int) -> list[int]:
    count = Counter(nums)
    # Sort keys by their frequency in descending order
    sorted_elements = sorted(count.keys(), key=lambda x: count[x], reverse=True)
    return sorted_elements[:k]