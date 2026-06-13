import sys , os
import numpy as np 
import matplotlib.pyplot as plt
import json
file_path = os.path.join('Weights.json')

def execute(km):
    try:
        with open('weights.json' ,'r') as file:
            data =  json.load(file)
    except:
        print(f"error '{file_path}' not found ")
        sys.exit(1)
    theta0 =  data['theta0']
    theta1 =  data['theta1']
    km_min  = data['km_min']
    km_max  = data['km_max']

    km_scaled = (km - km_min) / (km_max - km_min)

    price  = theta0 + km_scaled*theta1
    print(f"price for car of {km} km : {price}")
    plt.plot(price)


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