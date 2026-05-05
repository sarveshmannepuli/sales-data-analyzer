import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")

df["revenue"] = df["price"] * df["quantity"]

total_revenue = df["revenue"].sum()
print("Total Revenue:", total_revenue)

product_sales = df.groupby("product")["revenue"].sum()
print("\nRevenue by Product:\n", product_sales)

top_product = product_sales.idxmax()
print("\nTop Product:", top_product)

product_sales.plot(kind="bar")
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.show()