import numpy as np

# Define a sigmoid function and its first derivative

def s(x):
    return 1/(1 + np.exp(-x))
def s_derivative(x):
    return x * (1 - x)

# Define the training data for the AND gate: All combinations for binary inputs

inputs = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

# Expected output for AND gate:

E_output = np.array([[0], [0], [0], [1]])

# Initialize weights and bias randomly
np.random.seed(123)
weights = np.random.uniform(size=(2,1)) # Create a 2x1 matrix with random numbers between 0 and 1
bias = np.random.uniform(size=(1,)) # Constant added to the neuron's weighted sum

# Create a training loop

learning_rate = 0.1 # Keep updating the value of the weights and bias. Keep the value somewhat low to avoid overshoot.
epochs = 10000 # Going through the bias 10000 times will adjust the bias and weight each time for more accuracy

for _ in range(epochs):

    # Forward pass
    weighted_sum = np.dot(inputs, weights) + bias
    P_output = s(weighted_sum)

    # Calculate error
    error = E_output - P_output # Expected output minus predicted output

    # Backpropagation
    adjustments = error*s_derivative(P_output)

    # Update weights and bias
    weights += np.dot(inputs.T, adjustments)
    bias += np.sum(adjustments) * learning_rate

# Display final weight and prediction

print("Final weights", weights)
print("Final bias", bias)
print("\nPrediction after training: ")
print(P_output.round(3)) # Round the value up to 3 decimal portions  