class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for char in s:
            if char == '{' or char == '[' or char == '(':
                st.append(char)
            else: 
                if not st:
                    return False
                else:
                    if char == ']' and st[-1] == '[':
                        st.pop()
                    elif char == '}' and st[-1] == '{':
                        st.pop()
                    elif char == ')' and st[-1] == '(':
                        st.pop()
                    else:
                        return False
        return not st