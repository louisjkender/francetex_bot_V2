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
tot=0
class NameForm(FlaskForm):
        name = StringField('Quel est votre nom?', validators=[DataRequired()])
        submit = SubmitField('Faire le devis')


class FormDevis(FlaskForm):
        title = SelectField('Produit', [DataRequired()], choices=[('hoodie', 'Sweat à capuche'),('casquetteTrucker', 'Casquette Trucker'),('casquettebaseball', 'Casquette Tissus Baseball'),('bonnet', 'Bonnet'),('t-shirt','t-shirt'),('sweat','sweat'),('TPB','T-shirt premium bio'),('sans produit','sans produit')])
        quantity = IntegerField('Quantité?', validators=[NumberRange(min=0, max=1000)])
        surnom=SelectField('Surnoms', [DataRequired()], choices=[(0, 'Aucun'),(1, 'Dos'),(2, 'Coeur'),(3, 'Les deux')])
        lettragecoeur = IntegerField('lettrage coeur?', validators=[NumberRange(min=0, max=10)])
        lettragedos=IntegerField('lettrage dos?', validators=[NumberRange(min=0, max=10)])
        coeur = IntegerField('logo coeur?', validators=[NumberRange(min=0, max=10)])
        carre = IntegerField('logo carre?', validators=[NumberRange(min=0, max=10)])
        big = IntegerField('logo A4?', validators=[NumberRange(min=0, max=10)])
        color=SelectField('Nombre de couleur logo', [DataRequired()], choices=[('1', '1'),('2', 'Multi')])
        marge=IntegerField('Marge bénéficiaire (%+)', validators=[NumberRange(min=0, max=100)])
        submit = SubmitField('Calculer')
        logocoeur=IntegerField('logo coeur', validators=[NumberRange(min=0, max=100)])
        logodos=IntegerField('logo dos', validators=[NumberRange(min=0, max=100)])


@app.route('/', methods=['GET', 'POST'])
def index():
            form = NameForm()
            if form.validate_on_submit():
                return redirect(url_for('bot', name=form.name.data,_external=True))
            return render_template('index.html',form = form, name = form.name.data)

@app.route('/bot/<name>', methods=['GET', 'POST'])
def bot(name):
    tot=0
    totTVA=0
    coeur=0
    carre=0
    big=0
    produitparfeuille=0
    feuilleprice=0
    color=0
    PU=0
    marge=0
    lettragecoeur=0
    form = FormDevis()
    frais=0
    quantity=1
    produitparfeuille=1
    lettragecoeur=0
    lettragedos=0
    logocoeur=0
    logodos=0
    priceprintimpression=0
    size=3
    productprice=0
    marge=0
    lettragedos=0
    color=form.color.data


    if color=="1":
        color=1
    elif color=="2":
        color=2

    surnom=0
    quantity=form.quantity.data
    lettragecoeur=form.lettragecoeur.data
    coeur=form.coeur.data
    carre=form.carre.data
    big=form.big.data
    title=form.title.data
    surnom=form.surnom.data
    logocoeur=form.logocoeur.data
    logodos=form.logodos.data
    priceprint=0

    marge=form.marge.data
    lettragedos=form.lettragedos.data
    if logocoeur is None:
        logocoeur=0
    if logodos is None:
        logodos=0
    if lettragecoeur is None:
        lettragecoeur=0
    if surnom is None:
        surnom=0
    if surnom is not IntegerField:
        surnom=0

    if marge is None:
        marge=0
    if quantity is None:
        quantity=1
    if productprice is None:
        productprice=0
    if priceprint is None:
        priceprint=0
    if title=="hoodie":
         productprice=7.5
    if title=="TPB":
        productprice=3.59
    if title=="casquetteTrucker":
         productprice=1.49
    if title=="casquettebaseball":
         productprice=2.05
    if title=='t-shirt':
        productprice=1.92
    if title=='sweat':
        productprice=5.35
    if title=='bonnet':
        productprice=1.40
    if title=='polo':
        productprice=3.44
    if title=='sans produit':
        productprice=0                                                              
                                           

    tax=2
    priceprint=0
    productvariable=0
    if color is None:
                color=0
    if lettragecoeur is None:
        lettragecoeur=0
    if lettragedos is None:
        lettragedos=0
    if coeur is None:
        coeur=0
    if carre is None:
        carre=0
    if big is None:
        big=0



    if coeur>0 or carre>0 or big>0:
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
        else:
            produitparfeuille=1
            quantity=10


        quantityfeuille=float(quantity)/float(produitparfeuille)
        print("quantity" +str(quantity))


    else:
        produitparfeuille=0
        quantityfeuille=0

    if lock==True:

                       if color==1:
                          if quantityfeuille >0 and quantityfeuille<=15:
                                   quantityfeuille=15
                          elif quantityfeuille>15 and quantityfeuille<=20:
                                   quantityfeuille=20
                          elif quantityfeuille>20 and quantityfeuille<=25:
                                   quantityfeuille=25
                          elif quantityfeuille>25 and quantityfeuille<=30:
                                   quantityfeuille=30
                          elif quantityfeuille>30:
                             size=3
                       elif color==2:
                          if quantityfeuille<=6 and quantityfeuille>0:
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

    print(size)
    if lock==True:

      if quantityfeuille>0:
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
                          elif quantityfeuille>25 and quantityfeuille<=30:
                             feuilleprice=76
                          elif quantityfeuille>30 and quantityfeuille<=35:
                             feuilleprice=84
                          elif quantityfeuille>35 and quantityfeuille<=40:
                             feuilleprice=94
                          elif quantityfeuille>40 and  quantityfeuille<=50:
                             feuilleprice=98
                          elif quantityfeuille==50:
                            feuilleprice=107
                          elif quantityfeuille>50 and quantityfeuille <=60:
                             feuilleprice=120
                          elif quantityfeuille>60 and quantityfeuille <=70:
                              feuilleprice=134
                          elif quantityfeuille>70 and quantityfeuille <=80:
                                 feuilleprice=146
                          elif quantityfeuille>80 and quantityfeuille <=90:
                               feuilleprice=152
                          elif quantityfeuille>90 and quantityfeuille <=100:
                               feuilleprice=162
                          elif quantityfeuille>100 and quantityfeuille <=125:
                               feuilleprice=185
                          elif quantityfeuille>125 and quantityfeuille <=150:
                               feuilleprice=215
                          elif quantityfeuille>150 and quantityfeuille <=175:
                               feuilleprice=235
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
                               if quantityfeuille>45 and quantityfeuille<61:
                                   feuilleprice=158
                               elif quantityfeuille>60 and quantityfeuille <=70:
                                      feuilleprice=182
                               elif quantityfeuille>70 and quantityfeuille <=80:
                                      feuilleprice=208
                               elif quantityfeuille>80 and quantityfeuille <=100:
                                    feuilleprice=220
                               elif quantityfeuille>100 and quantityfeuille <=110:
                                    feuilleprice=242
                               elif quantityfeuille>110 and quantityfeuille <=120:
                                    feuilleprice=264
                               elif quantityfeuille>120 and quantityfeuille <=130:
                                    feuilleprice=286
                               elif quantityfeuille>130 and quantityfeuille <=145:
                                    feuilleprice=319

                               elif quantityfeuille>145 and quantityfeuille <=160:
                                   feuilleprice=352

                               elif quantityfeuille>160 and quantityfeuille <=200:
                                   feuilleprice=380
                               elif quantityfeuille>200 and quantityfeuille <=300:
                                   feuilleprice=575

                 print("feuilleprice only "+str(feuilleprice))
                 feuilleprice=feuilleprice+9+0.80*quantity
                 priceprint=feuilleprice
      else:
               priceprint=0


    print("number of color "+str(color))
    print("price of print " +str(priceprint))
    print(" number of feuille " +str(quantityfeuille))


    if lettragecoeur>0 or logocoeur>0 or lettragedos>0 or logodos>0 or surnom>0:
        priceprintimpression=priceprint
        priceprint=0


        if lettragecoeur>0:
          lettragecoeur=lettragecoeur*quantity
          if lettragecoeur<=9:
              priceprint+=7.5
          elif lettragecoeur>9 and lettragecoeur<=24:
              priceprint+=3.50
          elif lettragecoeur>24 and lettragecoeur<=49:
              priceprint+=2.50
          elif lettragecoeur>49 and lettragecoeur<149:
              priceprint+=1.80
          elif lettragecoeur>149 and lettragecoeur<499:
              priceprint+=1.50
          elif lettragecoeur>499 and lettragecoeur<2000:
              priceprint+=1.30
          else:print('sur devis')
          frais=0
          frais=frais+30
        if logocoeur>0:
          logocoeur=logocoeur*quantity

          if logocoeur<=9:
              priceprint=priceprint+10
          elif logocoeur>9 and logocoeur<=24:
              priceprint=priceprint+4.50
          elif logocoeur>24 and logocoeur<=49:
              priceprint=priceprint+3.50
          elif logocoeur>49 and logocoeur<149:
              priceprint=priceprint+3
          elif logocoeur>149 and logocoeur<499:
              priceprint=priceprint+2.50
          elif logocoeur>499 and logocoeur<2000:
              priceprint=priceprint+2
          else:print('sur devis')
          print(frais)
          print(priceprint)
          frais=frais+40
        if lettragedos>0:
             lettragedos=lettragedos*quantity
             if lettragedos<=9:
                 priceprint=priceprint+15
             elif lettragedos>9 and lettragedos<=24:
                 priceprint=priceprint+7
             elif lettragedos>24 and lettragedos<=49:
                 priceprint=priceprint+5
             elif lettragedos>49 and lettragedos<149:
                 priceprint=priceprint+3.5
             elif lettragedos>149 and lettragedos<499:
                 priceprint=priceprint+3
             elif lettragedos>499 and lettragedos<2000:
                 priceprint=priceprint+2.50
             else:print('sur devis')
             frais=frais+50
        print(priceprint)
        if logodos>0:
           logodos=logodos*quantity
           if logodos<=9:
               priceprint=priceprint+15
           elif logodos>9 and logodos<=24:
               priceprint=priceprint+7
           elif logodos>24 and logodos<=49:
               priceprint=priceprint+5
           elif logodos>49 and logodos<149:
               priceprint=priceprint+3.5
           elif logodos>149 and logodos<499:
               priceprint=priceprint+3
           elif logodos>499 and logodos<2000:
               priceprint=priceprint+2.50
           else:print('sur devis')
           frais=frais+70
        print(priceprint)
        if surnom >0:
            if surnom==1:
                surnom=quantity
                if surnom<=10:
                    priceprint=priceprint+10
                elif surnom>10 and surnom<=49:
                    priceprint=priceprint+7
                elif surnoms>49 and surnom<=200:
                    priceprint=priceprint+5
            elif surnom==2:
                surnom=quantity
                if surnom<=10:
                    priceprint=priceprint+5
                elif surnom>10 and surnom<=49:
                    priceprint=priceprint+3.5
                elif surnoms>49 and surnom<=200:
                    priceprint=priceprint+2.5

            elif surnom==3:
                surnom=quantity
                if surnom<=10:
                    priceprint=priceprint+5+10
                elif surnom>10 and surnom<=49:
                    priceprint=priceprint+3.5+7
                elif surnoms>49 and surnom<=200:
                    priceprint=priceprint+2.5+5

        print(priceprint)
        priceprint=priceprint*quantity+frais+10


    tot=quantity*productprice+priceprint+priceprintimpression
    print(quantity*productprice)
    totnoprofit=tot
    tot=tot*(float(marge)+100)/100
    totTVA=tot+tot*tax/10
    totTVA=round(totTVA,2)


    tot=round(tot,2)
    PU=tot/quantity
    PU=round(PU,2)
    profit=tot-totnoprofit
    profit=round(profit,2)
    return render_template('bot.html', name=name, form=form, quantity=form.quantity.data, tot=tot, totTVA=totTVA, lettragecoeur=lettragecoeur,coeur=coeur,carre=carre,big=big, produitparfeuille=produitparfeuille, feuilleprice=feuilleprice,color=color,PU=PU,priceprint=priceprint, profit=profit)
