import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

wd = pd.read_csv("weatherdata.csv")

average_temp = wd.groupby("")["temperature"].mean()
