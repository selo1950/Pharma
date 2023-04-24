from flask import Flask, render_template, request,redirect, url_for, Blueprint
from .forms import Indication, SelectMedicine
from flask_wtf import FlaskForm
from .samolijecenje import medicine_clean

main = Blueprint('main', __name__)



@main.route('/', methods = ['GET', 'POST'])
def homepage():
    indicat = Indication()
    if indicat.validate_on_submit():
        ind = indicat.indikacija.data
        age = indicat.age.data
        sex = indicat.sex.data
        child_weight = indicat.weight.data

        if child_weight:
            return redirect (url_for('main.choose_medicine', ind=ind, age=age, child_weight = child_weight))
        else:
            return redirect (url_for('main.choose_medicine', ind=ind, age=age, child_weight = 'zero'))
        
    return render_template('homepage.html', indication = Indication())

            
@main.route('/choose_medicine/<ind>/<age>/<child_weight>', methods = ['GET', 'POST'])
def choose_medicine(ind, age, child_weight):
    medicines = []
    select_medicine = SelectMedicine()
    for x in range(len(medicine_clean['Lijek'])):
        if int(age) < medicine_clean['Min.dob'][str(x)]:
            continue
        else:
            if int(age) < 12 and medicine_clean['Doza-djeca'][str(x)] == 'X':
                continue
            else:
                if ind in medicine_clean['Indikacija'][str(x)]:
                    name = medicine_clean['Lijek'][str(x)]
                    medicines.append((name,name))
    select_medicine.select.choices = medicines


    if select_medicine.validate_on_submit():
         med = select_medicine.select.data
         print(select_medicine.select.data)
         return redirect (url_for('main.information', name = med, age = age, ind = ind, child_weight = child_weight))

    return render_template('choose_medicine.html', select_medicine = select_medicine, ind = ind)
 
       
@main.route('/information/<name>/<age>/<ind>/<child_weight>')
def information(name,age,ind,child_weight):
     for x in range(len(medicine_clean['Lijek'])):    
        if name in medicine_clean['Lijek'][str(x)]: 

            if int(age) < 12:
                descript = medicine_clean['Opis-djeca'][str(x)]
                dose = medicine_clean['Doza-djeca'][str(x)]
                dose_clean = [int(y) for y in dose.split() if y.isdigit()]
                max_dose = medicine_clean['Maksimalna doza-djeca'][str(x)]
                max_dose_clean = [int(y) for y in max_dose.split() if y.isdigit()]
                

                if 'mg/kg' in dose: 
                    doza = f'{child_dose(child_weight, dose_clean[0],max_dose_clean[0] )[0]} mg'
                    frequency = child_dose(child_weight, dose_clean[0],max_dose_clean[0])[1]
                else:
                    doza = medicine_clean['Doza-djeca'][str(x)]

            else:
                doza = medicine_clean['Doza-odrasli'][str(x)]
                frequency = medicine_clean['Ucestalost'][str(x)]
                descript = medicine_clean['Opis-odrasli'][str(x)]
            return render_template('information.html', name = name, doza = doza, ind = ind, frequency = frequency, descript = descript)

def child_dose(child_weight, dose_clean, daily_dose):
    single_dose = int(child_weight)* int(dose_clean)
    frequency = round(int(daily_dose)*int(child_weight)/int(single_dose))
    return single_dose, frequency









    
     


