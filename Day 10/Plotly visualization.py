import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px

df = pd.read_csv("../Day 10/avgIQpercountry.csv")

df["Population - 2023"] = df["Population - 2023"].str.replace(",", "").astype(float)

figure = px.scatter_geo(df, locations="Country", locationmode="country names",
                        hover_name="Country", size="Average IQ", color="Continent",
                        projection="natural earth", title="Average IQ per country",
                        size_max=20, template="plotly_dark")

figure.show()
