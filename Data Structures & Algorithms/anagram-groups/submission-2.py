class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # defaultdict creates default values for keys with no values
        # In this case, an empty list
        hash_strs = defaultdict(list)

        for word in strs:
            # Sorted always returns a list
            # Make it a string using ''.join(): join every item in the list with '' in between
            hash_strs[''.join(sorted(word))].append(word)
        
        return [item for item in hash_strs.values()]