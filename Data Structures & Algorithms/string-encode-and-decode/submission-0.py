class Solution:

  def encode(self, strs: list[str]) -> str:
    res = ""
    for s in strs:
      res += str(len(s)) + "#" + s
    return res

  def decode(self, s: str) -> list[str]:
    res = []
    i = 0

    while i < len(s):
      # Find the delimiter '#' starting from index i
      j = i
      while s[j] != "#":
        j += 1

      # Read the length of the upcoming string
      length = int(s[i:j])

      # Extract the substring of exact 'length'
      i = j + 1
      res.append(s[i : i + length])

      # Move index to the start of next length header
      i += length

    return res