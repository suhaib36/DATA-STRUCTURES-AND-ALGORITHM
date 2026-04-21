class Solution:
    def reverse(self, x: int) -> int:
        c = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x > 0:
            last_digit = x % 10
            x = x // 10
            c = (c * 10) + last_digit

        c = sign * c

        # 32-bit overflow check
        if c < -2**31 or c > 2**31 - 1:
            return 0

        return c