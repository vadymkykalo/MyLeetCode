"""
Given an integer x, return true if x is a palindrome , and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Constraints:

-231 <= x <= 231 - 1

Follow up: Could you solve it without converting the integer to a string?
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        digits = [int(digit) for digit in str(x)]

        return digits == digits[::-1]


if __name__ == '__main__':
    solution = Solution()

    assert solution.isPalindrome(121) == True, "Test case 1 failed"
    assert solution.isPalindrome(-121) == False, "Test case 2 failed"
    assert solution.isPalindrome(10) == False, "Test case 3 failed"
    assert solution.isPalindrome(12321) == True, "Test case 4 failed"
    assert solution.isPalindrome(123321) == True, "Test case 5 failed"

    print("All tests passed successfully.")