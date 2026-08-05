class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        ROWS, COLS = len(matrix), len(matrix[0])

        left, right = 0, (ROWS * COLS) - 1

        while left <= right:
            mid = left + (right - left) // 2
            
            # 1D index 'mid' ko 2D (row, col) coordinates me map kar rahe hain
            row = mid // COLS
            col = mid % COLS
            mid_val = matrix[row][col]

            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1

        return False