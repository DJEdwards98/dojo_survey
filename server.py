
from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key = 'asdfghjkklqwertyuizxcvbn'
@app.route('/')
def index():
    return render_template('index.html')

@app.post('/users')
def enter_users():
    session['username'] = request.form['username']
    # session['location'] = request.form['location']
    # session['languages'] = request.form['languages']
    # session['comment'] = request.form['comment']
    return redirect('/info')

@app.route('/info')
def info():
    return render_template('/info.html')

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5001)