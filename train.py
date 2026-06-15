import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys
from pathlib import Path
import json


class params:
    def __init__(self, path):
        self.df = pd.read_csv(path)
        self.slop = None
        self.theta0 = 0
        self.theta1 = 0
        self.cost = 0
        self.costarray = []
        self.cost_diff = []
        self.mse = 0

    def gredient_descent(self):
        Lr = 0.01
        self.theta0 = float(self.theta0)
        self.theta1 = float(self.theta1)
        km_min = self.df["km"].min()
        km_max = self.df["km"].max()
        km_min = float(km_min)
        km_max = float(km_max)
        self.df["km_scaled"] = (self.df["km"] - km_min) / (km_max - km_min)
        m = self.df.shape[0]
        for i in range(10000):
            estimatePrice0 = self.theta0 + (self.theta1*self.df["km_scaled"])
            sum_error = (estimatePrice0 - self.df["price"])
            gradient_theta0 = (1/m)*(sum_error).sum()
            gradient_theta1 = (1/m)*(sum_error * self.df["km_scaled"]).sum()
            temptheta0 = self.theta0 - (Lr * gradient_theta0)
            temptheta1 = self.theta1 - (Lr * gradient_theta1)
            self.theta0 = temptheta0
            self.theta1 = temptheta1
            self.cost = (sum_error**2).sum() / (2 * m)
            self.costarray.append(self.cost)
            self.cost_diff.append(-self.costarray[i] + self.costarray[i-1])
            print("iteration", i)
        # print("cost diff", self.cost_diff, "\n")
        self.mse = ((sum_error)**2).mean()
        with open("weights.json", "w") as json_file:
            json.dump({
                "theta0": self.theta0,
                "theta1": self.theta1,
                "km_min": km_min,
                "km_max": km_max
            }, json_file, indent=4)

    def plotregree(self):
        newprice = self.theta0 + self.theta1 * self.df["km_scaled"]

        fig, ax = plt.subplots(1, 4, figsize=(15, 5))

        ax[0].scatter(self.df["km"], self.df["price"], color="blue")
        ax[0].set_title("Original Data")
        ax[0].set_xlabel("km")
        ax[0].set_ylabel("price")

        ax[1].scatter(
            self.df["km"], self.df["price"],
            color="blue", label="Actual")
        ax[1].plot(
            self.df["km"], newprice, color="red",
            label="Prediction")
        ax[1].set_title("Linear Regression")
        ax[1].legend()

        ax[2].plot(range(len(self.costarray)), self.costarray)
        ax[2].set_xlabel("Iterations")
        ax[2].set_ylabel("Cost")
        ax[2].set_title("Cost vs Iterations")

        ax[3].axis('off')

        rmse = np.sqrt(self.mse)
        ss_res = ((self.df["price"] - newprice) ** 2).sum()
        ss_tot = ((self.df["price"] - self.df["price"].mean()) ** 2).sum()

        r2 = 1 - (ss_res / ss_tot)
        if r2 > 0.6:
            txt = "Model Passed"
        else:
            txt = "Model failed"
        ax[3].text(
            0.5, 0.5,
            f" Accuracy \n RMSE:{rmse:.2f}\nR²: {r2:.4f}\n\n\n {txt}",
            fontsize=12,
            fontweight='bold',
            ha='center',
            va='center'
        )

        plt.tight_layout()
        plt.show()


def execute(algo):
    algo.gredient_descent()
    algo.plotregree()


def main():
    try:
        assert len(sys.argv) == 2, "argument are bad"
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)
    path = Path(str(sys.argv[1]))
    print(path)
    tools = params(path)
    with open("weights.json", "w") as json_file:
        json.dump({
                "theta0": 0,
                "theta1": 0,
                "km_min": 0,
                "km_max": 0
            }, json_file, indent=4)

    execute(tools)


if __name__ == "__main__":
    main()
