![BFH Banner](https://trello-attachments.s3.amazonaws.com/542e9c6316504d5797afbfb9/542e9c6316504d5797afbfc1/39dee8d993841943b5723510ce663233/Frame_19.png)

# Sithara Song Generator 

### A Manglish lyrics generator that can give you Lyrics of a Malayalam Song that doesn't exist! in our favourite Manglish language. When User requests for one, API call is sent and pretrained model generates a lyrics and it is returned as response and displayed for you using JavaScript. 

### You can view the website [here](https://nandakishormpai.co/manglish_lyrics_generator/)

<!-- #### Data Collection

At First we scraped the lyrics(in manglish language) of Sitara songs from the internet. We used this [website](https://www.malayalachalachithram.com/listsongs.php?tot=147&g=1414&p=1) to scrape them and organized the lyrics in separate text files for training and validation. We used Beautiful Soup for web scraping. The source code regarding the same can be found in [scrapper](https://github.com/nandakishormpai2001/manglish_lyrics_generator/tree/main/scrapper) folder.

#### Data Preprocessing and Text Generation model

Minimal Data Preprocessing was done on the collected dataset, as more would have result in the loss of song structure. We split the data into train and validation in the ratio 85:15. A Deep Learning model with an architecture with an Embedding layer, LSTMs and fully connected layers were built using PyTorch and the dataset was trained on the model. We obtained a validation CrossEntropyLoss of `3.325`. Since the training was RAM intensive, it was carried out in Goole Colab and the jupyter notebook used for training and validation can be found [here](https://github.com/nandakishormpai2001/manglish_lyrics_generator/blob/main/model/train_notebook/manglish_lyrics_generator.ipynb)

#### Model Validation

The Validation Loss, was found out and was compared with the number of epochs, using suitable plot diagrams drawn with matplotlib. Required Hypertuning of parameters was done by varying batch size, number of epochs and learning rate. 

The source code regarding the model can be found in [model](https://github.com/nandakishormpai2001/manglish_lyrics_generator/tree/main/model) folder

#### Website and API

The backend was built on the micro-web framework Flask and it contains a function to handle GET request. The lyrics generation script and the model was used. The model was deployed onto Heroku after testing it locally. A website was built on  HTML, CSS, JS along with axios module for API request and response. Then the GET request is sent to the server hosted in Heroku at [api](https://manglish-lyrics-generator.herokuapp.com/.). The demo website is hosted in GitHub Pages and can be found [here](https://nandakishormpai.co/manglish_lyrics_generator/).
 -->
## Team members
1. [Nanda Kishor M Pai](https://github.com/nandakishormpai2001)
2. [Aswin Jayaji](https://github.com/aswinjayaji)
3. [Hari Krishnan U](https://github.com/Harikrishnan6336)


## Team Id

BFH/recEHiCGthePHSlQQ/2021

## Link to product walkthrough

#### Watch the video by clicking image below
<a href="https://drive.google.com/file/d/1yuChJ6B_Xx4VtguGs3tod4iI556RzEOZ/view?usp=sharing"   title="Product Walkthrough" target="_blank" ><img src="https://github.com/nandakishormpai2001/manglish_lyrics_generator/blob/frontend/images/walk.jpg" alt="Product Walkthrough" /></a>
<!-- {% gdrive %} https://drive.google.com/file/d/1yuChJ6B_Xx4VtguGs3tod4iI556RzEOZ/view?usp=sharing {% gdrive %} -->

## How it Works ?

1. The project website can be found [here](https://nandakishormpai.co/manglish_lyrics_generator/). A manglish lyrics gets generated when the user clicks the `Generate Lyrics` button and the lyrics gets cleared when the user uses the `Clear` button. The website was built using HTML, CSS and JS along with axios module for API request and response. On pressing the `Generate Lyrics` button, an API GET request gets called which returns the lyrics. The API is built on the micro-web framework Flask. The ML model along with the prediction script is incorporated into Flask and deployed onto Heroku after testing it locally. The api can be found [here](https://manglish-lyrics-generator.herokuapp.com/.). The source code regarding the api and website can be found in the [api](https://github.com/nandakishormpai2001/manglish_lyrics_generator/tree/main/api) and [frontend](https://github.com/nandakishormpai2001/manglish_lyrics_generator/tree/main/frontend) folders respectively.

      The dataset collected was splitted into train and validation in the ratio 85:15.  Minimal Data Preprocessing was done on the collected dataset, as more would have result in the loss of song lyrics structure. A Deep Learning model with an architecture including an Embedding layer, LSTMs and fully connected layers were built using PyTorch and the model was trained on the dataset. We obtained a validation CrossEntropyLoss of `3.325`. Since the training was RAM intensive, it was carried out in Goole Colab and the jupyter notebook used for training and validation can be found [here](https://github.com/nandakishormpai2001/manglish_lyrics_generator/blob/main/model/train_notebook/manglish_lyrics_generator.ipynb). The Validation Loss, was found out and was compared with the number of epochs, using suitable plot diagrams drawn with matplotlib. Required Hypertuning of parameters was done by varying batch size, number of epochs and learning rate. The source code regarding the model can be found in [model](https://github.com/nandakishormpai2001/manglish_lyrics_generator/tree/main/model) folder.
      
    
      For collecting the dataset, we scraped the lyrics (in manglish) of Sitara songs from the internet. We used this [website](https://www.malayalachalachithram.com/listsongs.php?tot=147&g=1414&p=1) to scrape them and organized the lyrics in separate text files for training and validation. We used Beautiful Soup for web scraping. The source code regarding the same can be found in [scrapper](https://github.com/nandakishormpai2001/manglish_lyrics_generator/tree/main/scrapper) folder.
      
      
## Live Demo

#### Watch the video by clicking image below

<a href="https://drive.google.com/file/d/1gCWtwgyNxcLD44HN93TPg5_brlaXxbWy/view?usp=sharing" target="_blank" title="Live Demo"><img src="https://github.com/nandakishormpai2001/manglish_lyrics_generator/blob/frontend/images/demo.jpg" alt="Live Demo" /></a>

<!-- {% gdrive %} https://drive.google.com/file/d/1gCWtwgyNxcLD44HN93TPg5_brlaXxbWy/view?usp=sharing {% gdrive %} -->

## Libraries used
      

  - pandas - 1.2.4

  - numpy - 1.20.3

  - torch - 1.8.0+cpu

  - matplotlib - 3.4.2

  - flask - 2.0.0

  - gunicorn - 20.1.0

  - beautifulsoup4 - 4.9.3

## How to configure

Inorder to train the model, load the python jupyter notebook found [here](https://colab.research.google.com/drive/1vgdj1Y2Vqwn8QgV4QOd0famMZbwp0Q9-?usp=sharing) in a Google Colab and make a copy of it for your use.

## How to Run

After configuring the project as above mentioned, Run cells of the notebook in chronological order and download the model after training. 

To see the Live demo, try this [website](https://nandakishormpai.co/manglish_lyrics_generator/).
