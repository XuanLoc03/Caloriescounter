import csv
import pandas as pd
import streamlit as st
import datetime
#21500000

user_data = [{'id':11511200, 'name':'Chocolate milk, ready to drink, reduced fat', 'weight':10, 'exp_date':'20-10-2022'},
             {'id':21500000, 'name':'Ground beef, raw', 'weight':4, 'exp_date':'24-10-2022'}]
gram = 0
calo = 0
i = 0
protein = 0
carb = 0
fat = 0
prd_data = []
for food in user_data:
    prd_data.append(food['name'])
def calculatecalo(food,i,calo,):
    unit_data = pd.read_csv("C:\\Users\\Lenovo\\Desktop\\Portion.csv")
    ingres_data = pd.read_csv("C:\\Users\\Lenovo\\Desktop\\Nutrition.csv")
    foodcode = food['id']
    st.write(food['name'])
    unit = unit_data.loc[unit_data['Food code'] == foodcode]
    unitchoice = st.selectbox('Choose the unit:', unit['Descr'],key = i)
    unitgr = unit_data.loc[(unit_data['Food code'] == foodcode) & (unit['Descr'] == unitchoice)]
    portion = st.number_input('Enter the number you want to have:',key = i+1)
    gram = int(unitgr['weight']) * portion
    nutri = ingres_data.loc[ingres_data['Food code'] == foodcode]
    return gram,nutri
if st.button('Calculate nutrition'):
    for food in user_data:
        gram,nutri = calculatecalo(food,i,calo)
        calo += int(nutri['Energy']) * (gram / 100)
        protein += int(nutri['Protein (g)']) * (gram / 100)
        carb += int(nutri['Carbohydrate (g)']) * (gram / 100)
        fat += int(nutri['Total Fat (g)']) * (gram / 100)
        i+=2
    st.write('Total calo:',calo)
    st.write('Total carb:',carb)
    st.write('Total protein:',protein)
    st.write('Total fat:',fat)
else:
    st.write('Bye')

