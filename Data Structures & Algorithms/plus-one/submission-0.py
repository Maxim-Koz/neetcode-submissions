class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
            d = digits
            d.reverse()
            d[0] += 1
            for i in range(len(d)):
                if d[i] == 10:
                    d[i] = 0
                    if i != len(d)-1:
                        d[i+1] += 1
                    else:
                        d.append(1)
            d.reverse()
            return d
    