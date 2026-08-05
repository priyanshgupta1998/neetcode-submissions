class Solution:
    def isValid(self, s: str) -> bool:
        # Quick edge case check: Odd length string valid nahi ho sakti
        if len(s) % 2 != 0:
            return False

        stack = []
        closeToOpen = { ")": "(", "}": "{", "]": "[" }

        for c in s:
            if c in closeToOpen:
                # Agar character closing bracket hai
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                # Agar character opening bracket hai
                stack.append(c)

        # Agar stack empty hai, toh valid hai
        return len(stack) == 0