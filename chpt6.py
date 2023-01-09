alien_o={'color':'green', 'points': 5 }
print(alien_o['color'])
print(alien_o['points'])

alien_o['x-position']=0 #key : value -> key = string / value= 0
alien_o['y-position']=25
print(alien_o)

#Starting with an empty dictionary
alien_o={} #empty dictionary
alien_o['color']='green'
alien_o['points']=5
print(alien_o)

#modifying values in a dictionary
alien_o['color']='red' #we modify color from green to red
print(f"The color of the alien is {alien_o['color']}!")

alien_o={'x_position':0, 'y-positions':25, 'speed': 'medium'}
print(f"Original position: {alien_o['x_position']}")

if alien_o['speed'] == 'slow':
    x_increment=1
elif alien_o['speed'] == 'medium':
    x_increment=2
elif alien_o['speed'] =='fast':
    x_increment=3
else:
    x_increment=4

alien_o['x_position']=alien_o['x_position']+x_increment
print(f"New position is: {alien_o['x_position']}")

#REMOVING KEY VALUE PAIRS
alien_o={'color':'green', 'points': 5 }
del alien_o['points']
print(alien_o)

#A dictionary of similar objects

fav_languages={'Diogo': "Java", "Rohana": "Python", "Bryan":"JavaScript"}
language=fav_languages['Rohana'].title()
print(f"Rohana's favortie programming language is: {language}")

#Using get() method to access values 
#get methods used to set a dafault value that will be returned if the requested key does not exist
#Example: 
teams={"Country": "Portugal", "Color":"red", "Team":"Benfica"}
point_value=teams.get("points", "No point value assigned in the dictionary")
print(point_value)

#####
#6-1 exercise 
personal_info={
    "first_name":"Diogo",
    "last_name":"Aires",
    "age":23,
    "city":"Houston"
}

for i in personal_info:
    print(f" {i.title()}, is {personal_info[i]}")

print(personal_info) #prints the dictionary

#### 
#Looping through a dictionary 
#6-2 exercise
favNums={"Diogo":28, "Rohana":3, "hugo":19, "Catia":40}

for i in favNums:
    print(f"{i.title()}'s favorite number is: {favNums[i]}")   
####### DIFFERENT WAY OF ACCESSING THE DICTIONARY
for k,v in dict.items(favNums):
    print(f"{k.title()}'s favorite number is: {v}") 

print()
#looping through all the keys in a dictionary 
for name in favNums.keys(): #same as doing -> for name in favNums: -> because keys are the default values when looping through the dictionary 
    print(name.title())

for nums in favNums.values():
    print(nums)

#looping through dictionary in particular order

fav_idioms={
    "diogo":"Portuguese", 
    "rohana":"Malialam",
    "hugo":"spanish", 
    "catia":"French"
}

for name in sorted(fav_idioms):
    print(f"{name.title()}, take you for taking the poll!")
print()
#looping through all values in dictionary 
for idiom in fav_idioms.values():
    print(idiom.title())


print()
###################################
#SET() EXAMPLE
fav_idioms={
    "diogo":"Portuguese", 
    "rohana":"Malialam",
    "hugo":"spanish", 
    "catia":"Portuguese"
}

for idiom in set(fav_idioms.values()):
    print(idiom.title())

# When wrapping a set() around a list that contains duplicate items. 
# Python identifies the unique items in the list and builds a set from those items 

# Building a set 
# languages = {"python", "java", "JS"} etc....

### 6-5
rivers={
    "nile":"egypt",
    "Sado":"Portugal",
    "Mississipi":"USA"
}
print()
for k, v in dict.items(rivers):
    print(f"{k.title()} runs through the country of {v.title()}")

print()

for river in rivers:
    print(river.title())
print()
for country in rivers.values():
    print(country.title())
print()

#6-6
fav_idioms={
    "diogo":"Portuguese", 
    "rohana":"Malialam",
    "hugo":"spanish", 
    "catia":"Portuguese"
}

people=["Daniela","Isa","Fernando", "Bryan", "Sergio","diogo","rohana"]

for person in people:
    if person in fav_idioms.keys():
        print(f"{person.title()}, thank you for polling")
    else:
        print(f"{person.title()}, please take the poll, we are missing your vote!")
print()
print()
### NESTING DICTIONARIES
alien_0={"color":"green", "points":5}
alien_1={"color":"yellow", "points":10}
alien_2={"color":"red", "points":15}

aliens=[alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
print()
print()

aliens=[] #empty list 

#make 30 aliens
for alienNum in range(30):
    new_alien= {"color":"red", "points":15, "speed":"slow"}
    aliens.append(new_alien)

#showing first 5 elements 
print("The first 5 aliens are:")
for alien in aliens[:5]:
    print(alien)
print("............")
print(f"total number of aliens is {len(aliens)}")


