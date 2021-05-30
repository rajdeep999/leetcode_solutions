class Solution:
    def isValid(self, s: str) -> bool:
        stack_li = []
        for i in s:
            if i in ["(", "[", "{"]:
                stack_li.append(i)
            else:
                if len(stack_li) > 0:
                    if i == ")" and stack_li[-1] == "(":
                        stack_li.pop(-1)
                    elif i == "]" and stack_li[-1] == "[":
                        stack_li.pop(-1)
                    elif i == "}" and stack_li[-1] == "{":
                        stack_li.pop(-1)
                    else:
                        return False
                else:
                    return False
        if len(stack_li) == 0:
            return True
        else:
            return False

