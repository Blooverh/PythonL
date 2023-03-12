import csv
from plotly.graph_objs import Bar, Layout
from plotly import offline

filename='Data\dataExample.csv'
with open(filename) as f:
    reader= csv.reader(f)
    header_row= next(reader) #returns the next line in the file when passed the reader object 
    #print(header_row) #prints the headers from the first row in the file 

    # printing the headers and their positions
    for index, column_header in enumerate(header_row):
        print(index, column_header)
# enumerate() function returns both the index of each item and the item itself as we loop through the list 

    #Extracting and reading data
    jobsInHouston=[]
    jobsSomewhereElse=[]
    for row in reader:
        job= row[3]
        if job == 'Houston':
            jobsInHouston.append(job)
        else:
            jobsSomewhereElse.append(job)

        
print()
print(f"Up to the date: 03/09/2023 I applied to {len(jobsInHouston)} in Houston")
#Here some rows are empty an they are accounted for in this example
print(f"as of 03/09/2023 I have applied to {len(jobsSomewhereElse)} outside of the Houston area")

#Making the Histogram
jobsLen= len(jobsInHouston) + len(jobsSomewhereElse)
x_values= ['Houston Jobs', 'Outside Houston Jobs']
y_values= [len(jobsInHouston), len(jobsSomewhereElse)]
data=[Bar(x=x_values, y=y_values)]

x_axis_config= {'title': 'Houston vs Outside Houston', 'dtick':1}
y_axis_config={'title': 'Number of jobs applied'}

my_layout=Layout(title='Comparison between how many jobs applied in Houston and outside of Houston', xaxis=x_axis_config, yaxis= y_axis_config)

offline.plot({'data':data, 'layout':my_layout}, filename="applicationAnalysis.html")
print(jobsLen)
