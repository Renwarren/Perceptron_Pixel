from constants import *
from perceptron import *


print('The initial weights are:')
print(WEIGHTS)
weights = WEIGHTS[:]
flag = True
iteration = 1
while flag:
    error = 0
    flag = False
    print('------------------Epoch',iteration,'-----------------------')
    for i in range(len(EXAMPLES)) :
        print('Example',i+1,':',EXAMPLES[i][1:])
        s = weighted_sum(weights,EXAMPLES[i])
        predicted = predict(s,THRESHOLD)

        if predicted != OUTPUT[i]:
            flag = True
            error+=1
            print('*************ERROR************')
            print('Predicted:',predicted)
            print('Expected:',OUTPUT[i])
            weights = rectify_weights(weights,predicted,OUTPUT[i],EXAMPLES[i])
            print('UPDATED WEIGHTS:',weights)
            print('*******************************')
    print('NUMBER OF ERRORS:',error)
    iteration+=1

print('FINAL WEIGHTS:',weights)

