import pandas as pd
# Sales Dataset
data = {
    "Product": ["Laptop","Phone","Laptop","Tablet","Phone","Tablet","Laptop"],
    "City": ["Chennai","Chennai","Bangalore","Chennai","Bangalore","Chennai","Chennai"],
    "Quantity": [5,10,3,8,6,4,5],
    "Sales": [50000,30000,45000,20000,25000,18000,50000]
}
df = pd.DataFrame(data)

# Add missing values
df.loc[2, "Sales"] = None
df.loc[4, "Quantity"] = None
print("Original Data:\n", df)

# 1. Detect and count missing values
print("\nMissing Values:")
print(df.isnull().sum())

# 2. Remove missing values
removed = df.dropna()
print("\nAfter Removing Missing Values:")
print(removed)

# 3. Fill missing values
df["Sales"] = df["Sales"].fillna(df["Sales"].mean())
df["Quantity"] = df["Quantity"].fillna(df["Quantity"].mean())
print("\nAfter Filling Missing Values:")
print(df)

# 4. Grouping
print("\nTotal Sales by Product:")
print(df.groupby("Product")["Sales"].sum())