from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

#create a die with default value of sides D6
die= Die()
die2=Die(10)

results=[] # start as empty list that will store every roll of the die
for roll in range(1000):
    result= die.roll()+ die2.roll()
    results.append(result)

frequencies =[] # empty list to store the frequencies of each number in the die ]
max= die.num_sides +die2.num_sides
for value in range(2, max+1):
    frequency = results.count(value) # -> IMPORTANT
    frequencies.append(frequency)

# print(results)
# print(frequencies)

#MAKING A HISTOGRAM 
x_val= list(range(2, max+1))
data=[Bar(x=x_val, y = frequencies)] #data is created as a list of bars that contain x as the x values and y as its frequencies

#dictionary needed to configure the title and title name
x_axis_config= {'title': 'result', 'dtick':1}
y_axis_config={'title':'frequency of result'}
# Then attach each dictionary to correct axis 
my_layout=Layout(title='Results of rolling two dices 100 times one dice with 6 sides, other with 10 sides', xaxis= x_axis_config, yaxis= y_axis_config)

#offline plot, plots the histogram in local host with a designated file
offline.plot({'data': data, 'layout':my_layout}, filename='d6_d10.html')