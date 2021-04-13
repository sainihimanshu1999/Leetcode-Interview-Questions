class Solution:
    def evalRPN(self,A):
        stack = []
        for num in A:
            if num not in '+-*/':
                stack.append(int(num))

            else:
                r,l = stack.pop(),stack.pop()
                if num == '+':
                    stack.append(l+r)
                elif num == '-':
                    stack.append(l-r)
                elif num == '*':
                    stack.append(l*r)
                else:
                    stack.append(int(float(l)/r))

        return stack.pop()

                