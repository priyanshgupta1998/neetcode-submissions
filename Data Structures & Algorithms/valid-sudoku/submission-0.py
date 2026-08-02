class Solution:

  def isValidSudoku(self, board: list[list[str]]) -> bool:
    rows = [0] * 9
    cols = [0] * 9
    boxes = [0] * 9

    for r in range(9):
      for c in range(9):
        val = board[r][c]
        if val == ".":
          continue

        digit = int(val)
        bit = 1 << digit
        box_idx = (r // 3) * 3 + (c // 3)

        # Check duplicate using Bitwise AND
        if (
            (rows[r] & bit) != 0
            or (cols[c] & bit) != 0
            or (boxes[box_idx] & bit) != 0
        ):
          return False

        # Set bit using Bitwise OR
        rows[r] |= bit
        cols[c] |= bit
        boxes[box_idx] |= bit

    return True