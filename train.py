import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os , sys
from pathlib import Path
#* 1. predict.py runs → theta.json doesn't exist → θ0=0, θ1=0 → price = 0
#* 2. train.py runs → gradient descent → saves theta.json with real values
#* 3. predict.py runs again → reads theta.json → gives real price

class params:
    def __init__(self, path):
        self.df =  pd.read_csv(path)
        self.slop =None
        self.theta0 = 0 #*intercept
        self.theta1 = 0 #*slop 


##* estimatedprice(mileage) =  theta0 + (theta1*mileage)
    def estimate_price(self):

        Lr  = 0.1
        estimated = self.theta0 + (self.theta1*self.df["km"]) #*
        price = (estimated -self.df["price"]).sum()   #*(theta0+theta1*mileage[i])
        averageErr = (1/self.df.shape[0])*(price)
        self.theta0 = Lr*averageErr
        #* tmpθ1 = learningRate ∗ 1 m m−1∑ i=0 (estimatePrice(mileage[i]) − price[i]) ∗ mileage[i]
        estimated1 =  self.theta1 + (self.theta1*self.df["km"])
        price1 =  ((estimated1 - self.df["price"]).sum())
        averageErr1 = (1/self.df.shape[0])*(price1) 
        self.theta1 = (Lr * averageErr1 )*estimated1
        print(self.theta0 , self.theta1)

#* tmpθ0 = learningRate ∗ 1 m m−1∑ i=0 (estimatePrice(mileage[i]) − price[i])

    
         
         
def execute(algo):
    algo.estimate_price()

def main():
    try:
        assert len(sys.argv) == 2 , "argument are bad"
    except AssertionError as e :
        print(f"AssertionError: {e}")
        sys.exit(1)
    path  = Path(str(sys.argv[1]))
    print(path)
    tools =  params(path)
    execute(tools)
if __name__ == "__main__":
    main()




