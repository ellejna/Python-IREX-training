import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../Day 10/avgIQpercountry.csv")

nobel_prizes_by_continent = df.groupby("Continent")["Nobel Prices"].sum()

number_of_continents = nobel_prizes_by_continent.count()

print(number_of_continents)

colors = ["gold", "lightcoral", "yellow", "green", "orange"]

plt.figure(figsize=(10, 10))

nobel_prizes_by_continent.plot(kind="pie", autopct="%1.1f%%", color=colors)

plt.show()