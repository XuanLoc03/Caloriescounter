import streamlit as st
import csv
user_data = [{'id':11511200, 'name':'Chocolate milk, ready to drink, reduced fat', 'weight':10, 'exp_date':'20-10-2022'}]
gram = 0
def calculate(foods_data):
    ingres_data = [*csv.DictReader(open(r"C:\Users\Admin\Desktop\Portion.csv"))]
    ingres_data2 = [*csv.DictReader(open(r"C:\Users\Admin\Desktop\Nutrition.csv"))]
    unit = {}
    calo = 0
    portion = {}
    for food in foods_data:
        foodcode = food['id']
        unit[foodcode] = []
        for ingre in ingres_data:
            if int(ingre['Food code']) == food['id'] and ingre['Descr'] != 'Quantity not specified':
                unit[foodcode].append(ingre['Descr'])
        st.write('Chon don vi cua san pham',food['name'])
        choice = st.selectbox('Chon don vi',unit[foodcode])
        for ingre in ingres_data:
            if int(ingre['Food code']) == food['id'] and choice == ingre['Descr']:
                portion[foodcode] = st.number_input('Nhap so luong',key = foodcode)
                gram = portion[foodcode] * int(ingre['weight'])
                st.write('Vay so luong gram la(g): ',gram)
                break
        for ingre2 in ingres_data2:
            if int(ingre2['Food code']) == foodcode:
                calo += float(ingre2['Energy']) * float(gram / 100)
                break
    st.write('Tong calo la(kcal)', calo)
if st.button('Tinh calo?'):
    calculate(user_data)