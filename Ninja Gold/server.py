from flask import Flask, render_template, redirect,request,session
import random
app=Flask(__name__)
app.secret_key="hithere"


@app.route('/')
def root():
    if "total" not in session:
        session['total']=0
    if "output" not in session:
        session['output']=[]
    # session.clear()
    return render_template('index.html')

@app.route('/process_money',methods=['POST'])
def process_money():
    if request.form['building']=='farm':
        session['gold']=random.randrange(10, 20)
        data={
            "gold": session['gold'],
            "from":request.form['building']
        }
        session['output'].append(data)
        session['total']=session['total']+session['gold']
       
        print "current total is farm",session['total']
    elif request.form['building']=='cave':
        session['gold']=random.randrange(5, 10)
        session['total']=session['total']+session['gold']
        print "current total is cave",session['total']
    elif request.form['building']=='house':
        pass
    elif request.form['building']=='casino':
        pass
    print " total is++++++",session['total']
    return redirect('/display')

@app.route('/display')
def display_gold():
    #print "this line runs 5"
    return render_template('index.html',output=session['output'],total=session['total'])







app.run(debug=True)