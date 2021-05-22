# 🎶 Sithara Song Generator 🎧

#### Manglish Lyrics Generator [Website](https://nandakishormpai.co/manglish_lyrics_generator/)  

  Our project submission to [TinkerHub Build From Home 2021 ](https://www.notion.so/Build-From-Home-by-TinkerHub-ab27844482524837aed175a57cf560cf). We choose the ML stack and chose [Sithara song generator](https://www.notion.so/ML3-Sithara-song-generator-f0b74faa46714a6f883285b0e6c79267) project.
  

## Contents of the Repository

**1. Model**
 - [model.py](./model/model.py)  contains the Model Class with Architecture of our model in PyTorch including LSTM.
 - [dataset.py](./model/dataset.py)  contains the Dataset class for Preprocessig and packaging of dataset from txt files into a usable form for DataLoader in PyTorch to fetch and supply samples in batches.
 - [train.py](./model/train.py) has the training script with parameters chose optimally after hypertuning and analysis.
 - [generate.py](./model/generate.py)  contains the basic testing script for evaluating the performance of the model
 - [train_notebook](./model/train_notebook/manglish_lyrics_generator.ipynb) contains the jupyter notebook used for training and validating the text generation model from data loading to generation.

**2. Scrapper**
 - Using Beautiful Soap a dataset was built with song name, film and lyrics URL from this [Source](https://www.malayalachalachithram.com/listsongs.php?tot=147&g=1414&p=1)
 - Dataset created was further used to fetch lyrics and stored them as txt files for training purposes 

**3. API**
 -    GET request is sent to the server hosted in Heroku at [https://manglish-lyrics-generator.herokuapp.com/](https://manglish-lyrics-generator.herokuapp.com/).
 -   Input for the text generation is provided internally by randomly selecting a seqeuence of 3 words from the dataset triggering the process and response is sent back.
 -   Trained model is included to be loaded for the same

      
      
**4. Frontend**
 - [Website](https://nandakishormpai.co/manglish_lyrics_generator/) built with HTML & CSS with JavaScript under the hood to Send Request to the API and display the response.
 
## Built With ❤️ 

* [Python3.6](https://docs.python.org/3.6/) - The programming language used
* [PyTorch](https://pytorch.org/) - The deep learning framework used
* [Flask](https://pypi.org/project/Flask/) - A light-weight web-application framework used


<br>

## Developers ✨


<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/nandakishormpai2001"><img src="https://avatars.githubusercontent.com/u/57388834?v=4" width="180px;" alt=""/><br /><sub><b>Nanda Kishor M Pai<br />NLP Model, API,<br />Scrapping & Web Dev</b></sub></a><br />
    <td align="center"><a href="https://github.com/aswinjayaji"><img src="https://avatars.githubusercontent.com/u/56126732?v=4" width="180px;" alt=""/><br /><sub><b>Ashwin Jayaji<br />Web Dev</b></sub></a><br />
      <td align="center"><a href="https://github.com/Harikrishnan6336"><img src="https://avatars.githubusercontent.com/u/53964426?v=4" width="180px;" alt=""/><br /><sub><b>Hari Krishnan U<br />NLP Model</b></sub></a><br />

