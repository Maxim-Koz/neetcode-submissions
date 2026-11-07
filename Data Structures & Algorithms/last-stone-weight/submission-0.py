class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        ans = stones
        while True:
            ans.sort(reverse=True)
            if len(ans) == 1:
                return ans[0]
            elif len(ans) == 0:
                return 0
            temp = ans[0] - ans[1]
            ans = ans[2:]
            ans.append(temp)