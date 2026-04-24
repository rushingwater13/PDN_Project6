from mrjob.job import MRJob
import re

WORD_RE = re.compile(r"[A-Za-z']+")
#WORD_RE = re.compile(r"[\w']+")


class MRLongestWords(MRJob):

        def mapper(self, _, line):
            # for each word, sort by first letter
            for word in WORD_RE.findall(line):
                word = clean(word)

                if word and word[0].isalpha():
                    yield word[0], word


        def combiner(self, letter, words):
            # find the longest length
            words = list(words)
            maxLength = 0
            for word in words:
                if len(word) > maxLength:
                    maxLength = len(word)

            # find the words with that longest length
            for word in words:
                 if len(word) == maxLength:
                    yield letter, word


        def reducer(self, letter, words):
            # find the longest length
            words = list(words)
            maxLength = 0
            for word in words:
                if len(word) > maxLength:
                    maxLength = len(word)

            # find the words with that longest length
            longest = []
            for word in words:
                 if len(word) == maxLength:
                      longest.append(word)
                    
            longest = list(set(longest))
            yield letter, longest


def clean(word):
    return word.strip(".,!?:;\"'()[]{}_—”“").lower()


if __name__ == '__main__':
    MRLongestWords.run()
