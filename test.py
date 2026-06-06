def cost(qt):
    price = 4
    return qt*price


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
def find_intercept():
    y = []
    x =[1,2,3,4,]
    for var in x:
        y.append( (3*var)+2)
    plt.plot(x,y)
    plt.show()
# find_intercept()
arr = [1,2,3,4,5,6,7,8,9]
def summation(arr):
    total  = 0
    for i in arr:
        total +=i
    mean = total/len(arr)
    print(total , mean)
arr1 =  np.array(arr.copy())
# print(summation(arr))
# print(arr1.mean())
        
mileages = [0,50000,100000,150000,200000]
prices   = [20000,18000,15000,12000,10000]
milcp =  np.array(mileages.copy())
pricecp =  np.array(prices.copy())
# print(f"average mileage : {int(milcp.mean())}, average price :{ int(pricecp.mean()) }")
# print(f"max price {pricecp.max()}")
# # print(f"min price {pricecp.min()}")
# plt.plot(pricecp,milcp)
# plt.ylabel("mileage")
# plt.xlabel("prices")
# slop = -0.05
# baseprice = 20000   #*slop * #*mileage + #*baseprice
# estimateprice =     -0.05  *  50000  +   20000
# print(f"estimated price  for 50000 mille is {estimateprice}")

# plt.show()
###*COST FUNCTION############### HOW wring we are 
##* find the best slop and intercept automatically
x = [1,2,3] #mileage
m =2 #slop
b = 1  # intercept
def predict(x,m,b):
    y = []
    for i in x:
        y.append((m*i)+1)
    return y
# print(predict(x,m,b))
####*COMPUTE THE ERROR = ypred - yactual
y_pred = [3, 5, 7]
y_actual = [2, 6, 8]
def loss(ypred , y_actual):
    rslt = []
    sqrt = []
    for i , j in zip(ypred, y_actual):
        # print(f"{i} - {j}")
        rslt.append(i-j)
    for i in rslt:
        sqrt.append(pow(rslt[i],2))

    print("Index | Predicted | Actual | Error   | sqrt")
    for i in range(len(ypred)):

        print(f"{i}     | {y_pred[i]}           | {y_actual[i]}     | {rslt[i]}     |   {sqrt[i]}")
loss(y_pred, y_actual)
