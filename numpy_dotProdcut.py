import numpy as np
inputs = [[1.3,2.2,1.1,2.9],
          [0.3,1.2,2.1,0.9],
          [2.3,0.2,0.1,1.9],
          [-1.3,2.2,2.1,3.9]]
# let's say 3 neurons process the inputs, each having seperate weight elements for each input element
weights = [[1.3,0.5,-0.2,2.2],
           [-1,-1.5,-1.2,2],
           [-1.2,-2.5,-2.2,1.2]]
# each of these neurons have a single bias value 
biases = [2,3,1]

# neurons performs the operations by the dot product(numpy)

# neuron-1
output1 = np.dot(inputs,np.array(weights).T)+biases[0]
print(output1)
