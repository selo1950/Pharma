from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, TextAreaField, SelectField, SubmitField, IntegerField,BooleanField
from samolijecenje import medicine_clean
from wtforms.validators import DataRequired

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



class Indication(FlaskForm):
    indikacija = SelectField('Odaberite vašu indikaciju: ', validate_choice=True, choices = choices_list, validators = [DataRequired()])
    age = IntegerField('Koliko imate godina?', validators=[DataRequired()])
    sex = RadioField('Spol:',  choices = [('M', 'Muško'), ('F','Žensko')], validators=[DataRequired()])
    weight = IntegerField('Težina:')
    #pregnancy = RadioField('Jeste li trudni?', choices=['Da', 'Ne'], validators=[DataRequired()])

    submit_ind = SubmitField('Pregledaj')

class SelectMedicine(FlaskForm):
    select = RadioField('Odaberite željeni lijek:', validators = [DataRequired()])
    submit = SubmitField('Odaberi')

