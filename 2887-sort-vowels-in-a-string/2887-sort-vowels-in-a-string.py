class Solution:
    def sortVowels(self, s: str) -> str:
        vowelKey = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
        vowelSet = set(vowelKey)
        vowel2num = defaultdict(int)
        t = []

        for i, v in enumerate(s):
            if v in vowelSet:
                t.append('')
                vowel2num[v] += 1
            else:
                t.append(v)
        
        currKeyId = 0

        for i in range(len(t)):
            if t[i] != '':
                continue
            while vowelKey[currKeyId] not in vowel2num:
                currKeyId += 1
            
            t[i] = vowelKey[currKeyId]
            vowel2num[t[i]] -= 1
            if vowel2num[t[i]] == 0:
                vowel2num.pop(t[i])

        return ''.join(t)