import matplotlib.pyplot as plt
from random_walk import RandomWalk

#make random walk
while True:
    rw= RandomWalk()
    rw.fill_walk()

    #plot the points in the walk
    plt.style.use('classic')
    fig, ax= plt.subplots()
    point_numbers= range(rw.num_points) # point numbers are all num_points points that will be used for coloring on next line 
    ax.scatter(rw.x_val, rw.y_val, c=point_numbers, cmap=plt.cm.Reds, edgecolors='none', s=15)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running =='n':
        break
