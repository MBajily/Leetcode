class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        start = ["(", "[", "{"]
        end = [")", "]", "}"]

        for i in s:
            # print(stack)
            try:
                if i in start:
                    stack.append(str(i))
                    # print("stack.append(str(i))")
                elif i in end:
                    if end.index(i) == start.index(stack[-1]):
                        stack.pop()
                        # print("stack.pop()")
                    else:
                        # print("else False")
                        return False
            except:
                return False
        if stack:
            return False
        return True
        