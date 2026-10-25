class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hash_s = defaultdict(int)

        for i in range(len(s)):
            hash_s[s[i]] += 1
            hash_s[t[i]] -= 1

        # All values in hash_s must be 0
        return all(count == 0 for count in hash_s.values())