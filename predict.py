import sys
import os
import matplotlib.pyplot as plt
import json
from pathlib import Path
file_path = os.path.join('Weights.json')


def execute(km, path):

    with open('weights.json', 'r') as file:
        data = json.load(file)
    theta0 = data['theta0']
    theta1 = data['theta1']
    km_min = data['km_min']
    km_max = data['km_max']

    km_scaled = (km - km_min) / (km_max - km_min)

    price = theta0 + km_scaled*theta1
    print(f"price for car of {km} km : {price}")
    plt.plot(price)


def main():
    try:
        assert len(sys.argv) == 2, "argument are bad"
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)
    mileage = int(sys.argv[1])
    weight = Path("weights.json")
    if not weight.is_file():
        print("File does not exist!")
        sys.exit(1)
    execute(mileage, weight)


if __name__ == "__main__":
    main()
