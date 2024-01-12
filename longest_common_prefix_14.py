"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        min_len_word = min(len(word) for word in strs)

        res = ''
        for i in range(min_len_word):
            current_char = strs[0][i]

            for word in strs:
                if word[i] != current_char:
                    return res
            res += current_char

        return res


if __name__ == '__main__':
    solution = Solution()

    assert solution.longestCommonPrefix(["flower", "flow", "flight"]) == "fl", "Error on test case 1"
    assert solution.longestCommonPrefix(["dog", "racecar", "car"]) == "", "Error on test case 2"
    assert solution.longestCommonPrefix(["interspecies", "interstellar", "interstate"]) == "inters", "Error on test case 3"
    assert solution.longestCommonPrefix([""]) == "", "Error on test case 4"
    assert solution.longestCommonPrefix(["a"]) == "a", "Error on test case 5"

    print("All tests passed successfully.")