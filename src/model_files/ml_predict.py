import torch
import numpy as np
from torch import nn
import os
import random
import pickle
from collections import Counter
# from torch.utils.data import DataLoader
# from collections import Counter
# import pandas as pd

class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.lstm_size = 128
        self.embedding_dim = 128
        self.num_layers = 3

        words_file = open("model_files/data/words.txt","r")
        words = words_file.read().split(" ")
        word_counts = Counter(words)

        n_vocab = len(word_counts)
        self.embedding = nn.Embedding(
            num_embeddings=n_vocab,
            embedding_dim=self.embedding_dim,
        )
        self.lstm = nn.LSTM(
            input_size=self.lstm_size,
            hidden_size=self.lstm_size,
            num_layers=self.num_layers,
            dropout=0.2,
        )
        self.fc = nn.Linear(self.lstm_size, n_vocab)

    def forward(self, x, prev_state):
        embed = self.embedding(x)
        output, state = self.lstm(embed, prev_state)
        logits = self.fc(output)
        return logits, state

    def init_state(self, sequence_length):
        return (torch.zeros(self.num_layers, sequence_length, self.lstm_size),
                torch.zeros(self.num_layers, sequence_length, self.lstm_size))



@torch.no_grad()
def generate(model,next_words=150):
    words_file = open("model_files/data/words.txt","r")
    words = words_file.read().split(" ")
    
    n = random.randint(0,len(words))
    text = " ".join(words[n:n+3])

    loaded_model = torch.load('model_files/manglish_model.h5')
    loaded_model.eval()
    words = text.split(' ')

    state_h, state_c = model.init_state(3)

    with open('model_files/data/word_to_index.json', 'rb') as wi:
        word_to_index = pickle.load(wi)
    with open('model_files/data/index_to_word.json', 'rb') as iw:
        index_to_word = pickle.load(iw)

    for i in range(0, next_words):
        x = torch.tensor([[word_to_index[w] for w in words[i:]]])
        y_pred, (state_h, state_c) = loaded_model(x, (state_h, state_c))

        last_word_logits = y_pred[0][-1]
        p = torch.nn.functional.softmax(last_word_logits, dim=0).detach().numpy()
        word_index = np.random.choice(len(last_word_logits), p=p)
        words.append(index_to_word[word_index])
    lyrics = " ".join(words)
    lyrics = lyrics.replace("<EOL>","\n")
    words_file.close()
    return lyrics
