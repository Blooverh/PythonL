import matplotlib.pyplot as plt

input_values=[1,2,3,4,5]
squares=[1,4,9,16,25]

#Using built- in styles
plt.style.use('seaborn')
fig, ax= plt.subplots() # fig -> represents the entire figure or collection of plots
ax.plot(input_values,squares, linewidth= 3) # linewidth sets the thickness of the line 


#set chart tittle and label axes
ax.set_title("square Numbers", fontsize= 24)
ax.set_xlabel("value", fontsize=14)
ax.set_ylabel("square of value", fontsize=14)

# set size of tick labels
ax.tick_params(axis='both', labelsize=14)

plt.show()