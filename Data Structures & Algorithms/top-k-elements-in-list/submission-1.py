class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0)+1
        top_k = sorted(freq, key = freq.get, reverse = True)[:k]
        return top_k