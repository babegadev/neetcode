class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if i in {'(', '[', '{'}:
                stack.append(i)
            else:
                if stack == []:
                    return False
                else:
                    pair = stack.pop()
                
                    match i:
                        case ")":
                            if pair == "(":
                                continue
                            else:
                                return False
                        case "]":
                            if pair == "[":
                                continue
                            else:
                                return False
                        case "}":
                            if pair == "{":
                                continue
                            else:
                                return False

        return stack == []

        