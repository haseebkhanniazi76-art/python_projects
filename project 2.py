import pandas as pd
df=pd.read_csv("morning_stock.csv")
class Ingredient:
    def __init__(self,ingredient,Qty_kg,cost_per_kg):
        self.ingredient = ingredient
        self.Qty_kg = Qty_kg
        self.cost_per_kg=cost_per_kg
        

    def use_item(self, amount):
        if amount <= self.Qty_kg
            self.Qty_kg -= amount
        else:
            print(f"Not enough {self.name} in stock!")
df.rename(column={"Qty_kg" : "current_quantity"})
cofee_row=df[df["ingredient"]=="cofee_beans["current_Quantity"].iloc[0]
beans_object=ingredient(cofee_row["ingredient"],cofee_row["current_quantity])
beans_object.use_items(2.5)
df.loc[df["ingredient"]=="cofee_beans."current_Quantity"]=beans_Object.quantity
df.to_csv("evening_Stock.csv",index=false)

