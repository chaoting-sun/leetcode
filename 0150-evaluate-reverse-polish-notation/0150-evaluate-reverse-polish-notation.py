class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        print(tokens)
        stack = [int(tokens[0])]
        i = 1
        l = len(tokens)

        while i < l:
            while i < l and tokens[i].lstrip('-').isdigit():
                stack.append(int(tokens[i]))
                i += 1

            if not tokens[i].lstrip('-').isdigit():
                prev2 = stack.pop() 
                
                while i < l and not tokens[i].lstrip('-').isdigit():
                    prev1 = stack.pop()

                    if tokens[i] == '+':
                        prev2 = prev1 + prev2
                    elif tokens[i] == '-':
                        prev2 = prev1 - prev2
                    elif tokens[i] == '*':
                        prev2 = prev1 * prev2
                    elif tokens[i] == '/':
                        prev2 = int(prev1 / prev2)
                    i += 1
                
                stack.append(prev2)
        
        return stack[0]