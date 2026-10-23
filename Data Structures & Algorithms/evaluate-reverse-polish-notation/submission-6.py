class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for token in tokens:
            if token not in ["+","-","/","*"]:
                nums.append(int(token))
            else:
                num1 = nums.pop()
                num2 = nums.pop()
                if token == "+":
                    result = num1 + num2
                if token == "-":
                    result = num2  - num1
                if token == "*":
                    result = num1 * num2
                if token == "/":
                    result = num2 / num1

                nums.append(int(result))

        return nums[-1]

