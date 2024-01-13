"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal
substring
 consisting of non-space characters only.

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.

Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        counter = 0
        for char in s[::-1]:
            if char == ' ' and counter != 0:
                return counter
            if char != ' ':
                counter += 1

        return counter

if __name__ == '__main__':
    solution = Solution()

    # Test cases
    assert solution.lengthOfLastWord("Hello World") == 5, "Test case 1 failed"
    assert solution.lengthOfLastWord("   fly me   to   the moon  ") == 4, "Test case 2 failed"
    assert solution.lengthOfLastWord("luffy is still joyboy") == 6, "Test case 3 failed"

    print("All test cases passed!")