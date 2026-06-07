import sys , os
import numpy as np 

def execute(km):

    theta0 = 0
    theta1 = 0
    price  = theta0 + km*theta1
    print(f"price for car of {km} km : {price}")


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