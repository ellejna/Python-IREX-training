import pandas as pd
import matplotlib.pyplot as plt

# remember to write the dots, so then it goes a folder above
df = pd.read_csv("../Day 10/avgIQpercountry.csv")
print(df.head())
print(df.info())

# get IQ of the countries where the average IQ is >=100
IQwith100 = df[df["Average IQ"]>=100].sort_values(by="Average IQ", ascending=False)
print(IQwith100)

plt.figure(figsize=(14, 8))
bars = plt.bar(df["Continent"], df["Average IQ"], color="skyblue")

plt.xlabel("Continent")
plt.xticks(rotation=90, fontsize=14)

plt.ylabel("Average IQ")
plt.yticks(fontsize=14)

plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.bar_label(bars, color="black")

plt.tight_layout()

plt.show()
