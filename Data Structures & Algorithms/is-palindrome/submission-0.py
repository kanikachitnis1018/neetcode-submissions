class Solution:
    def isPalindrome(self, s: str) -> bool:
        listed = list(s.lower())
        n = len(listed)
        start = 0 
        end = n - 1
        while start < end:
            if not listed[start].isalnum():
                start += 1
            elif not listed[end].isalnum():
                end -= 1
            elif listed[start] != listed[end]:
                return False
            else:
                start += 1
                end -= 1
        return True