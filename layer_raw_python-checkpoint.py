inputs = [1.3,2.2,1.1,2.9]
# weights for single neuron (unique weight for each input)
weights = [[-0.3,-1,2,3.1],
           [1,2.2,-1.1,-1.9]]
# two neuron so take will two bias values
bias = [2,3]
# layer1-> 1st neuron in its simplest raw python (calulates a weihted sum of the inputs)
output_1 = inputs[0]*weights[0][0] + inputs[1]*weights[0][1] + inputs[2]*weights[0][2] + inputs[3]*weights[0][3] 
output_1 += bias[0]
print("neuron 1 output: " , output_1)

# second neuron:
output_2 = inputs[0]*weights[1][0] + inputs[1]*weights[1][1] + inputs[2]*weights[1][2] + inputs[3]*weights[1][3] 
output_2 += bias[1]

# lets print our output
print("neuron 1 output: ", round(output_2))
