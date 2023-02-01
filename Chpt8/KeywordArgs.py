def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type.lower()}.")
    print(f"My {animal_type.lower()}'s name is {pet_name.title()}.")
#multiple function calls
describe_pet(animal_type="dog", pet_name="flash")
describe_pet("cat","Mowgli")