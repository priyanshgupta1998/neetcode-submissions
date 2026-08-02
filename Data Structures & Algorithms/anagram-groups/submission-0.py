from collections import defaultdict


class Solution:

  def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    ans = defaultdict(list)

    for s in strs:
      # 26 size frequency array for 'a' through 'z'
      count = [0] * 26
      for c in s:
        count[ord(c) - ord("a")] += 1

      # Convert list to immutable tuple to use as dictionary key
      ans[tuple(count)].append(s)

    return list(ans.values())