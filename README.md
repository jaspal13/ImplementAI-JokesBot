# ImplementAI-JokesBot
Our jokes bot for the implementAI hackathon

## Inspiration
The only people that ever said Roberto the Bot was funny were his mom and his 6 year old brother. He wanted to know for sure which jokes were funny and which were not, so he turned to machine learning for help.

## What it does
A user can chat with Robert and he will tell them jokes. Robert will them ask for a picture of the user’s reaction. Robert will use its fancy-pants machine learning model to determine if the user is smiling or not, and therefore if they liked the joked. Robert then ranks his jokes based on how many people like them or not.

## How we built it
First we used a web crawler to gather many pictures of people smiling, with neutral expressions or sad. Then we wrote a Python program using OpenCV to identify the faces in the pictures, crop them and format them to a size that our model can accept.

Our classifier model was built using keras library with a tensorflow backend and used a Convolutional Neural Network to classify faces as smiling, neutral or sad. We trained our model using the CNN (9 layers) and achieved an accuracy of 65% despite hardware bottlenecks. For our training data we used the faces obtained from crawling as well as a [kaggle dataset] (https://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge/data). We used approximately 16200 for training and 6000 for testing.

The chatbot is written in flask as backend and hosted on the google app engine server. Every time the user sends a message to Facebook messenger, Facebook calls a web-hook which invokes our api. The jokes were handpicked and is stored on a separate server; based on the user reaction to the joke, the specific joke gets a weight. The more funny reactions a joke gets, the joke gets ranked higher hence “Roberto” becomes wittier the next time.

## Challenges we ran into
* Integrating OpenCV and calibrating to detect faces without too many false positives
* Creating the CNN model and training it on limited hardware
* Optimizing the hyper parameters for the CNN model
* Initially we wanted to use firebase to store our jokes, but we ran into google app engine platform issue with our python firebase library. It took a lot of our time and we couldn’t hack it to make it work so we used our own server to host the data.

## Accomplishments that we’re proud of
* Facial detection works without too many false positives
* Our CNN model has an accuracy of 65%
* Created a chatbot who is smart enough to detect faces, and becomes funnier as we use it

## What we learned
* Integrating OpenCV with a Python script
* Deploying a Facebook chat bot using the Google App Engine
* Crawling the web for pictures using Python
* Using a CNN to detect happy, neutral or sad facex

## What’s next for Robert the JokesBot
* More jokes
* Better NLU
* Higher accuracy in the smile detection algorithm
