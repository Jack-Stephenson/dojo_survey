from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'oh no, my secret key, its broken!'

@app.route('/')
def form():
    return render_template('index.html')

@app.route('/process', methods=['post'])
def process():
    session['name'] = request.form['yourName']
    session['yourLocation'] = request.form['dojoLocation']
    session['favoriteLanguage'] = request.form['favoriteLanguage']
    session['comments'] = request.form['comments']
    session.permanent=True
    return redirect('/result')

@app.route('/result')
def show_user():
    return render_template('show.html', name=session['name'], yourLocation=session['yourLocation'], favoriteLanguage=session['favoriteLanguage'], comments=session['comments'])

if __name__ == "__main__":
    app.run(debug=True)