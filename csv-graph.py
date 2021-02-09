#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt

lines=0
with open("sample.csv","r") as f:
    for x in f:
        lines+=1
        print(x)
print("lines: {}".format(lines))
csv=pd.read_csv("sample.csv", header=0, names=["num1","num2"])
print(csv)
#print(csv["num1"]+" "+csv["num2"])
plt.plot(csv["num1"],csv["num2"],marker="o")
plt.show()
