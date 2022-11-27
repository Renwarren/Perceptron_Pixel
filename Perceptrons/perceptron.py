from constants import THRESHOLD, LEARNING_RATE

def predict(weighted_sum,threshold):
    if weighted_sum>threshold:
        return 1
    return 0

def weighted_sum(weights,input):
    s = 0
    for i in range(len(input)):
        s += weights[i] * input[i]
    return s

def rectify_weights(weights,predicted,output,example):
    change = (output - predicted)
    delta = []
    for i in range(len(example)):
        delta_i = LEARNING_RATE * change * example[i]
        delta.append(delta_i)
    for i in range(len(weights)):
        weights[i] = round(weights[i] + delta[i],2)
    return weights