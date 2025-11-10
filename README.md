# Python-Projects

You can find some AI-Related projects here in this repository. New projects will be added, and this file will be updated accordingly.


1) Sigmoid Function: This is a sort of mini neural network, a 2-layerd freeforward one. It relies on the Sigmoid Function to introduce non-linearity during learning. It also calculates error gradients (delta) during backpropagation, where the network how much each weight (number that controls how much influence one neuron has on a different one) contributes to the error and how much each one is to blame. During operation, this neural network learns the XOR logic function, which is something I encountered already during my studies learning about logic gates.

2) Now that we have familiarized ourselves with the sigmoid function, we can use it to operate logic gates. Here is how it works: 1) Randomly initialize weights and bias. 2) For a number of epochs (passes of the dataset), compute predictions, errors and update weights and bias accordingly. The program will predict AND gate outputs. 

IMPORTANT: Install numpy on PyCharm if you haven't already. For that, you go to terminal and type in 'pip install numpy'
