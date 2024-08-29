import pandas as pd
# kaggle average global iq per country with other states, search this on yt and convert the zip file
df = pd.read_csv("data/avgIQpercountry.csv")
print(df.head())
print(df.info())

# select only the tro columns that are needed
subset = df[["Country", "Average IQ"]]
print(subset)

# see countries and info for those whos IQ is above 100

filtered_df = subset[subset["Average IQ"] > 100]
print(filtered_df)

#handle an example where the data is missing or has duplicates
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

