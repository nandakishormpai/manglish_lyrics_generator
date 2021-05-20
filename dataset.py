import torch
from collections import Counter
import os
import pickle



class Dataset():
    def __init__(self):
        self.words = self.load_words()
        text_file = open("data/words.txt", "w")
        text_file.write(" ".join(self.words))
        text_file.close()
        self.uniq_words = self.get_uniq_words()

        # index_to_word and word_to_index converts words to number indexes and visa versa.
        self.index_to_word = {index: word for index, word in enumerate(self.uniq_words)}
        self.word_to_index = {word: index for index, word in enumerate(self.uniq_words)}
        with open('data/index_to_word.json', 'wb') as iw:
            pickle.dump(self.index_to_word, iw)
        with open('data/word_to_index.json', 'wb') as wi:
            pickle.dump(self.word_to_index, wi)    
        

        self.words_indexes = [self.word_to_index[w] for w in self.words]

        self.sequence_length=100

    
    def load_words(self):
        """ Returns words [list] - list of words
        Open the files in the dataset, and for each file read its contents, 
        replace the endline with an ' <EOL> ' string and then split each 
        words by space. These words are then returned in a list.
        """
        files = os.listdir("data/lyrics")
        words = []
        for file in files:
            with open("data/lyrics/"+file,'r') as txtfile:
                lyrics = txtfile.read()
                lyrics = lyrics.replace("\n"," <EOL> ")
                words = words + lyrics.split(" ")
        return words

    # get a list of Unique words
    def get_uniq_words(self):
        word_counts = Counter(self.words)
        return sorted(word_counts, key=word_counts.get, reverse=True)

    def __len__(self):
        return len(self.words_indexes) - self.sequence_length

    def __getitem__(self, index):
        return (
            torch.tensor(self.words_indexes[index:index+self.sequence_length]),
            torch.tensor(self.words_indexes[index+1:index+self.sequence_length+1]),
        )
