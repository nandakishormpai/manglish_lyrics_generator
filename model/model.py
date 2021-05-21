import torch
from torch import nn
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
        words_file = open("data/words.txt","r")
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


