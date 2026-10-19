class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nel = Counter(nums)
        buckets = {}
        freq = []
        answer = []
        for n in nel:
            if nel[n] not in buckets:
                buckets[nel[n]] = [n]
                freq.append(nel[n])
            else:
                buckets[nel[n]].append(n)
        freq = sorted(freq, reverse=True)
        for f in freq:
            for n in buckets[f]:
                answer.append(n)
                if len(answer) == k:
                    return answer