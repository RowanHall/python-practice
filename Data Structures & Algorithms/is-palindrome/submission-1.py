class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        alnum_s = ""
        for char in s:
            if char.isalnum():
                alnum_s = alnum_s + char
        s = alnum_s

        j = len(s)-1

        for i in range(len(s)):
            if s[i] != s[j]:
                return False
            j -= 1
        return True

