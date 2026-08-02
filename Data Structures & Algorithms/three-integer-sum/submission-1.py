class Solution:

  def threeSum(self, nums: list[int]) -> list[list[int]]:
    res = []
    nums.sort()  # Step 1: Sort the array

    for i in range(len(nums) - 2):
      # Skip positive numbers (since sorted array can't sum to 0 if smallest > 0)
      if nums[i] > 0:
        break

      # Skip duplicate values for 'i'
      if i > 0 and nums[i] == nums[i - 1]:
        continue

      left, right = i + 1, len(nums) - 1

      while left < right:
        three_sum = nums[i] + nums[left] + nums[right]

        if three_sum > 0:
          right -= 1
        elif three_sum < 0:
          left += 1
        else:
          res.append([nums[i], nums[left], nums[right]])
          left += 1
          right -= 1

          # Skip duplicates for 'left' pointer
          while left < right and nums[left] == nums[left - 1]:
            left += 1

    return res