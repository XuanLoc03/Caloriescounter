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
def calculatecalo(food,i,calo):
    unit_data = pd.read_csv("C:\\Users\\Admin\\Desktop\\Portion.csv")
    ingres_data = pd.read_csv("C:\\Users\\Admin\\Desktop\\Nutrition.csv")
    foodcode = food['id']
    st.write(food['name'])
    unit = unit_data.loc[unit_data['Food code'] == foodcode]
    unitchoice = st.selectbox('Choose the unit:', unit['Descr'],key = i)
    unitgr = unit_data.loc[(unit_data['Food code'] == foodcode) & (unit['Descr'] == unitchoice)]
    portion = st.number_input('Enter the number you want to have:',key = i+1)
    gram = int(unitgr['weight']) * portion
    nutri = ingres_data.loc[ingres_data['Food code'] == foodcode]
    calo += int(nutri['Energy']) * (gram/100)
    return calo
for food in user_data:
    if calo == 0:
        calo = calculatecalo(food,i,calo)
    else:
        calo = calculatecalo(food,i,calo)
    i +=2
st.write('Total calo:',calo)