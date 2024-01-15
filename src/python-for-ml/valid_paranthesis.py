"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false

"""

class ValidParanthesis:
    def isValid(self, s: str) -> bool:
        valid = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        open_brackets = ['(', '{', '[']
        stack = []
        i = 0
        chars = list(s)
        while i < len(chars):
            if chars[i] in open_brackets:
                stack.append(chars[i])
            else:
                if len(stack) > 0:
                    if valid[stack.pop()]!=chars[i]:
                        return False
                else:
                    return False
            i += 1
        if len(stack) == 0:
            return True
        return False




