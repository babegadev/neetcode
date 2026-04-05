class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {char: s.count(char) for char in set(s)}
        t_map = {char: t.count(char) for char in set(t)}

        return s_map == t_map
        