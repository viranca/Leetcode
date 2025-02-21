class Solution:
    def mySqrt(self, x: int) -> int:
        for i in range(9999999):
            if i*i > x:
                return i-1