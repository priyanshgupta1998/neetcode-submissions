class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            # Agar mid element rightmost element se bada hai, 
            # iska matlab min element RIGHT half me exist karta hai.
            if nums[mid] > nums[right]:
                left = mid + 1
            # Warna min element LEFT half me ya khud 'mid' par hai.
            else:
                right = mid

        # Loop end hone par left aur right same index (minimum element) par point karenge
        return nums[left]