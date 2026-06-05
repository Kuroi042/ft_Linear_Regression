# def price_for_mileage(milles):
#     price  = 240000 - 0.05*milles
#     return int(price)

# print(price_for_mileage(0))
# print(price_for_mileage(100000))
# print(price_for_mileage(200000))


# m =-0.05 ##* every extra kilo reducdes the price by 0.05
# b = 20000
# for x in [0,50000,10000, 150000]:
#         y = m*x+b
#         print(f"x={x}->y={y}")

#* x=0->y=20000.0
#* x=50000->y=17500.0
#* x=10000->y=19500.0
#* x=150000->y=12500.0


##* compute the slope manually
# these two points
# x1 = 100000
# y1=15000
# x2 = 200000 
# y2=10000

# slope =  (y2-y1)/(x2-x1)
# print (slope)

# import matplotlib.pyplot as plt
#* import seaborn as sns
#* prices = [10,20,30,40]
#* total= 0
# for p in prices:
    # total+=p
# print(total)
#*for p in prices:
#*   mean  =  total/len(prices)
#*print(mean)

# mileage =  [0, 50000, 100000, 150000]
# price = [20000, 18000, 15000, 12000]

# plt.scatter(mileage, price)
# sns.regplot(x=mileage, y=price)
# plt.ylabel("prices")
# plt.xlabel("mileage")
# plt.show()
###################################day 02@@@@@@@@@@@@@@@
###* build estimationPrice
teta0 = 20000 ## 
teta1 = -0.05 ##*slop
def estimatedprice(mileage):
    return (teta0 + teta1*mileage)

print(estimatedprice(500000))
