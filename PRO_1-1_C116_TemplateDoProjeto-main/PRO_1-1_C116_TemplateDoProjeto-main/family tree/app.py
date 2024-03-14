# importando os módulos da biblioteca flask
from flask import Flask , render_template

# criando a instância da classe Flask, fornecendo a palavra-chave __name__ como argumento
app = Flask(__name__)

# escreva as rotas usando funções de decorador
# rota padrão ou 'URL'
@app.route("/")
def home():

    nome = "Samuel" # escreva seu nome
    idade = "14 anos" # escreva sua idade

    return render_template('index.html' , nome = nome , idade = idade)

# defina a rota para a página do pai
# rota padrão ou 'URL'
@app.route("/Pai")
def home():

    nome = "Leon" # escreva seu nome
    idade = "46 anos" # escreva sua idade

    return render_template('index.html' , nome = nome , idade = idade)

# defina a rota para a página da mãe
# rota padrão ou 'URL'
@app.route("/Ana Carolina")
def home():

    nome = "Ana Carolina" # escreva seu nome
    idade = "44 anos" # escreva sua idade

    return render_template('index.html' , nome = nome , idade = idade)

# defina a rota para a página do amigo
# rota padrão ou 'URL'
@app.route("/João Pedro")
def home():

    nome = "João Pedro" # escreva seu nome
    idade = "14 anos" # escreva sua idade

    return render_template('index.html' , nome = nome , idade = idade)

# adicione outras rotas, se você quiser




# execute o arquivo
if __name__  ==  '__main__':
    app.run(debug=True)
