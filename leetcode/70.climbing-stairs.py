#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#
# https://leetcode.com/problems/climbing-stairs/description/
#
# algorithms
# Easy (46.05%)
# Likes:    3328
# Dislikes: 109
# Total Accepted:    564.5K
# Total Submissions: 1.2M
# Testcase Example:  '2'
#
# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can
# you climb to the top?
#
# Note: Given n will be a positive integer.
#
# Example 1:
#
#
# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
#
#
# Example 2:
#
#
# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
#
#
#

# @lc code=start

import math


class Solution:
    def climbStairs(self, n: int) -> int:
        sum = 0
        k = 0
        while n >= k:
            sum += math.factorial(n) // math.factorial(k) // math.factorial(n - k)
            n -= 1
            k += 1

        return sum

# @lc code=end

# the question is really given a number n, how many permutations are
# there for summing up to n, with the constraint that you can only use
# 1 and 2, and that obviously order matters.
# another way to look at it is, assume the 'background' is 1's, then how
# many ways can you put 2's in there to create the same sum.
# all 1's, all 1's with one 2 in each possible position, all 1's with two
# 2's in each possible position, etc. this is close to a binary string
# thing with a constraint. given n=10 we have a maximum two's string of
# 2,2,2,2,2. the number of twos could then be a binary string: 11111 (all
# two's are activated). if we replace a two with 2 1's, then there would
# be a zero. So 1,1,2,2,2,2 -> 01111. not quite sufficient though to just
# count the perms of the binary string, this would undercount. but a
# binary string representing the 1's would overcount. for 11111 there is
# one way to arrange those. for 01111 we have all two's and two 1's, so
# it's all the ways you can arrange that string. so on.

# take a string of all 1's. that is one arrangement. now take a pair of
# ones and bind them up as a two. now slide that couple down the array.
# each possible spot is another arrangement. so the count there is n-1.
# now we bind up two pairs of ones. the count would be n-2 (I think), but
# we have to subtract for the fact that these two couples are identical so
# AB = BA where A and B are both 1 couples.

# it is binomial coefficients. nCr. solution is nC0 + (n-1 C 1) + (n-2 C
# 2) + ... + (n/2 C n/2).
