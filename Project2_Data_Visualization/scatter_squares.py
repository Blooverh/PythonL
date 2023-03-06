import matplotlib.pyplot as plt

x_val=range(1,1001) # all nums between 1 and 1000
y_val=[x**2 for x in x_val] # square every x in list of x_val (square all nums 1 to 1000)

plt.style.use('seaborn')
fig, ax= plt.subplots() # fig -> represents the entire figure or collection of plots

ax.scatter(x_val,y_val,c=y_val, cmap=plt.cm.Blues,s=10)

ax.set_title("square Numbers", fontsize= 24)
ax.set_xlabel("value", fontsize=14)
ax.set_ylabel("square of value", fontsize=14)

#set the range for each axis
ax.axis([0,1100, 0, 1100000])

# set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=14) 
#to show plot
#plt.show()

# to save plot 
plt.savefig('squares_plot.py', bbox_inches='tight')