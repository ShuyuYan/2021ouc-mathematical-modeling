import numpy as np
import random

def sigmoid(inX):
    return 1.0 / (1 + np.exp(-inX))

#梯度上升训练
def gradAscent(dataMatIn, classLabels):
    dataMatrix = np.mat(dataMatIn)
    labelMat = np.mat(classLabels).transpose()
    m, n = np.shape(dataMatrix)
    alpha = 0.01
    maxCycles = 500
    weights = np.ones((n,1))
    for k in range(maxCycles):
        h = sigmoid(dataMatrix * weights)
        error = labelMat - h
        weights = weights + alpha * dataMatrix.transpose() * error
    return weights.getA()

#运行模型
def colicTest():
    frTrain = open('训练.txt')
    frTest = open('测试.txt')
    trainingSet = []; trainingLabels = []
    for line in frTrain.readlines():
        currLine = line.strip().split('\t')
        lineArr = []
        
        for i in range(len(currLine)-1):
            lineArr.append(float(currLine[i]))
        trainingSet.append(lineArr)
        trainingLabels.append(float(currLine[-1]))
    trainWeights = gradAscent(np.array(trainingSet), trainingLabels)
    #print(trainWeights)
    
    errorCount = 0; numTestVec = 0.0
    data = open('ans.txt','w+')
    t, f = 0, 0
    for line in frTest.readlines():
        numTestVec += 1.0
        currLine = line.strip().split('\t')

        lineArr =[]
        for i in range(len(currLine)-1):
            lineArr.append(float(currLine[i]))
        #print(int(classifyVector(np.array(lineArr), trainWeights[:,0])),file = data)
        if int(classifyVector(np.array(lineArr), trainWeights[:,0]))!= int(currLine[-1]):
            errorCount += 1
        elif int(classifyVector(np.array(lineArr), trainWeights[:,0]))== 1:
            t += 1
        else:
            f += 1
    tpr = float(t)/50.0*100
    fpr = float(f)/450*100
    errorRate = (1.00-float(errorCount)/numTestVec) * 100
    print("测试集总体准确率为: %.2f%%" % errorRate)
    print('测试集TPR为: %.2f%%'% tpr)
    print('测试集FPR为: %.2f%%'% fpr)

#结果预测
def classifyVector(inX, weights):
    prob = sigmoid(sum(inX*weights))
    if prob >= 0.5: return 1.0
    else: return 0.0

if __name__ == '__main__':
    colicTest()
