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
