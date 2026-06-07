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
        self.intecep = None
    def find_slope(self):
        print(self.df)

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



