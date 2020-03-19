#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#
# https://leetcode.com/problems/count-primes/description/
#
# algorithms
# Easy (30.52%)
# Likes:    1586
# Dislikes: 517
# Total Accepted:    308.9K
# Total Submissions: 1M
# Testcase Example:  '10'
#
# Count the number of prime numbers less than a non-negative number, n.
#
# Example:
#
#
# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
#
#
#

# @lc code=start


class Solution:
    # this is not my code! this was taken from SO
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        sieve = [True] * n
        for i in range(3, int(n**0.5) + 1, 2):
            if sieve[i]:
                sieve[i * i::2 * i] = [False] * \
                    ((n - i * i - 1) // (2 * i) + 1)
        return len([2] + [i for i in range(3, n, 2) if sieve[i]])


# @lc code=end
