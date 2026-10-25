class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        # Counter creates a dictionary-like object containing frequencies:
        # Counter({
        #    1: 5 <- 1 appears 5 times
        #    2: 8
        #    3: 4
        # })

        # .items() returns all the key value pairs as tuples
        # number is assigned to the first value of the tuple (the key)
        # frequency is assigned to the second value of the tuple (the value)
        # Tuple values can be accessed like lists, where index 0 = key and index 1 = value

        # key=lambda x: x[1] is applied to every tuple in the list (Counter(nums).items() is
        # wrapped in the list function), where the tuple itself (in this case: (key,
        # frequency)) is x and x[1] is freuquency

        # sorted(...)[:k] returns a list
        # The list comprehension becomes:
        # [number for number, frequency in (list from sliced sorted)]
        
        # We assign number, frequency even though frequency isn't used for unpacking the tuples
        return [number for number, frequency in sorted(list(Counter(nums).items()), key=lambda x: x[1], reverse=True)[:k]]