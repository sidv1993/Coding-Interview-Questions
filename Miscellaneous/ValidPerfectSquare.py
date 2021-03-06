# Given a positive integer num, write a function which returns True if num is a perfect square else False.
# Note: Do not use any built-in library function such as sqrt.
# Example 1:
# Input: 16
# Returns: True

# Example 2:
# Input: 14
# Returns: False

# KEY STEP: Using Newton-Raphson Method to find root.
# TC: O(log n)
# SC: O(1)

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        r = num
        while r*r > num:
            r = (r + num/r)/2
        return r*r == num