class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        newset = set()
        maxN = 0
        left = 0

        for right in range(len(s)):
            while s[right] in newset:
                newset.remove(s[left])
                left += 1
            newset.add(s[right])
            maxN = max(maxN, right - left +1)
        return maxN
        