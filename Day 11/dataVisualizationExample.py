import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("../Day 10/avgIQpercountry.csv")

avg_iq_per_country = df.groupby('Continent')['Average IQ'].mean()

plt.figure(figsize=(12, 6))

avg_iq_per_country.plot(kind='line')

plt.title('Average IQ per country')
plt.xlabel('Country')
plt.ylabel('Average IQ')

plt.grid(axis="both", linestyle="--", alpha=0.5)

plt.show()