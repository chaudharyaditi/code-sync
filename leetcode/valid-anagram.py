class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # first try runtime wayyy too long
        # seen = []
        # if len(s) != len(t):
        #     return False #idk if we assume this or not

        # for i in range(len(s)):
        #     seen.append(s[i]) #create set of letters

        # for i in range(len(t)):
        #     if t[i] not in seen:
        #         return False
        #     else:
        #         seen.remove(t[i]) #removes first occurence
        # return True

        if len(s) != len(t):
            return False
        count = [0]*26
        for ch in s:
            count[ord(ch)-ord('a')] += 1
        for ch in t:
            idx = ord(ch) - ord('a')
            count[idx] -= 1
            if count[idx] < 0:
                return False
        return True