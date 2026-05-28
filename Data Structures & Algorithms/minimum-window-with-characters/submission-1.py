class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        slilding window
        keep moving i right until we have all three, 
            then keep shortening the window until window is no longer valid

        we can keep track if window is valid by using freq map of T and 
            checking it against freq map of our window    
        '''
        res = ''
        # Build t freq map
        freq_t = {}
        freq_s = {}
        for char in t:
            freq_t[char] = 1 + freq_t.get(char, 0)
            freq_s[char] = 0
        
        def is_valid():
            for char in freq_t:
                if freq_s[char] < freq_t[char]:
                    return False
            return True

        l = 0  
        for r in range(len(s)):
            if s[r] in freq_s:
                freq_s[s[r]] += 1
            while is_valid():
                if res == '':
                    res = s[l:r+1]
                else:
                    res = s[l:r+1] if len(res) > (r - l + 1) else res
                if s[l] in freq_s:
                    freq_s[s[l]] -= 1
                l += 1    
        return res