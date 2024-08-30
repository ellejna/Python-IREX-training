import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("../Day 10/avgIQpercountry.csv")

df["Population - 2023"] = df["Population - 2023"].str.replace(",", "").astype(float)

numerical_iq_data = df.select_dtypes(include="number")

sns.heatmap(numerical_iq_data.corr(), annot=True, cmap="coolwarm", fmt=".2f")

plt.show()
