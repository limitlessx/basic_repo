from flask import Flask, render_template, redirect,request,session
import random
import time
from datetime import datetime


app=Flask(__name__)
app.secret_key="hithere"

def content(random_n):
  session['gold']=random_n
  data ={
      "msg":"Earned {} golds from {} ! ({})".format(str(session['gold']),session['building'],session['timestamp']),
      "color":"green"
  }
  session['total']=session['total']+session['gold']
#   if data not in session['output']:
#       session['output'].insert(0,data)
  session['output'].append(data)
  
      
@app.route('/')
def root():
    
    if "total" not in session:
        session['total']=0
        session['output']=[]
    return render_template('index.html')

@app.route('/process_money',methods=['POST'])
def process_money():
    session['timestamp'] = datetime.now().strftime('%Y/%m/%d %I:%M %p') 
    session['building']=request.form['building']
       
    if session['building']=='farm':
        content(random.randrange(10, 20))
        
    elif session['building']=='cave':
        content(random.randrange(5, 10))
        
    elif session['building']=='house':
        content(random.randrange(2, 5))
        
    elif session['building']=='casino':
        win_or_lost=random.randrange(0, 2)
        print "++++++++++++++++++++++++",win_or_lost
        if win_or_lost ==1:
            content(random.randrange(0, 50))
        elif win_or_lost ==0:
            data={
                "msg":"Entered a {} and lost {} golds! from ({})".format(session['building'],str(session['gold']),session['timestamp']),
                "color":"red"
            }
            session['total']=session['total']-session['gold']
            # if data not in session['output']:
            #      session['output'].insert(0,data)
            session['output'].append((data))
            # if session['total'] <=0:
            #     return redirect('/reset')
    return redirect('/')

@app.route('/reset')
def restart_game():
    session.clear()
    return redirect('/')

app.run(debug=True)