#This is a very simple neural network, a 2-layer freeforward one
#It features an input layer, a hidden layer and an output layer
#This is often referred to as 2-2-1 Neural Network (2 inputs, 2 hidden neurons, 1 output)
#The neural network also shows why Linear Algebra is so crucial in computer science and artificial intelligence

import numpy as np

#Activation function for non-linearity in the function
def sigmoid_funct(x):
    return 1 / (1 + np.exp(-x))

#Derivative of the sigmoiod function assuming input x is sigmoid output already
def sigmoid_derivative(x):
    return x * (1 -x)

#Define 2 matrices that holds the input data (features) and expected outputs (labels)
X = np.array([[0,0],[0,1],[1,0],[1,1]]) #Inputdataset: All possible pairs of 0 and 1
Y = np.array([[0],[1],[1],[0]]) #Output dataset: XOR truth table outputs (Knowledge from logic gates)

np.random.seed(1) # Set random seed for reproductibility of initial weights

#'syn0' is the matrix connecting the input layer to the hidden layer
#Input layer has 2 neurons and the hidden layer has 2 neurons, thus [2,2]
syn0 = 2 * np.random.random((2,2)) - 1 #'np.random.random' is the numpy that generates random numbers between 0 and 1

#'syn1' is the matrix connecting hidden layer to output layer
#Hidden layer has 2 neurons and output layer has 1 neuron, thus [2,1]
syn1 = 2 * np.random.random((2,1)) - 1


for iter in range(10000):

    l0 = X
    l1 = sigmoid_funct(np.dot(l0, syn0)) #Compute the output of the hidden layer neurons
    #'np.dot(l0,syn0)' is a linear transformation that computes the weighted sum of inputs for each hidden layer neuron
    #l0 is the unput data (given above as [0,0] or [0,1]
    l2 = sigmoid_funct(np.dot(l1, syn1)) #Compute the output of the final prediction for each input
    #Linear transformation that performs matrix multiplication between l1 and syn1
    #Take the outputs from the hidden layer l1 and compute a weighted sum using syn1


    l2_error = Y - l2 #This is the error signal between true output Y and the predicted output l2 for updating weight
    #It is a simple way to represent the gradient of the loss (mean squared error) with respect to the output layer

    if (iter % 1000) == 0:
        print(f"Error: {np.mean(np.abs(l2_error))}")


    #Important to know: 'delta' represents the error gradiant in neural networks
    #They are partial derivatvies of the loss with respect to neuron outputs
    l2_delta = l2_error * sigmoid_derivative(l2)
    l1_error = l2_delta.dot(syn1.T)
    l1_delta = l1_error * sigmoid_derivative(l1)


    syn1 += l1.T.dot(l2_delta) #Update weights between hidden layer and output layer
    syn0 += l0.T.dot(l1_delta) #Update weights between hidden layer and input layer

print("\nFinal prediction results: ") #A sigmoid function outputs a value between 0 and 1
#It predicts the probability that a given input belongs to a particular class (such as a "positive" class)
print(l2) #'l2' holds the final output prediction of the neural network after training
#Print 'l2' in order to see what the network has learned