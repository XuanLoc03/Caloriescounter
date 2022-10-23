import csv
user_data = [{'id':11511200, 'name':'Chocolate milk, ready to drink, reduced fat', 'weight':10, 'exp_date':'20-10-2022'},
             {'id':21500000, 'name':'Ground beef, raw', 'weight':4, 'exp_date':'24-10-2022'}]
gram = 0
def calculatecalo(foods_data):
    calo = 0
    ingres_data = [*csv.DictReader(open(r"C:\Users\Admin\Desktop\Portion.csv"))]
    ingres_data2 = [*csv.DictReader(open(r"C:\Users\Admin\Desktop\Nutrition.csv"))]
    for food in foods_data:
        print(food['name'])
        for ingre in ingres_data:
            if int(ingre['Food code']) == food['id'] and ingre['Descr'] != 'Quantity not specified':
                print(ingre['Descr'])
        choice = input('chon don vi?:')
        for ingre in ingres_data:
            if int(ingre['Food code']) == food['id'] and choice in ingre['Descr']:
                portion = int(input('Nhap so luong ban muon lay:'))
                gram = portion * int(ingre['weight'])
                for ingre2 in ingres_data2:
                    if ingre['Food code'] == ingre2['Food code']:
                        calo += int(ingre2['Energy']) *  (gram/100)
                        break
                break
    print(f'tong calo la: {calo} kcal')
calculatecalo(user_data)