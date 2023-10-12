class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        print(tokens)
        stack = [int(tokens[0])]
        i = 1
        l = len(tokens)

        operate = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: int(x / y)
        }

        while i < l:
            while i < l and tokens[i].lstrip('-').isdigit():
                stack.append(int(tokens[i]))
                i += 1

            if not tokens[i].lstrip('-').isdigit():
                prev2 = stack.pop() 
                
                while i < l and not tokens[i].lstrip('-').isdigit():
                    prev1 = stack.pop()
                    prev2 = operate[tokens[i]](prev1, prev2)
                    i += 1
                
                stack.append(prev2)
        
        return stack[0]