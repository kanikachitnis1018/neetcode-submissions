class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        expression = []
        for token in tokens:
            if token in ["+","-","/","*"]:
                num1 = expression.pop()
                num2 = expression.pop()
                if token == "+":
                    result = num1 + num2
                elif token == "-":
                    result = num2 - num1
                elif token == "*":
                    result = num1 * num2
                else:
                    result = int(num2/num1)
                expression.append(result)
            else:
                expression.append(int(token))
        return expression.pop()

                 
