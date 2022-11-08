import sqlite3
import streamlit as st
from datetime import date
calo = 2300
con = sqlite3.connect('Usercalo.db')
cu = con.cursor()
cu.execute("SELECT Date FROM User")
checkdate = cu.fetchall()
if date.today() not in checkdate:
        cu.execute("INSERT INTO User VALUES (?,?,?)",('Duong',calo,date.today()))
else:
        cu.execute('SELECT Calo FROM User WHERE Date = ?',date.today())
        oldcalo = cu.fetchone()
        calo += oldcalo
        cu.execute("UPDATE User SET Calo = ? where Date = ?",(calo,date.today()))

date1 = st.date_input("Enter the start date")
date2 = st.date_input("Enter the end date")
def hienthi(cu,date1,date2):
        cu.execute("SELECT Date,Calo FROM User WHERE Date BETWEEN (?) AND(?) ",(date1,date2))
        calo1 = cu.fetchall()
        res_dict = {}
        Date = []
        Calo = []
        for option in calo1:
                Date.append(option[0])
                Calo.append(option[1])
        res_dict['Date'] = Date
        res_dict['Calo'] = Calo
        st.line_chart(data = res_dict,x='Date',y ='Calo')
hienthi(cu,date1,date2)