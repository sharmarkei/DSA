class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict_1 = {}
        
        for i in s:
            if i not in dict_1:
                dict_1[i] = 1
            else: 
                dict_1[i] += 1
        
        print(dict_1)
        
        for idx, val in enumerate(s):
            if dict_1[val] == 1:
                return idx

        return -1
        