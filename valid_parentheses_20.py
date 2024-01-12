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


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        dict_pairs = {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }

        stack = []
        for char in s:
            if char in dict_pairs.keys():
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                else:
                    top_element = stack.pop()
                    if dict_pairs.get(top_element) == char:
                        continue
                    else:
                        return False

        return len(stack) == 0


if __name__ == '__main__':
    solution = Solution()

    assert solution.isValid("()") == True, "Error on test case 1"
    assert solution.isValid("()[]{}") == True, "Error on test case 2"
    assert solution.isValid("(]") == False, "Error on test case 3"
    assert solution.isValid("([)]") == False, "Error on test case 4"
    assert solution.isValid("{[]}") == True, "Error on test case 5"

    print("All tests passed successfully.")