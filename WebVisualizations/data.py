#using pandas read csv file
import pandas as pd 
dataframe = pd.read_csv('cities.csv')

#save file as html
dataframe.to_html("data.html", index=False)
datatbl = dataframe.to_html()
#print to verify success
print(datatbl)