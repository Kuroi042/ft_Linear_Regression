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
        self.costarray= []

#* tmpθ0 = learningRate ∗ 1/m  (estimatePrice(mileage[i]) − price[i])
#* tmpθ1 = learningRate ∗ 1/m (estimatePrice(mileage[i]) − price[i]) ∗ mileage[i]
    def gredient_descent(self):
        Lr  =  0.01
        costarray = []
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
            self.costarray.append(self.cost)
            
            print("iteration" , i)
        print("0",self.costarray[0])
        print("1",self.costarray[0])
        print("9999",self.costarray[9999])

        with open("weights.json", "w") as json_file:
            json.dump({
                "theta0": self.theta0,
                "theta1": self.theta1,
                "km_min": km_min,
                "km_max": km_max
            }, json_file, indent=4)

    

    def plotregree(self):
        newprice = self.theta0 + self.theta1 * self.df["km_scaled"]

        fig, ax = plt.subplots(1, 3, figsize=(12, 5))

        # Plot 1: Original data
        ax[0].scatter(self.df["km"], self.df["price"], color="blue")
        ax[0].set_title("Original Data")
        ax[0].set_xlabel("km")
        ax[0].set_ylabel("price")

        # Plot 2: Data + regression line
        ax[1].scatter(
            self.df["km"],
            self.df["price"],
            color="blue",
            label="Actual data"
        )

        ax[1].plot(
            self.df["km"],
            newprice,
            color="red",
            linewidth=2,
            label="Regression line"
        )



        ax[1].set_title("Linear Regression")
        ax[1].set_xlabel("km")
        ax[1].set_ylabel("price")
        ax[1].legend()
        
        ax[2].plot(range(len(self.costarray)), self.costarray)     
        ax[2].set_xlabel("Iterations")
        ax[2].set_ylabel("Cost")
        ax[2].set_title("Cost vs Iterations")  
        ax[2].yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:,.0f}'))

        plt.tight_layout()
        plt.show()


def execute(algo):
    algo.gredient_descent()
# bonus
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




