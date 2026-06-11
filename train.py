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

#*cost function to cehck the error value between the predicted 
#* output and actual output of estimated function
##* estimatedprice(mileage) =  theta0 + (theta1*mileage)
    def gredient_descent(self):
#* tmpθ0 = learningRate ∗ 1/m  (estimatePrice(mileage[i]) − price[i])
#* tmpθ1 = learningRate ∗ 1/m (estimatePrice(mileage[i]) − price[i]) ∗ mileage[i]
        Lr  =  0.01
        self.theta0 = float(self.theta0)
        self.theta1 = float(self.theta1)
        km_min = self.df["km"].min()
        km_max = self.df["km"].max()
        km_min = float(km_min)
        km_max = float(km_max)
        self.df["km_scaled"] = (self.df["km"] - km_min) / (km_max - km_min)        
        m =  self.df.shape[0]
        gt1 = []
        gt0 = [] 
        for i in range(10000):
            #*y^​=θ0​+θ1​x
            estimatePrice0 = self.theta0 + (self.theta1*self.df["km_scaled"]) #*estimated_price
            #*y^​ −y estimated -  actual  
            #*As the loop keeps running, the estimatedPrice gets closer to price
            sum_error = (estimatePrice0 -self.df["price"])
            #* 1/m * ​∑(y^i-yi)
            gradient_theta0 = (1/m)*(sum_error).sum()
            gt0.append(gradient_theta0)
            #* 1/m * ​∑(y^i-yi)*xi 
            gradient_theta1 = (1/m)*(sum_error *self.df["km_scaled"]).sum()
            gt1.append(gradient_theta1)                
            temptheta0 = self.theta0 - (Lr * gradient_theta0)
            temptheta1 = self.theta1 - (Lr * gradient_theta1)
            self.theta0 =  temptheta0
            self.theta1 = temptheta1
        self.df["newprice"] = self.theta0 + (self.theta1*self.df["km_scaled"])
        print(self.theta0, self.theta1, km_min, km_max)

        # data_dict = dict(zip(keys, values))
        with open("model_weights.json", "w") as json_file:
            json.dump({
                "theta0": self.theta0,
                "theta1": self.theta1,
                "km_min": km_min,
                "km_max": km_max
            }, json_file, indent=4)


    import matplotlib.pyplot as plt


    def plot(self):
        # 1. Plot the real dataset as individual points (Scatter plot)
        print(self.df["newprice"])
        plt.scatter(

            self.df["km"], self.df["newprice"], 
        )
        # 4. Display the window
        plt.show()


def execute(algo):
    algo.gredient_descent()
    algo.plot()

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




