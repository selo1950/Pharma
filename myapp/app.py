from flask import Flask, render_template, request,redirect, url_for, Blueprint
from forms import Indication, SelectMedicine
from flask_wtf import FlaskForm
from samolijecenje import medicine_clean

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Aguero16'


@app.route('/', methods = ['GET', 'POST'])
def homepage():
    indicat = Indication()
    if indicat.validate_on_submit():
        ind = indicat.indikacija.data
        age = indicat.age.data
        sex = indicat.sex.data
        child_weight = indicat.weight.data
        return redirect (url_for('choose_medicine', ind=ind, age=age, child_weight = child_weight))
    return render_template('homepage.html', indication = Indication())

            
@app.route('/choose_medicine/<ind>/<age>/<child_weight>', methods = ['GET', 'POST'])
def choose_medicine(ind, age, child_weight):
    medicines = []
    select_medicine = SelectMedicine()
    for x in range(len(medicine_clean['Lijek'])):    
            if ind in medicine_clean['Indikacija'][str(x)]:
                name = medicine_clean['Lijek'][str(x)]
                medicines.append((name,name))
    select_medicine.select.choices = medicines


    if select_medicine.validate_on_submit():
         med = select_medicine.select.data
         print(select_medicine.select.data)
         return redirect (url_for('information', name = med, age = age, ind = ind, child_weight = child_weight))

    return render_template('choose_medicine.html', select_medicine = select_medicine, ind = ind)
 
       
@app.route('/information/<name>/<age>/<ind>/<child_weight>')
def information(name,age,ind,child_weight):
     for x in range(len(medicine_clean['Lijek'])):    
        if name in medicine_clean['Lijek'][str(x)]: 
                #if pregnancy == 'DA' and medicine_clean['Trudnoca'][str(x)] == 'Ne':
                    #print(f'Lijek {name} se ne preporučuje trudnicama.')
                #else:
            if int(age) < 12:
                dose = medicine_clean['Doza-djeca'][str(x)]
                dose_clean = [int(y) for y in dose.split() if y.isdigit()]
                if 'mg/kg' in dose: 
                    doza = f'{child_dose(child_weight, dose_clean[0])} mg'     
                else:
                    doza = medicine_clean['Doza-djeca'][str(x)]
            else:
                doza = medicine_clean['Doza-odrasli'][str(x)]
            return render_template('get_advice.html', name = name, doza = doza, ind = ind)

def child_dose(child_weight, dose_clean):
    single_dose = int(child_weight)* int(dose_clean)
    return single_dose

app.run(debug=True)






    
     


