class Solution:
    def isValid(self, s: str) -> bool:
        para = []
        for b in s:
            if para == []:
                para.append(b)
            else:
                if b == '}' and para[-1] == '{':
                    para.pop()
                elif b == ')' and para[-1] == '(':
                    para.pop()
                elif b == ']' and para[-1] == '[':
                    para.pop()
                else:
                    para.append(b)
        if para == []:
            return True
        return False