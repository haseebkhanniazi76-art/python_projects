import pandas as pd
df=pd.read_csv("products.csv")
class Product:
    def __init__(self,product_id,catagory,price):
        self.prod_id = product_id
        self.catagory = catagory
        self.price = float(price)

    def apply_discount(self, percent_off):
        discount_amount = self.price * (percent_off / 100)
        self.price -= discount_amount


electronics_df = df[df["Category"] == "Electronics"].copy()

discounted_price = []

for i, r in electronics_df.iterrows():
    item = Product(r["product_id"], r["price"])

    item.apply_discount(20)

    discounted_price.append(item.price)

electronics_df["Price"] = discounted_price
electronics_df["Promo_Active"] = "Yes"
electronics_df.to_excel("holiday_promos.xlsx")
print(electronics_df)
