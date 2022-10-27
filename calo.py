import csv
import pandas as pd
import streamlit as st
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
prd_total = []
foodid = 0
for food in user_data:
    prd_data.append(food['name'])
def calculatecalo(foodcode,i):
    unit_data = pd.read_csv("C:\\Users\\Lenovo\\Desktop\\Portion.csv")
    ingres_data = pd.read_csv("C:\\Users\\Lenovo\\Desktop\\Nutrition.csv")
    unit = unit_data.loc[unit_data['Food code'] == foodcode]
    unitchoice = st.selectbox('Choose the unit:', unit['Descr'],key = i+1)
    unitgr = unit_data.loc[(unit_data['Food code'] == foodcode) & (unit['Descr'] == unitchoice)]
    portion = st.number_input('Enter the number you want to have:',key = i+2)
    gram = int(unitgr['weight']) * portion
    nutri = ingres_data.loc[ingres_data['Food code'] == foodcode]
    return gram,nutri
if 'button_clicked' not in st.session_state:
    st.session_state.button_clicked = False
def callback():
    st.session_state.button_clicked = True
if st.button('Add',on_click= callback) or st.session_state.button_clicked:
    options = st.selectbox('Choose product',prd_data,key = i)
    if options:
        for food1 in user_data:
            if food1['name'] == options:
                foodid = food1['id']
                break
        gram,nutri = calculatecalo(foodid,i)
        calo += int(nutri['Energy']) * (gram / 100)
        protein += int(nutri['Protein (g)']) * (gram / 100)
        carb += int(nutri['Carbohydrate (g)']) * (gram / 100)
        fat += int(nutri['Total Fat (g)']) * (gram / 100)
        i+=2
st.write('Total calo:',calo)
st.write('Total carb:',carb)
st.write('Total protein:',protein)
st.write('Total fat:',fat)