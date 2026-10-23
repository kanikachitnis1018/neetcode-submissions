import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
        "+":operator.add, 
        "-": lambda a, b: b - a,
        "/": lambda a, b: int(b/a),
        "*":operator.mul
        }
        stk = []

        for t in tokens:
            if t not in ops:
                stk.append(int(t))
            else:
                a = stk.pop()
                b = stk.pop()
                stk.append(ops[t](a,b))

        return stk[0]
