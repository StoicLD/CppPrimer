import os

path = os.getcwd() + '\\'
for i in range(8,19):
    createPath = path + 'Ch'
    if(i <= 10):
        createPath += '0'
    createPath += str(i)
    print(createPath)
    os.mkdir(createPath)