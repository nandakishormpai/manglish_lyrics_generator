# 🎶 Sithara Song Generator 🎧

#### Manglish Lyrics Generator

  Our project submission to [TinkerHub Build From Home || ML track](https://www.notion.so/Build-From-Home-by-TinkerHub-ab27844482524837aed175a57cf560cf). We choose the ML stack and chose [Sithara song generator](https://www.notion.so/ML3-Sithara-song-generator-f0b74faa46714a6f883285b0e6c79267) project.
  

## Contents of the Repository

**1. model**
 - [model.py](./model/model.py)  contains the Model Class with Architecture of our model in PyTorch including LSTM.
 - [dataset.py](./model/dataset.py)  contains the Dataset class for Preprocessig and packaging of dataset from txt files into a usable form for DataLoader in PyTorch to fetch and supply samples in batches.
 - [train.py](./model/train.py) has the training script with parameters chose optimally after hypertuning and analysis.
 - [generate.py](./model/generate.py)  contains the basic testing script for evaluating the performance of the model
 - [train_notebook](./model/train_notebook/manglish_lyrics_generator.ipynb) contains the jupyter notebook used for training and validating the text generation model from data loading to generation.

**2. scrapper**
 - Using Beautiful Soap a dataset was built with song name, film and lyrics URL from this [Source](https://www.malayalachalachithram.com/listsongs.php?tot=147&g=1414&p=1)
 - Dataset created was further used to fetch lyrics and stored them as txt files for training purposes 

**3. api**
 -    GET request is sent to the server hosted in Heroku at [https://manglish-lyrics-generator.herokuapp.com/](https://manglish-lyrics-generator.herokuapp.com/).
 -   Input for the text generation is provided internally by randomly selecting a seqeuence of 3 words from the dataset triggering the process and response is sent back.
 -   Trained model is included to be loaded for the same

      
      
**4. Front end**
 - [Website](https://nandakishormpai.co/manglish_lyrics_generator/) built with HTML & CSS with JavaScript under the hood to Send Request to the API and display the response.
 


