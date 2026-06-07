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

    # print("Index | Predicted | Actual | Error   | sqrt")
    # for i in range(len(ypred)):

        # print(f"{i}     | {y_pred[i]}           | {y_actual[i]}     | {rslt[i]}     |   {sqrt[i]}")
    # print(f"total_error :  {sum(sqrt)}")
loss(y_pred, y_actual)
###################*Cost Function#########3 J=1/n*​∑(error2)
x = [1, 2, 3] #featur
y = [2, 6, 8] #actual y

x = [1, 2, 3] 

# def Cost(x,y):
#     m = 2
#     b = 1
#     err = []
#     pre= []
#     sqr = []
#     for i in (x):
#         pre.append(i*m + b)
#     for i,j in zip(pre,y):
#         err.append(i-j)
#     for i in err:
#         sqr.append(pow(i,2))
#     summ  =  sum(sqr)
#     cost =  summ / len(y)

#     print(pre)
#     print(err) ##* takes the 
#     print(sqr)
#     print(summ)
#     print(cost) ##*Mean Squared Error (MSE).
# Cost(x,y)
x = [0, 50000, 100000] # mileage
y = [20000, 18000, 15000] # price
def cost(x,y):
    m = -0.05
    b = 20000
    pred = []
    sqrderror =[]
     
    for i  in x:
        pred.append(i*m+b)
    for i,j in zip(pred,y):
        error = i -j  #*actual price -  predicted 
        sqrderror.append(error**2) #* squared error
    sumofsqrterror = sum(sqrderror)
    mse =  sumofsqrterror/len(y)
    print(pred) ##*[20000.0, 17500.0, 15000.0] 
    print(error) ##*[0.0, -500.0, 0.0]
    print(f" suum of sqrd error = {sumofsqrterror}")
    print(f"cost MSE {mse}")
# cost(x,y)
####* estimatePrice(mileage)=θ0​+(θ1​×mileage) we dont have intercep price at 0km
##* extract Theta0 =   intercept
import numpy as np
mil = [1,2,3]
price = [3,5,7]
#*theta0 is the price when mil =0
##* price =  t0 + t1*mileage
#*price = t0
##* find the slop manualy 
mill_m =  np.array(mil)
price_m =  np.array(price)
mill_m = mill_m.mean()
price_m =  price_m.mean()
print(mill_m, price_m)
##* compute x- xmean how far is each X from the average of x ?
meanx= []
meany = []
for i, j in zip (mil ,price):
    meanx.append(i-mill_m)
    meany.append(j-price_m)
# print(meanx)
# print(meany)
up = 0
down = 0
for i,j in zip(mil, price):
    up += ((i-int(mill_m))*(j-int(price_m)))
    down  +=  pow((i - mill_m),2)
print(up) 
print(down)
print(f"slop =  {up/down}")
    # down =  
# (xi-xm)(yi-ym)
# x = [1,2,3]
# y = [3,5,7]
# xm = 2
# ym = 5

# xmnea  = [-1,0,1]
# ymean  = [-2,0,2]
