class Solution:

  def productExceptSelf(self, nums: list[int]) -> list[int]:
    n = len(nums)
    res = [1] * n

    # Step 1: Calculate prefix products directly in res array
    prefix = 1
    for i in range(n):
      res[i] = prefix
      prefix *= nums[i]

    # Step 2: Multiply with postfix products on the fly
    postfix = 1
    for i in range(n - 1, -1, -1):
      res[i] *= postfix
      postfix *= nums[i]

    return res