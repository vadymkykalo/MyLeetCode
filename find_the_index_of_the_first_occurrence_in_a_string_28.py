"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if not needle:
            return 0

        len_haystack = len(haystack)
        len_needle = len(needle)

        for i in range(len_haystack - len_needle + 1):
            flag = True
            for j in range(len_needle):
                if haystack[i + j] != needle[j]:
                    flag = False
                    break

            if flag:
                return i
        return -1



if __name__ == '__main__':
    solution = Solution()

    assert solution.strStr("sadbutsad", "sad") == 0, "Error on test case 1: 'sad' in 'sadbutsad'"
    assert solution.strStr("leetcode", "leeto") == -1, "Error on test case 2: 'leeto' not in 'leetcode'"
    assert solution.strStr("hello", "lo") == 3, "Error on test case 3: 'lo' in 'hello'"
    assert solution.strStr("hi", "hello") == -1, "Error on test case 6: 'haystack' shorter than 'needle'"

    print("All tests passed successfully.")
