import pandas as pd

print("SCRIPT STARTED")

df = pd.read_csv("../data/customers.csv")

df["name"] = df["name"].str.strip()

df["city"] = df["city"].str.strip().str.upper()

df["salary_band"] = df["salary"].apply(
    lambda x: "HIGH" if x > 500000 else "Medium"
)

print(df)

df.to_csv("../data/customers_cleaned.csv", index=False)

print("ETL process completed successfully.")
