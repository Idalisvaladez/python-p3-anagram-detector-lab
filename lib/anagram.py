class Anagram:

    def __init__(self, word):
        self.word = word

    def match(self, word):
            return [word for word in word if sorted(self.word) == sorted(word)]
            