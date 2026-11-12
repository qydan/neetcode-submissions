class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        if not tokens: return 0
        
        operators = {"*", "+", "-", "/"}
        number_stack = []

        for token in tokens:
            if token in operators:
                operand_2 = number_stack.pop()
                operand_1 = number_stack.pop()
                if token == "+": 
                    number_stack.append(operand_1 + operand_2) 
                elif token == "-":
                    number_stack.append(operand_1 - operand_2) 
                elif token == "*": 
                    number_stack.append(operand_1 * operand_2) 
                else: 
                    number_stack.append(int(operand_1  / operand_2)) 

            else:	
                number_stack.append(int(token))

        return number_stack[0]

