#list is a collection of items in a particular order, anything can be put in a list 
#the items dont need to be related in any particular way
#brackets are seen as "[]"

cars= ["ford", "Audi", "Chevy", "porsche"]
print(cars)

# accessing elements in a list 
# lists are ordered collections, so we can get any element based on position (index)

print(cars[2])
print(cars[3].title())

#special syntax to access the last element in a list is [-1]
print(cars[-1]) #porsche

#using individual values from a list 
message= f"My first car was a {cars[0].title()} !"
print(message)

#modifying elements in list 
bike= "Ducati"
cars[2]= bike
print(cars[2])
print(cars) #after new modification
if(cars[2] == "Ducati"):
   alert= "false"
   print(alert)

#Appending elements at the end of a list (list).append
cars.append("Ferrari")
print(cars)\

#inserting elements in a list with specific index 
cars.insert(0, "Genesis") #adds at index 0 the new car, pushing the other elements to the next index 
print(cars)

#removing elements from a list 
del cars[4] # how to delete 
print(cars)

#removing an item using the pop() method
# -> pop() method removes the last item in a list (THINK OF IT AS A STACK POPING THE TOP OF THE STACK)
# but allows to work with said item after removing it and append to a different list 

motorcycles= ["yamaha", "suzuki", "ducati", "BMW"]
print(motorcycles)
popped_motorcycle= motorcycles.pop() #last element of the list popped and assigned to a new variable 
print(motorcycles) #print the list after popped item 
print(popped_motorcycle) #print popped item (last item of the list)

#pop can also remove any element in the list by expressing the index of the item to be removed 
popped_bike= motorcycles.pop(0) # pops item at index 0 (first item in the list in this example)
print(motorcycles)
print(popped_bike)

#removing an item by value 
pop_another_bike = motorcycles.remove('suzuki') #simply removes item, unlike pop it cannot be reused 
print(motorcycles)
# remove() method deleted only the first occurrence of the value specified
#if there is the same value in the list at a later index, this value will not be removed 

#3-4 Guest list:
peopleInvited = ["Hugo", "Catia", "Lara"]

message1=f"{peopleInvited[0]}, you are to be invited to my dinner"
print(message1)

#3-5 

print(f"{peopleInvited[2]}, you are uninvited as you are not able to appear")
peopleInvited.remove('Lara')
print(peopleInvited)
peopleInvited.append('Rohana') #appended to last index 
peopleInvited.insert(0, 'Bryan') #inserted at index 0
print(peopleInvited) #print new list with the 2 new additions
message1=f"{peopleInvited[0]}, you are to be invited to my dinner" #new message to new value at index 0
print(message1) 

#3-6 add 3 new people using append and insert
peopleInvited.append("Daniela")
peopleInvited.insert(2, 'Fernando')
peopleInvited.insert(1, "Pardo")
print(peopleInvited)

for i in range(len(peopleInvited)):
    new_message=f"{peopleInvited[i]}, new invitation for dinner"
    print(new_message)

#3-7 shrinking list to only 2 people
print(peopleInvited)
Pardo_pop=peopleInvited.pop(1) #index one popped 
print(f"{Pardo_pop}, you are not invited anymore")
print(peopleInvited)
Fernando_pop= peopleInvited.pop(2)
print(f"{Fernando_pop}, you are not invited anymore")
print(peopleInvited)
Daniela_pop=peopleInvited.pop(4)
print(f"{Daniela_pop}, you are not invited anymore")
print(peopleInvited)
Bryan_pop= peopleInvited.pop(0)
print(f"{Bryan_pop}, you are not invited anymore")
print(peopleInvited)
Hugo_pop= peopleInvited.pop(0)
print(f"{Hugo_pop}, you are not invited anymore")
print(peopleInvited)

for i in range(len(peopleInvited)):
    print(f"{peopleInvited[i]}, you are still invited for dinner")
print(peopleInvited)

del peopleInvited[0]
del peopleInvited[0]
print(peopleInvited)

#Organizing a list 
#Sorting a list permanently with sort() method 

names= ["Diogo", "Filipe", "Borges", "Aires"]
print(names)
names.sort() #orders in alphabetical order based on first character of each item
print(names)

#reverse aphabetical order 
names.sort(reverse=True)
print(names)

#sorting a list temporarily we use sorted() function
names= ["Diogo", "Filipe", "Borges", "Aires"]
print("original list: ")
print(names)

print("sorted list: ")
print(sorted(names))

print("original list: ")
print(names)

#printing a list in reverse order 
#reverse method changes the order of the list permanently and not the order alphabetically 
#however we can reverse it to original if we use reverse() method again
names.reverse()
print(names)
#reverse to original 
names.reverse()
print(names)

#Finding the length of a list 
print(len(names)) #length of the list 






