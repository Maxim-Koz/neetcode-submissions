class Solution:
    def isHappy(self, n: int) -> bool:
        n = n
        s = set()
        while True:
            sum = 0
            for l in str(n):
                sum += (int(l)**2)
            if sum == 1:
                return True
            elif sum in s:
                return False
            n = sum
            s.add(n)