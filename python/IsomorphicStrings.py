
class Solution:
    def isIsomorphic(self, s, t):
        order_s = 0
        order_t = 0
        s_dict = {}
        t_dict = {}
        s_str = ""
        t_str = ""
        for i in range(0, len(s)):
            if s[i] not in s_dict:
                s_dict[s[i]] = order_s
                order_s += 1
            s_str += str(s_dict[s[i]])
            if t[i] not in t_dict:
                t_dict[t[i]] = order_t
                order_t += 1
            t_str += str(t_dict[t[i]])
        return s_str == t_str
