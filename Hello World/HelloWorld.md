# Getting Started with Machine Learning

So, this section explains us to use Machine Learning to classify (categorize) Iris flowers by species. 
Well, in the programing cummunity we often refer 'Iris Flower Classification' problem as the 'Hello World' of Machine Learning.
This document will help you to dive deeply into the TensorFlow code to do exactly that, explaining ML fundamentals along the way.

If the following list describes you, then you are in the right place:

- You know little to nothing about machine learning.
- You want to learn Tensorflow
- You can code (atleast a little) in Python.

## The Iris Classification Problem

The problem is to write a program which can help us to classify the given Iris plant to it's respective species. 
But our ambitions are more modest--we're going to classify Iris flowers based solely on the length and width of their *sepals* and *petals*. For fact, the Iris family has about 300 species but right now we would deal with three of them. 
![alt text](MachineLearning/samples.png)

- Iris Setosa
- Iris Virginica
- Iris Versicolor

Okay, we are clear with the Problem Statement, so now you don't know anythin about ML and decide to write a program which does that and you started writing down all the **variables** which make a flower, flower. But ta-da there are many many many variables that contribute in making of a flower which unfortunately you can not take into account. To ease that, we use **Machine Learning**.
The difference is that, now we don't tell everything (like we used to do in *classical programs*) to the program. Infact, we don't tell anything to the program about the flower. Infact we don't tell it anything about the flower. We give it some related data of Iris Flower and train it on the basis of it and later we feed it with some input and ask the program to tell us that is it the flower we are looking for.
For a start, we already have a well-labeled dataset of 120 Iris flower of these three different species with the sepal and petal measurements. The dataset is avaiable already in the repo, and you could easily find over the internet.
Following is a sample dataset.
![alt text](MachineLearning/Table.png)

Before getting our hands dirty, let's get introduced with some common terms:
- The last column (species) is called the label; the first four columns are called features. Features are characteristics of an example, while the label is the thing we're trying to predict.
- An example consists of the set of features and the label for one sample flower. The preceding table shows 5 examples from a data set of 120 examples.

Each label is naturally a string (for example, "setosa"), but machine learning typically relies on numeric values. Therefore, someone mapped each string to a number. Here's the representation scheme:
- 0 represents Setosa
- 1 represents Versicolor
- 2 represents Virginica

## Models and Training

A model is the relationship between features and the label. For the Iris problem, the model defines the relationship between the sepal and petal measurements and the Iris species. Some simple models can be described with a few lines of algebra; more complex machine learning models contain such a large number of interlacing mathematical functions and parameters that they become hard to summarize mathematically.

Could you determine the relationship between the four features and the Iris species without using machine learning? That is, could you use traditional programming techniques (for example, a lot of conditional statements) to create a model? Maybe. You could play with the data set long enough to determine the right relationships of petal and sepal measurements to particular species. However, a good machine learning approach determines the model for you. That is, if you feed enough representative examples into the right machine learning model type, the program will determine the relationship between sepals, petals, and species.

Training is the stage of machine learning in which the model is gradually optimized (learned). The Iris problem is an example of supervised machine learning in which a model is trained from examples that contain labels. (In unsupervised machine learning, the examples don't contain labels. Instead, the model typically finds patterns among the features)
