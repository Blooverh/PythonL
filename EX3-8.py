locations= ["Dubai", "Qatar", "Angola", "Portugal", "Bulgaria"]
print(locations) #original list order
print(sorted(locations)) #temporarily sorted 
print(locations) #original list order
print(sorted(locations, reverse=True)) #temporarily reverse alphabetically the list
print(locations)

locations.reverse() #reverse order based on position of items in list 
print(locations)
locations.reverse() #reverse again to obtain original list 
print(locations)

locations.sort()#list in alphabetical order -> PERMANENT
print(locations)
locations.sort(reverse=True) #list in reverse alphabetical order -> PERMANENT
print(locations)
