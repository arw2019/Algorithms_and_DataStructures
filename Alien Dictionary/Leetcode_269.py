class Solution:
    def alienOrder(self, words: List[str]) -> str:
        less = []
        for i in range(len(words)-1):
            word1, word2 = words[i], words[i+1]
            for j in range(min(len(word1), len(word2))):
                char1, char2 = word1[j], word2[j]
                if char1 != char2:
                    less += [char1 + char2]
                    break
      
                    
        chars = set(''.join(words))
        N = len(chars)
        order = []
        while less:
            free = chars - {pair[1] for pair in less}
            if not free: return ''
            order += free
            chars -= free
            less = [pair for pair in less if free.isdisjoint(pair)]
      
        return ''.join(order + list(chars))