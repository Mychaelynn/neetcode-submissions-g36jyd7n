class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        result=0
        for i in tokens:
                match i:
                    case "+":
                        result=stack.pop()+stack.pop()
                        stack.append(result)
                    case "-":
                        divisor = stack.pop()
                        divider = stack.pop()
                        result=divider-divisor
                        stack.append(result)
                    case "*":
                        result=stack.pop()*stack.pop()
                        stack.append(result)
                    case "/":
                        divisor = stack.pop()
                        divider = stack.pop()
                        result=int(float(divider)/divisor)
                        stack.append(result)
                    case _:
                        stack.append(int(i))

                    
        return stack.pop()

                