class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        maintain a dict with key value of
            freq of char as a tuple : list of strings with that freq

        return that dict.values()    
        '''

        groups = {}

        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord('a')] += 1
            signature = tuple(freq)
            if signature not in groups:
                groups[signature] = []
            groups[signature].append(s)

        return list(groups.values())            
