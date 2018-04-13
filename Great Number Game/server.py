from flask import Flask, render_template,redirect,request,session
import random
app=Flask(__name__)
app.secret_key="hellworld"

@app.route('/')
def root():
    print 'root is up'
    if "ran_n" not in session:
        session['ran_n']=random.randrange(0, 101)
    return render_template('index.html')
    
@app.route('/store',methods=['post'])
def store_info():
    print "the random number is----",session['ran_n']
    session['guessN']=request.form['input']
    try:
        if int(session['guessN']) ==session['ran_n']:
            session['guessN']='You got it!'
            
        elif int(session['guessN']) <session['ran_n']:
            session['guessN']='Too Low!'
            print session['guessN']
        elif int(session['guessN']) >session['ran_n']:
            session['guessN']='Too High!'
            print session['guessN']
    except:
        session['guessN']="please enter a numbric!"
        print session['guessN']
    return redirect('/show')

@app.route('/show')
def display_data():
    return render_template('index.html',name=session['guessN'],show_n=session['ran_n'])

@app.route('/reset',methods=['post'])
def restart_game():
    session.clear()
    return redirect('/')

app.run(debug=True)