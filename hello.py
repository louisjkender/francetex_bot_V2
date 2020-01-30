from reportlab.pdfgen import canvas
from datetime import date
from reportlab.graphics.shapes import Rect
from reportlab.lib.colors import Color, black, blue, red

from flask import Flask, render_template, session, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from wtforms import SelectField

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField, IntegerField
from wtforms.validators import DataRequired, NumberRange
import random
from random import randint,choice,randrange


app=Flask(__name__)
moment=Moment(app)
bootstrap= Bootstrap(app)
app.config['SECRET_KEY'] = 'severine'

quantityfeuille=0
produitparfeuille=0
quantity=50
size=0
color=0
coeur=0
carre=0
big=0
marge=0
lock=True
class NameForm(FlaskForm):
        name = StringField('Quel est votre nom?', validators=[DataRequired()])
        submit = SubmitField('Faire le devis')


class FormDevis(FlaskForm):
        title = SelectField('Produit', [DataRequired()], choices=[('hoodie', 'hoodie'),('casquette', 'casquette'),('t-shirt','t-shirt'),('sweat','sweat')])
        quantity = IntegerField('Quantité?', validators=[NumberRange(min=0, max=1000)])
        printype=SelectField('Quelle impression souhaitez-vous', [DataRequired()], choices=[('impression', 'impression'),('broderie', 'broderie')])
        lettragecoeur = IntegerField('lettrage coeur?', validators=[NumberRange(min=0, max=10)])
        coeur = IntegerField('logo coeur?', validators=[NumberRange(min=0, max=10)])
        carre = IntegerField('logo carre?', validators=[NumberRange(min=0, max=10)])
        big = IntegerField('logo A4?', validators=[NumberRange(min=0, max=10)])
        color=IntegerField('Combien de couleur', validators=[NumberRange(min=0, max=10)])
        marge=IntegerField('Marge bénéficiaire (%+)', validators=[NumberRange(min=0, max=10)])
        submit = SubmitField('Calculer le prix des tshirts')


@app.route('/', methods=['GET', 'POST'])
def index():
            form = NameForm()
            if form.validate_on_submit():
                return redirect(url_for('bot', name=form.name.data,_external=True))
            return render_template('index.html',form = form, name = form.name.data)

@app.route('/bot/<name>', methods=['GET', 'POST'])
def bot(name):

    marge=0
    lettragecoeur=0
    form = FormDevis()

    quantity=form.quantity.data
    lettragecoeur=form.lettragecoeur.data
    coeur=form.coeur.data
    carre=form.carre.data
    big=form.big.data
    title=form.title.data
    color=form.color.data
    marge=form.marge.data
    if title=="hoodie":
         productprice=8
    if title=="casquette":
         productprice=2
    if title=='t-shirt':
        productprice=4
    if title=='sweat':
        productprice=6
    tax=2
    priceprint=0
    productvariable=0
    if lock==True:
            if coeur==0 and carre==0 and big==1:
                size=4
                produitparfeuille=1
            elif coeur==0 and carre==1 and big==0:
                size=4
                produitparfeuille=1
            elif coeur==1 and carre==0 and big==1:

                size=4
                produitparfeuille=1
            elif coeur==1 and carre==1 and big==0:

                size=4
                produitparfeuille=1
            elif coeur==2 and carre==1 and big==0:

                size=4
                produitparfeuille=1
            elif coeur==4 and carre==0 and big==0:
                size=4
                produitparfeuille=1
            elif coeur==2 and carre==1 and big==0:

                size=3
                produitparfeuille=1
            #feuille A3 et une seuille feuilleparproduit
            elif coeur==0 and carre==0 and big==2:
                size=3
                produitparfeuille=1
            elif coeur==0 and carre==1 and big==1:
                size=3
                produitparfeuille=1
            elif coeur==0 and carre==2 and big==0:
                size=3
                produitparfeuille=1
            elif coeur==1 and carre==2 and big==0:
                size=3
                produitparfeuille=1
            elif coeur==1 and carre==1 and big==1:
                size=3
                produitparfeuille=1
            elif coeur==2 and carre==0 and big==1:
                size=3
                produitparfeuille=1
            elif coeur==2 and carre==2 and big==0:
                size=3
                produitparfeuille=1
            elif coeur==2 and carre==1 and big==1:
                size=3
                produitparfeuille=1
            elif coeur==3 and carre==0 and big==1:
                size=3
                produitparfeuille=1
            elif coeur==3 and carre==2 and big==0:
                size=3
                produitparfeuille=1
            elif coeur==4 and carre==0 and big==1:
                size=3
                produitparfeuille=1
            elif coeur==3 and carre==1 and big==0:
                size=3
                produitparfeuille=1
            elif coeur==4 and carre==1 and big==0:
                size=3
                produitparfeuille=1
            elif coeur==4 and carre==2 and big==0:
                size=3
                produitparfeuille=1
            #autres exeptions
            elif coeur==1 and carre==0 and  big==0:
                 size=4
                 produitparfeuille=6
            elif coeur==2 and carre==0 and  big==0:
                 size=4
                 produitparfeuille=3
            elif coeur==3 and carre==0 and  big==0:
                 size=4
                 produitparfeuille=int(2)
    quantityfeuille=float(quantity)/float(produitparfeuille)
    if lock==True:
                           if color==1:
                              if quantityfeuille<=15:
                                       quantityfeuille=15
                              elif quantityfeuille>15 and quantityfeuille<=20:
                                       quantityfeuille=20
                              elif quantityfeuille>20 and quantityfeuille<=25:
                                       quantityfeuille=25
                              elif quantityfeuille>25 and quantityfeuille<=30:
                                       quantityfeuille=30
                              elif quantityfeuille>30:
                                 size=3
                           elif color>=2:
                              if quantityfeuille<=6:
                                  quantityfeuille=10
                              if quantityfeuille>6 and quantityfeuille<=10 :
                                 quantityfeuille=10
                              elif quantityfeuille>15 and quantityfeuille<=20:
                                 quantityfeuille=20
                              elif quantityfeuille>20 and quantityfeuille<=25:
                                 quantityfeuille=25
                              elif quantityfeuille>25 and quantityfeuille<=30:
                                 quantityfeuille=30
                              elif quantityfeuille>30:
                                 size=3
    if lock==True:

             if color==1:
                  if size==4:
                    if quantityfeuille==15:
                                feuilleprice=25
                    elif quantityfeuille==20:
                                feuilleprice=32
                    elif quantityfeuille==25:
                      feuilleprice=38
                    elif quantityfeuille==30:
                      feuilleprice=45
                  elif size==3:
                      if quantityfeuille==15:
                         feuilleprice=45
                      elif quantityfeuille==20:
                         feuilleprice=59
                      elif quantityfeuille==25:
                         feuilleprice=68
                      elif quantityfeuille==30:
                         feuilleprice=76
                      elif quantityfeuille==35:
                         feuilleprice=84
                      elif quantityfeuille==40:
                         feuilleprice=94
                      elif quantityfeuille==45:
                         feuilleprice=98
                      elif quantityfeuille==50:
                        feuilleprice=107
             elif color!=1:
                  if size==4:
                      if quantityfeuille==1:
                        feuilleprice=10.50
                      if quantityfeuille>1 and quantityfeuille<=6:
                        size=3
                        quantityfeuille=int(quantityfeuille/2)
                        if quantityfeuille==3:
                                feuilleprice=45.46
                        if quantityfeuille==4:
                                feuilleprice=60.48
                        if quantityfeuille==5:
                                feuilleprice=75.60
                        if quantityfeuille==6:
                                feuilleprice=90.72
                      if quantityfeuille>6:
                        size=3
                        quantityfeuille=int(quantityfeuille/2)
                        if quantityfeuille>6 and quantityfeuille<=10:
                              feuilleprice=89.50
                        if quantityfeuille>10 and quantityfeuille<=15:
                              feuilleprice=102
                        if quantityfeuille>15 and quantityfeuille<=21:
                              feuilleprice=107
                        if quantityfeuille>21 and quantityfeuille<=25:
                              feuilleprice=127
                        if quantityfeuille>25 and quantityfeuille<=30:
                              feuilleprice=153
                        if quantityfeuille>30 and quantityfeuille<=35:
                              feuilleprice=178
                  if size==3:
                           if quantityfeuille==1:
                                   feuilleprice=15.12
                           if quantityfeuille==2:
                                   feuilleprice=30.24
                           if quantityfeuille==3:
                                   feuilleprice=45.46
                           if quantityfeuille==4:
                                   feuilleprice=60.48
                           if quantityfeuille==5:
                                   feuilleprice=75.60
                           if quantityfeuille==6:
                                   feuilleprice=90.72


                           if quantityfeuille>6 and quantityfeuille<=10:
                               feuilleprice=89.50
                           if quantityfeuille>10 and quantityfeuille<=15:
                               feuilleprice=102
                           if quantityfeuille>15 and quantityfeuille<=21:
                               feuilleprice=107
                           if quantityfeuille>22 and quantityfeuille<=23:
                               feuilleprice=112
                           if quantityfeuille>22 and quantityfeuille<=23:
                                feuilleprice=117
                           if quantityfeuille>21 and quantityfeuille<=24:
                               feuilleprice=122
                           if quantityfeuille>24 and quantityfeuille<=41:
                               feuilleprice=127
                           if quantityfeuille>41 and quantityfeuille<=45:
                                 feuilleprice=139
                           if quantityfeuille>45 and quantityfeuille<=61:
                               feuilleprice=150
    feuilleprice=feuilleprice+9+0.80*quantity
    priceprint=feuilleprice
    tot=quantity*productprice+priceprint
    totTVA=tot+tot*tax/10

    tot=tot*(float(marge)+100)/100
    tot=round(tot,2)
    PU=tot/quantity
    PU=round(PU,2)
    return render_template('bot.html', name=name, form=form, quantity=form.quantity.data, tot=tot, totTVA=totTVA, lettragecoeur=lettragecoeur,coeur=coeur,carre=carre,big=big, produitparfeuille=produitparfeuille, feuilleprice=feuilleprice,color=color,PU=PU)
