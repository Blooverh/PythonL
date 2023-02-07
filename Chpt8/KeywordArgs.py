def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type.lower()}.")
    print(f"My {animal_type.lower()}'s name is {pet_name.title()}.")
#multiple function calls
describe_pet(animal_type="dog", pet_name="flash")
describe_pet("cat","Mowgli")

#defaul value usage in functionn and function calls
def pet_description(pet_name, animal_type='dog'):
    print(f"\nI have a {animal_type.lower()}.")
    print(f"My {animal_type.lower()}'s name is {pet_name.title()}.")

pet_description(pet_name='Flash')
#we can also use:
pet_description('Princess') #this call will automatically use princess as the non default value pet_name
