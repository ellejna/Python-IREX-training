import pandas as pd
# kaggle average global iq per country with other states, search this on yt and convert the zip file
df = pd.read_csv("avgIQpercountry.csv")
print(df.head())
print(df.info())

# select only the tro columns that are needed
subset = df[["Country", "Average IQ"]]
print(subset)

# see countries and info for those whos IQ is above 100

filtered_df = subset[subset["Average IQ"] > 100]
print(filtered_df)

# handle an example where the data is missing or has duplicates
null_mask = df.isnull()
null_count = null_mask.sum()
print(null_count)

# remove the unwanted data
df.dropna(inplace=True)
print(df.info())

# find the duplicates
duplicate_count = df.duplicated().sum()
print("Duplicate count is: ", duplicate_count)

df.drop_duplicates(keep="first", inplace=True)

# find average IQ for each continent
average_iq_per_continent = df.groupby("Continent")["Average IQ"].mean()

# "df.groupby" allows you to pick a specific category/column and then the "Average IQ"
# is the name that it is classified as
print(average_iq_per_continent)

# create a filter which organizes it by highest to lowest
average_iq_per_continent_sorted = average_iq_per_continent.sort_values(ascending=True)
print(average_iq_per_continent_sorted)
# This is from lowest to highest, and if we put in "False" then it would be from highest-lowest

# the number of Nobel prizes per country, Prize is the aggregated column ,
# there's mean(), median(), min(), max()
nobel_prizes_for_country = df.groupby("Country")["Nobel Prices"].sum()
print(nobel_prizes_for_country)

# filter this by who has the highest number of nobel prizes
nobel_prizes_for_country_sorted = nobel_prizes_for_country.sort_values(ascending=False)
print(nobel_prizes_for_country_sorted)

# find the mean for the literacy rate for continent
literacy_rate_per_continent = df.groupby("Continent")["Literacy Rate"].mean()
print(literacy_rate_per_continent)
