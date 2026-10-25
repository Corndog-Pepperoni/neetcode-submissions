class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return [[""]]
        elif len(strs) == 1:
            return [[strs[0]]]

        # defaultdict creates default values for keys with no values
        # Accessing a key with no value in a regular dict throws an error
        # defaultdict automatically sets that key with no value to a default value you assign
        # In this case, an empty list []
        hash_strs = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            # Tuple = fixed version of a list; not dynamic (can't add, remove, change values)
            # Dicts only take immutable keys so that they cannot be changed
            hash_strs[tuple(count)].append(word)
        
        return [value for value in hash_strs.values()]
