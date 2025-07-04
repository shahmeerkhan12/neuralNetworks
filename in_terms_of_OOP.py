import numpy as np

np.random.seed(0)

X = [[1,2,3,2.5],
     [2.0,5.0,-1.0,2.0],
     [-1.5,2.7,3.3,-0.8]]

class Layer_dense:
   def __init__(self,n_inputs,n_neurons):
      self.weights = 0.1*np.random.randn(n_inputs,n_neurons)
      self.bias = np.zeros((1,n_neurons))
   def forward(self,inputs):
      #accepts only true inputs or output of another layer
      self.output = np.dot(inputs, self.weights) + self.bias


# for formating purpose only   
np.set_printoptions(precision=3)

# layer 1 with 5 neurons
layer_1 = Layer_dense(4,5)
layer_1.forward(X)
# print(layer_1.output)

# layer 2
layer_2 = Layer_dense(5,1)
layer_2.forward(layer_1.output)
print(layer_2.output)
