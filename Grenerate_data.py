import pandas as pd

row = ['2', ' Marie', ' California']

with open('emp2.csv','w') as fp2:
    fp2.write("Hello, java, python,no.\n")
    fp2.write("Hello1, java1, python1,1\n")
    fp2.write("Hello2, java2, python2,2\n")
    fp2.write("Hello3, java3, python3,3\n")
    fp2.write("Hello4, java4, python4,4\n")


dataFrame = pd.read_csv('emp2.csv', delimiter=',')
print(type(dataFrame.values[0][3]))
