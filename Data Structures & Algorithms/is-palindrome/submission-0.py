class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_s = "".join(c for c in s if c.isalnum()).lower()
        
        s_reversed = "".join(reversed(filtered_s))
        if filtered_s == s_reversed:
            return True
        return False