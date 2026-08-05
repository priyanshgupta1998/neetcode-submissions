import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right

        while left <= right:
            k = left + (right - left) // 2

            # Calculate total hours needed with speed 'k'
            total_hours = 0
            for p in piles:
                # Math ceiling: (p + k - 1) // k is integer equivalent of math.ceil(p / k)
                total_hours += (p + k - 1) // k

            # Agar given time limit 'h' ke andar kha sakti hai
            if total_hours <= h:
                res = k
                right = k - 1  # aur choti speed try karo
            else:
                left = k + 1   # speed badhao

        return res