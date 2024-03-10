class MedicineManager:
    def __init__(self):
        self.drugs = {}

    def register_drugs(self):
        self.register_drug("Cocaine", "Cocaine is a tropane alkaloid that acts as a central nervous system stimulant. As an extract, it is mainly used recreationally, and often illegally for its euphoric and rewarding effects.")
        self.register_drug("Meth", "Methamphetamine, also known as Meth, is a potent central nervous system stimulant that is mainly used as a recreational drug and less commonly as a second-line treatment for attention deficit hyperactivity disorder and obesity.")

    def interact_with_user(self):
        while True:
            print("Please enter the name of a drug you wish to view information of (or 'quit' to exit):")
            for drug in self.drugs.values():
                print(drug.name)
            response = input().strip()
            if response == "":
                print("You entered an empty string. Please enter a valid drug name.")
                continue
            if response.lower() == "quit":
                break
            drug = self.get_drug_by_name(response)
            if drug is not None:
                print(f"\nName: {drug.name}")
                print(f"Description: {drug.description}\n")
            else:
                print("Sorry, I could not find any drug with that name.")
            print("Would you like to view another drug? (yes/no)")
            response = input()
            if response.lower() != "yes":
                break

    def register_drug(self, name, description):
        self.drugs[name.lower()] = Drug(name, description)

    def get_drug_by_name(self, name) -> str:
        return self.drugs.get(name.lower())

class Drug:
    def __init__(self,
        name: str,
        description: str
    ):
        self.name = name
        self.description = description

    def __str__(self) -> str:
        return f"Drug{{name='{self.name}', description='{self.description}'}}"
    
medicineMgr = MedicineManager()
medicineMgr.register_drugs()
medicineMgr.interact_with_user()