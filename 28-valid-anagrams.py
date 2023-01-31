# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# easy
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        hashmap1 = {}
        hashmap2 = {}

        for i in range(len(s)):
            hashmap1[s[i]] = 1 + hashmap1.get(s[i], 0)
            hashmap2[t[i]] = 1 + hashmap2.get(t[i], 0)
        for c in hashmap1:
            if hashmap1[c] != hashmap2.get(c,0):
                return False
        return True