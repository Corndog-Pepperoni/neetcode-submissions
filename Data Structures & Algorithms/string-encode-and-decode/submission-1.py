class Solution:

    def encode(self, strs: List[str]) -> str:
        # Create an empty string representing the encoded list
        encoded = ''

        # Go through every word in the str list
        for word in strs:
            # '#' indicates a new word
            # len(word) tells us how many characters after '#' the
            # string persists
            # word is the current word
            encoded += f'{len(word)}#{word}'
        return encoded
        
    def decode(self, s: str) -> List[str]:
        decoded = []
        # i represents the start of a length or the word itself
        i = 0

        # Until we hit the beginning of the end
        while i < len(s):
            # j represents the end of the length or the word itself
            # Will be used for slicing s
            j = i

            # Until j finds a '#'
            while s[j] != '#':
                j += 1

            # Slice s to find the length and turn it into an int
            length = int(s[i:j])

            # Set i to be after j to mark the start of the word itself
            i = j + 1
            # Move j to be after the end of the word itself for slicing
            # i marks the start of the word and adding length puts j after the end of the word
            j = i + length

            # Slice s with the new i and j vals to parse the word itself and append it to the
            # decoded str
            decoded.append(s[i:j])

            # Set i at the same spot as j to mark the start of a new length
            i = j

        return decoded