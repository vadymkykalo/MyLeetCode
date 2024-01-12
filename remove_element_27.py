"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).

Constraints:

0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100
"""

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        j = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j

if __name__ == '__main__':
    solution = Solution()

    nums1 = [3, 2, 2, 3]
    val1 = 3
    expected1 = [2, 2]
    k1 = solution.removeElement(nums1, val1)
    assert k1 == len(expected1), f"Error in test case 1: Expected k={len(expected1)}, but got {k1}"
    assert sorted(nums1[:k1]) == sorted(expected1), f"Error in test case 1: Expected nums[:k]={expected1}, but got {sorted(nums1[:k1])}"

    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    val2 = 2
    expected2 = [0, 1, 3, 0, 4]
    k2 = solution.removeElement(nums2, val2)
    assert k2 == len(expected2), f"Error in test case 2: Expected k={len(expected2)}, but got {k2}"
    assert sorted(nums2[:k2]) == sorted(expected2), f"Error in test case 2: Expected nums[:k]={expected2}, but got {sorted(nums2[:k2])}"

    print("All tests passed successfully.")
