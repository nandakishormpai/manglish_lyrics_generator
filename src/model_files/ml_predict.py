import torch
import numpy as np
from torch import nn
import random
import pickle
from collections import Counter

# Model class to define the architecture
class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        # Defining lstm parameters
        self.lstm_size = 128
        self.embedding_dim = 128
        self.num_layers = 2

        # Loading Corpus 
        words_file = open("model_files/data/words.txt","r")
        words = words_file.read().split(" ")
        word_counts = Counter(words)
        n_vocab = len(word_counts)

        # Defining Leyers
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

    # init_state returns tensors to initialize inputs for the Model
    def init_state(self, sequence_length):
        return (torch.zeros(self.num_layers, sequence_length, self.lstm_size),
                torch.zeros(self.num_layers, sequence_length, self.lstm_size))


# to avoid gradients update
@torch.no_grad()
def generate(model,keyword,next_words=100):
    # loading lyrics corpus
    words_file = open("model_files/data/words.txt","r")
    words = words_file.read().split(" ")

    # returning failed message as keyword not in dataset
    if (keyword not in words):
        while True:
            n = random.randint(0,len(words))
            message = "Keyword not found in dataset, try words like"+" ".join(words[n:n+3])
            if("<EOL>" not in message and "(" not in message and ")" not in message):
                return message

    loaded_model = model
    loaded_model.load_state_dict(torch.load("model_files/manglish_model.pth"))
    loaded_model.eval()
    words = []
    words.append(keyword)

    state_h, state_c = model.init_state(1)

    # Loading dictionaries for word to index and vice versa 
    with open('model_files/data/word_to_index.json', 'rb') as wi:
        word_to_index = pickle.load(wi)
    with open('model_files/data/index_to_word.json', 'rb') as iw:
        index_to_word = pickle.load(iw)
    # for loop to generate lyrics with 100 words
    for i in range(0, next_words):
        x = torch.tensor([[word_to_index[w] for w in words[i:]]])
        y_pred, (state_h, state_c) = loaded_model(x, (state_h, state_c))

        last_word_logits = y_pred[0][-1]
        p = nn.functional.softmax(last_word_logits, dim=0).detach().numpy()
        word_index = np.random.choice(len(last_word_logits), p=p)
        words.append(index_to_word[word_index])
    
    lyrics = " ".join(words)
    # formatting the lyrics
    lyrics = lyrics.replace(" <EOL> ","\n")
    lyrics = lyrics.replace("<EOL> ","\n")
    lyrics = lyrics.replace(" <EOL>","\n")

    words_file.close()
    # returning as a string
    return lyrics

if __name__ == "__main__":
    model = Model()
    lyrics = generate(model,"Ishtam")
    print(lyrics)
