app.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/precommande', methods=['GET', 'POST'])
def precommande():
    if request.method == 'POST':
        produit = request.form['produit']
        quantite = request.form['quantite']
        return redirect(url_for('home'))
    return render_template('precommande.html')

if __name__ == '__main__':
    if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
