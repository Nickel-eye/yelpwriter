class Markov(object):
    """A class that analyzes the word occurance patterns of a given
    text file (the corpus) and can generate random text in the style
    of that corpus."""

    def __init__(self, corpus_file):
        self.corpus = open(corpus_file)
        self.text = self.corpus.read()
        self.words = self.text.split()

    def make_ngrams(self, n, inputlist):
        """Make ngrams of every n consecutive
        words to feed the dictionary function, AS LIST."""
        for x in range(0, len(inputlist)-n):
            yield [inputlist[x+i] for i in range(n)]

    def make_dictionary(self, n, inputlist=None):
        """For every ngram, takes first n-1 words as key, and last as value."""

        # TODO: make case/punct-insensitive?
        if inputlist is None:
            inputlist = self.words

        temp_dict = defaultdict(list)
        for wordlist in self.make_ngrams(n, inputlist):
            final_word = wordlist.pop()
            temp_dict[tuple(wordlist)].append(final_word)

        return temp_dict

    def generate(self, length=100, n=3):
        """Make random text of given length (using ngrams of the given n)."""
        word_dict = self.make_dictionary(n)
        seed_no = randint(0,len(self.words)-n) # choose random seed
        output = [self.words[seed_no+x] for x in range(n-1)]
        for x in range(n-1, length):
            next_key = tuple(output[-(n-1):])
            output.append(choice(word_dict[next_key]))

        return " ".join(output)
