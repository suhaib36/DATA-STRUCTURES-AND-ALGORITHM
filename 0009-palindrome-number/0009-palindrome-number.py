class Solution:
    def isPalindrome(self, x: int) -> bool:
        dup = x
        N = x

        b = 1
        if N < 0:
            return False
            x = -N
            b = -1
        else:
            x = N

        C = 0 
        while x > 0:
            last_digit = x % 10
            x = x // 10
            C = (C * 10) + last_digit

        return dup == C * b