class Solution:
    def RPN(self, tokens: list[str]) -> int:
        stack = []
        for token in tokens:
            if token in "+-*/":
                b = stack.pop()
                a = stack.pop()
                
                if token == "+":
                    result = a + b
                elif token == "-":
                    result = a - b
                elif token == "*":
                    result = a * b
                else:
                    result = int(a / b)
                
                stack.append(result)
            else:
                stack.append(int(token))
        
        return stack.pop()
obj = Solution()
# print(obj.RPN(["2","1","+","3","*"]))
print(obj.RPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
