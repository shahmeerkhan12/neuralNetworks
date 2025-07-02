inputs = [1,2.2,4.1,5.9]
# weights for single neuron (unique weight for each input)
weights = [2.3,1,2,3.9]
# bias (single neuron has single bias value)
bias = 2
# now neuron does the following
output = inputs[0]*weights[0] + inputs[1]*weights[1] + inputs[2]*weights[2] + inputs[3]*weights[3] 
output += bias
# lets print our output
print(output)
