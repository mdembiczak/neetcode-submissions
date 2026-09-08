class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_seen = dict()
        t_seen = dict()
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] in s_seen:
                s_seen[s[i]] = s_seen[s[i]] + 1
            else:
                s_seen[s[i]] = 1
            if t[i] in t_seen:
                t_seen[t[i]] = t_seen[t[i]] + 1
            else:
                t_seen[t[i]] = 1
        
        for key in s_seen:
            if key not in t_seen:
                return False
            if s_seen[key] != t_seen[key]:
                return False
            
        
        return True

        
        

            
        