from flask import Flask, render_template, redirect,request,session
import random
import time
from datetime import datetime


app=Flask(__name__)
app.secret_key="hithere"

def content():
  session['color']="green"
  green=session['color']
  data ="Earned {} golds from {} ! ({})".format(str(session['gold']),session['building'],session['timestamp']),green
  session['total']=session['total']+session['gold']
  session['output'].append((data))
  
      
@app.route('/')
def root():
    
    if "total" not in session:
        session['total']=0
    if "output" not in session:
        session['output']=[]
    return render_template('index.html')

@app.route('/process_money',methods=['POST'])
def process_money():

    session['timestamp'] = datetime.now().strftime('%Y/%m/%d %I:%M %p') 
    session['color']=""
    session['building']=request.form['building']
    session['red']=""
       
    if session['building']=='farm':
        session['gold']=random.randrange(10, 20)
        content()
        session['color']="green"
    elif session['building']=='cave':
        session['gold']=random.randrange(5, 10)
        content()
        session['color']="green"

    elif session['building']=='house':
        session['gold']=random.randrange(2, 5)
        content()
        session['color']="green"
    elif session['building']=='casino':
        win_or_lost=random.randrange(0, 2)
        print "++++++++++++++++++++++++",win_or_lost
        if win_or_lost ==1:
            session['gold']=random.randrange(0, 50)
            content()
            session['color']="green"
        elif win_or_lost ==0:
            session['color']="red"
            red=session['color']
            data="Entered a {} and lost {} golds from ({})!".format(session['building'],str(session['gold']),session['timestamp']),red
            session['total']=session['total']-session['gold']
            session['output'].append((data))
            if session['total'] <=0:
                return redirect('/reset')


    return redirect('/display')

@app.route('/display')
def display_gold():
    #print "this line runs 5"
    return render_template('index.html')

@app.route('/reset')
def restart_game():
    session.clear()
    return redirect('/')





app.run(debug=True)