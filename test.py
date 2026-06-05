def cost(qt):
    price = 4
    return qt*price


import matplotlib.pyplot as plt
def find_intercept():
    y = []
    x =[1,2,3,4,]
    for var in x:
        y.append( (3*var)+2)
    plt.plot(x,y)
    plt.show()
find_intercept()


