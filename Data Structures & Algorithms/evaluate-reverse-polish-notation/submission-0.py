class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []

        def operations(left, right, op)-> int:
            if op == "+":
                return left + right
            elif op == "-":
                return left - right
            elif op =="*":
                return left * right
            elif op =="/":
                return int(left / right)

        for i in range(len(tokens)):
            if tokens[i] in "+-*/":
                right = st.pop()
                left = st.pop()
                st.append(operations(left,right,tokens[i]))
            else:
                st.append(int(tokens[i]))
        return st.pop()
                