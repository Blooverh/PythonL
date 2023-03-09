import matplotlib.pyplot as plt
from random_walk import RandomWalk

#make random walk
while True:
    rw= RandomWalk(50_000) #increasing num_points to 50000 
    rw.fill_walk()

    #plot the points in the walk
    plt.style.use('classic')
    fig, ax= plt.subplots()
    point_numbers= range(rw.num_points) # point numbers are all num_points points that will be used for coloring on next line 
    ax.scatter(rw.x_val, rw.y_val, c=point_numbers, cmap=plt.cm.Reds, edgecolors='none', s=1) # s is changed from 15 to 1 since we have 50000 points which is a lot 

    #Emphasize the first and last points 
    ax.scatter(0,0, c='green', edgecolors='none',s=100)
    ax.scatter(rw.x_val[-1], rw.y_val[-1], c='red', edgecolors='none', s=100)

    # removing the y and x axis 
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running =='n':
        break
