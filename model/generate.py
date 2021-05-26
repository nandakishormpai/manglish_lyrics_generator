import torch
import numpy as np
import random
import pickle

from model import Model

# to avoid gradients update
@torch.no_grad()
def generate(model,keywords,next_words=100):
    # loading lyrics corpus
    words_file = open("data/words.txt","r")
    words = words_file.read().split(" ")

    # returning failed message as keyword not in dataset
    for keyword in keywords.split(" "):
        if (keyword not in words):
            while True:
                n = random.randint(0,len(words))
                message = '"'+keyword+'" Keyword not found in dataset. Try words like '+", ".join(words[n:n+3])
                if("<EOL>" not in message and "(" not in message and ")" not in message):
                    return message

    loaded_model = model
    loaded_model.load_state_dict(torch.load("MODEL-NAME-HERE.pth"))
    loaded_model.eval()
    words = keywords.split(" ")

    state_h, state_c = model.init_state(len(words))

    # Loading dictionaries for word to index and vice versa 
    with open('data/word_to_index.json', 'rb') as wi:
        word_to_index = pickle.load(wi)
    with open('data/index_to_word.json', 'rb') as iw:
        index_to_word = pickle.load(iw)
    # for loop to generate lyrics
    for i in range(0, next_words):
        x = torch.tensor([[word_to_index[w] for w in words[i:]]])
        y_pred, (state_h, state_c) = loaded_model(x, (state_h, state_c))

        last_word_logits = y_pred[0][-1]
        p = nn.functional.softmax(last_word_logits, dim=0).detach().numpy()
        word_index = np.random.choice(len(last_word_logits), p=p)
        words.append(index_to_word[word_index])
    
    # print(len(words),words[50],words[100])
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
    lyrics = generate(model,"oru Ishtam")
    print(lyrics)
