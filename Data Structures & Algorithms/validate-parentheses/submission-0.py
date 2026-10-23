class Solution:
    def isValid(self, s: str) -> bool:
        OpentoClose = {")":"(", "]":"[", "}":"{"}

        stk = []

        for c in s:
            if c not in OpentoClose:
                stk.append(c)

            else:
                if stk:
                    popped = stk.pop()
                    if popped != OpentoClose[c]:
                        return False
                else:
                    return False
        return not stk