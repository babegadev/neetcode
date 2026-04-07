class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for i in s:
            if i in "({[":
                stack.append(i)
            elif stack == []:
                return False
            else:
                pair = stack.pop()
                
                if pairs[i] == pair:
                    continue
                else:
                    return False

        return stack == []

        