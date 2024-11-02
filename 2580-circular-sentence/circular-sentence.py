class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if sentence[-1]!=sentence[0]:
            return False
        words = sentence.split()
        for idx, word in enumerate(words):
            if idx==len(words)-1:
                continue
            if word[-1]!=words[idx+1][0]:
                return False
        return True