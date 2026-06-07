import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os , sys
from pathlib import Path

#head(01)
class params:
    def __init__(self, path):
        self.df =  pd.read_csv(path)
        self.slop =None
        self.theta0 = None #*intercept
        self.theta1 = None #*slop 


##* estimatedprice(mileage) =  theta0 + (theta1*mileage)
    def find_slope(self):
            price =  self.df["price"]
            km =  self.df["km"]
            y_mean = price.mean() #*price
            x_mean =  km.mean()   #*km
            up , down =0 ,0
            up =  ((self.df["km"]-(x_mean))*(self.df["price"]-(y_mean))).sum()
            down = ((self.df["km"]-x_mean)**2).sum()
            self.theta1 =  up/down
            self.theta0 = y_mean - self.theta1*x_mean
            print(f"slop ={self.theta1} , intercept = {self.theta0}")
            
    # def find_intercept(self):
         
         
def execute(algo):
    algo.find_slope()

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



