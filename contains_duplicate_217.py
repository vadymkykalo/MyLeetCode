"""
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        tmp = set([])
        for i in nums:
            if i in tmp:
                return True
            tmp.add(i)
        return False

if __name__ == '__main__':
    solution = Solution()

    assert solution.containsDuplicate([2, 7, 11, 15]) == False, "Test case 1 failed"
    assert solution.containsDuplicate([3, 2, 4]) == False, "Test case 2 failed"
    assert solution.containsDuplicate([3, 3]) == True, "Test case 3 failed"

    print("All tests passed successfully.")