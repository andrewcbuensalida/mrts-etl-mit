import pandas as pd

# Define the data
data = {
    "sales_amount": [146376.00, 7258.00, 6358.00],
    "month": [1, 1, 1],
    "year": [1992, 1992, 1992, 1993, 1993, 1993],
    "kind_of_business": [
        "Hardware stores",
        "Hardware stores",
        "Women's clothing stores",
        "Women's clothing stores",
        "Men's clothing stores",
        "Men's clothing stores",
    ],
}
df = pd.DataFrame(data)

# Convert "month" and "year" columns to datetime format
df["date"] = pd.to_datetime(
    df["year"].astype(str) + "-" + df["month"].astype(str), format="%Y-%m"
)

# Set the "date" column as the index
df.set_index("date", inplace=True)
df.sort_index(inplace=True)


