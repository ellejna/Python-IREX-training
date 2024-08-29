import pandas as pd

# create a pandas series
products = ["Apple", "Banana", "Orange", "Pear"]
sales = [150, 30, 40, 55]
sales_series = pd.Series(sales, index=products)
print(sales_series)

# create a pandas DataFrame
data = {
    "Name": ["Alma", "Blerta", "Elena "],
    "Age": [21, 22, 19],
    "City": ["Pristina", "New York", "Chicago"],
}

dt_people = pd.DataFrame(data)
print(dt_people)
