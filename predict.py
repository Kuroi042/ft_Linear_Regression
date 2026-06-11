import sys , os
import numpy as np 
import matplotlib.pyplot as plt
def execute(km):

    theta0 = 100000
    theta1 = -0.5
    price  = theta0 + km*theta1
    # print(f"price for car of {km} km : {price}")
    # plt.plot()

def main():
    try:
        assert len(sys.argv) == 2 , "argument are bad"
    except AssertionError as e :
        print(f"AssertionError: {e}")
        sys.exit(1)
    mileage =  int(sys.argv[1])
    execute(mileage)
if __name__ == "__main__":
    main()