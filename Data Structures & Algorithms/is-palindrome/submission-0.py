class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumerical = "".join(char for char in s if char.isalnum()).lower()

        for i in range(round(len(alphanumerical) / 2)):
            if alphanumerical[i] != alphanumerical[-i - 1]:
                return False

        return True