import sys
import json
from pathlib import Path


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


def main():
    km = float(input("Enter mileage: "))
    weight = Path("weights.json")
    if not weight.is_file():
        print("File does not exist!")
        sys.exit(1)
    execute(km, weight)


if __name__ == "__main__":
    main()
