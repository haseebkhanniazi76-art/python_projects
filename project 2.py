import pandas as pd
df=pd.read_csv("ingredents data.csv")
class Ingredient:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = float(quantity)

    def use_item(self, amount):
        if amount <= self.quantity:
            self.quantity -= amount
        else:
            print(f"Not enough {self.name} in stock!")
print(df)