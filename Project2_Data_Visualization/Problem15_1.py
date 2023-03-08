import matplotlib.pyplot  as plt

x_val=range(1,5001)
y_val= [x**3 for x in x_val]

plt.style.use('seaborn')
fig, ax= plt.subplots()

ax.scatter(x_val, y_val, c=y_val, cmap=plt.cm.Reds, s=10)

ax.set_title("cube Numbers", fontsize= 24)
ax.set_xlabel("value", fontsize=14)
ax.set_ylabel("cube of value", fontsize=14)

ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()