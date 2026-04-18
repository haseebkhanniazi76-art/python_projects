import pandas as pd
df_a=pd.read_csv("Shelter-a-data.csv")
df_b=pd.read_csv("Shelter-b-data.csv")

class RescuePet:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
        self.adopted = False

    def process_adoption(self):

        self.adopted = True
        print(f"the {self.name} of {self.species} has been adopted.")


combined_df = pd.concat([df_a, df_b])

combined_df.dropna()
dogs_df = combined_df[combined_df["Animal_Type"] == "Dog"].copy()

target_dog = dogs_df.iloc[0]
my_pet = RescuePet(target_dog["Pet_Name"], target_dog["Animal_Type"], target_dog["Age_Years"])


my_pet.process_adoption()


adopted_data = pd.DataFrame([{
    "Pet_Name": my_pet.name,
    "Animal_Type": my_pet.species,
    "Age_Years": my_pet.age,
    "Adoption_Status": my_pet.adopted
}])


adopted_data.to_csv("adopted_data.csv")
print("Current Dogs Available")
print(df)
