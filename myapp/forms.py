from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, TextAreaField, SelectField, SubmitField, IntegerField,BooleanField, validators
from .samolijecenje import medicine_clean
from wtforms.validators import DataRequired, Optional, ValidationError

indikacije = medicine_clean['Indikacija']
indikacije_clean = set()
for ind in indikacije.values():
    i = ind.split(',')
    for x in i:
        indikacije_clean.add(x.title())

choices_list=[]
for clean in indikacije_clean:
    (a,b) = (clean, clean)
    choices_list.append((a,b))

#print(choices_list)

def validate_weight(form,field):
    """Custom validator that checks if age entered in form is above 12 and requires input in weight field if it is not"""

    weight_entered = field.data
    age_entered = form.age.data

    if int(age_entered) < 12 and int(weight_entered) == 0:  
        raise ValidationError('Molimo unesite težine za dijete mlađe od 12 godina!')
    
    

class Indication(FlaskForm):
    indikacija = SelectField('Odaberite vašu indikaciju: ', validate_choice=True, choices = choices_list, validators = [DataRequired()])
    age = IntegerField('Koliko imate godina?', validators=[DataRequired()])
    sex = RadioField('Spol:',  choices = [('M', 'Muško'), ('F','Žensko')], validators=[DataRequired()])
    weight = IntegerField('Težina:',default = 0,  validators = [Optional(), validate_weight])
    #pregnancy = RadioField('Jeste li trudni?', choices=['Da', 'Ne'], validators=[DataRequired()])

    submit_ind = SubmitField('Pregledaj')


   
            





class SelectMedicine(FlaskForm):
    select = RadioField('Odaberite željeni lijek:', validators = [DataRequired()])
    submit = SubmitField('Odaberi')

