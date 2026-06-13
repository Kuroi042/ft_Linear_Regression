import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os , sys
from pathlib import Path
import seaborn as sns
import json
#* 1. predict.py runs → theta.json doesn't exist → θ0=0, θ1=0 → price = 0
#* 2. train.py runs → gradient descent → saves theta.json with real values
#* 3. predict.py runs again → reads theta.json → gives real price

class params:
    def __init__(self, path):
        self.df =  pd.read_csv(path)
        self.slop =None
        self.theta0 = 0 #*intercept
        self.theta1 = 0 #*slop 
        self.cost = 0

#* tmpθ0 = learningRate ∗ 1/m  (estimatePrice(mileage[i]) − price[i])
#* tmpθ1 = learningRate ∗ 1/m (estimatePrice(mileage[i]) − price[i]) ∗ mileage[i]
    def gredient_descent(self):
        Lr  =  0.01
        self.theta0 = float(self.theta0)
        self.theta1 = float(self.theta1)
        km_min = self.df["km"].min()
        km_max = self.df["km"].max()
        km_min = float(km_min)
        km_max = float(km_max)
        self.df["km_scaled"] = (self.df["km"] - km_min) / (km_max - km_min)        
        m =  self.df.shape[0]
        for i in range(10000):
            #*y^​=θ0​+θ1​x
            estimatePrice0 = self.theta0 + (self.theta1*self.df["km_scaled"])
            sum_error = (estimatePrice0 -self.df["price"])
            gradient_theta0 = (1/m)*(sum_error).sum()
            gradient_theta1 = (1/m)*(sum_error *self.df["km_scaled"]).sum()
            temptheta0 = self.theta0 - (Lr * gradient_theta0)
            temptheta1 = self.theta1 - (Lr * gradient_theta1)
            self.theta0 =  temptheta0
            self.theta1 = temptheta1
            self.cost = (sum_error**2).sum() / (2 * m)
        with open("weights.json", "w") as json_file:
            json.dump({
                "theta0": self.theta0,
                "theta1": self.theta1,
                "km_min": km_min,
                "km_max": km_max
            }, json_file, indent=4)

    
    
    def plotregree(self):
        newprice = []
        newprice =  self.theta0 +  self.theta1*self.df["km_scaled"]
        plt.plot(self.df["km_scaled"],newprice, linestyle='--')
        plt.ylabel("predicted price")
        plt.xlabel("km")
        plt.legend("")

        plt.show()


    def plotscatter(self):
        plt.scatter(

            self.df["km"], self.df["newprice"], 
        )
        # 4. Display the window
        plt.ylabel("price")
        plt.xlabel("km")
        plt.show()


def execute(algo):
    algo.gredient_descent()
    # algo.plotscatter()
    algo.plotregree()
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




