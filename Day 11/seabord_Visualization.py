import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("../Day 10/avgIQpercountry.csv")

plt.figure(figsize=(10, 6))
sns.histplot(df["Average IQ"])
plt.title("Average IQ")
plt.xlabel("Average IQ")
plt.ylabel("Count")
plt.tight_layout()

plt.show()
