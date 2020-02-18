#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#
# https://leetcode.com/problems/pascals-triangle/description/
#
# algorithms
# Easy (49.88%)
# Likes:    1062
# Dislikes: 88
# Total Accepted:    331.9K
# Total Submissions: 663.9K
# Testcase Example:  '5'
#
# Given a non-negative integer numRows, generate the first numRows of Pascal's
# triangle.
#
#
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it.
#
# Example:
#
#
# Input: 5
# Output:
# [
# ⁠    [1],
# ⁠   [1,1],
# ⁠  [1,2,1],
# ⁠ [1,3,3,1],
# ⁠[1,4,6,4,1]
# ]
#
#
#

# @lc code=start


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = []

        for rowNum in range(numRows):
            if rowNum == 0:
                rows.append([1])
                continue

            newRow = [1] * (rowNum + 1)
            for i in range(1, rowNum):
                newRow[i] = rows[rowNum - 1][i - 1] + rows[rowNum - 1][i]

            rows.append(newRow)

        return rows

        # @lc code=end
