class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keys = {}
        for l in strs:
            added = False
            v = "".join(sorted(l))
            keys.setdefault(v, []).append(l)
        answer = []
        for m in keys:
            answer.append(keys[m])
        return answer
                