import csv
from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/sobre-equipe')
def sobreEquipe():
    return render_template('sobre-equipe.html')


@app.route('/glossario')
def glossario():
    
    glossarioDeTermos = []

    with open('bd_glossario.csv', 'r', newline='', encoding='utf-8') as arquivo:
        reader = csv.reader(arquivo, delimiter=';')
        for linha in reader:
            glossarioDeTermos.append(linha)

    return render_template('glossario.html', glossario=glossarioDeTermos)


@app.route('/novo-termo')
def novoTermo():
    return render_template('novo-termo.html')


@app.route('/criarTermo', methods=['POST'])
def criarTermo():

    termo = request.form['termo']
    definicao = request.form['definicao']

    with open('bd_glossario.csv', 'a', newline='', encoding='utf-8') as arquivo:
        writer = csv.writer(arquivo, delimiter=';')
        writer.writerow([termo, definicao])

    return redirect(url_for('glossario')) 


app.run(debug=True)