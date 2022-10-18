import pandas as pd
xldata = pd.read_csv('C:\\Users\\Admin\\PycharmProjects\\food.csv')
choice0 = input('Enter the name of the ingredient: ')
choice1 = xldata.loc[xldata['Category']== choice0]
print(choice1['Description'])
type = int(input('Pick the number which contains the type of food you want:'))
choice = xldata.loc[type]
print(choice)
print(xldata.loc[type,"Data.Cholesterol"])