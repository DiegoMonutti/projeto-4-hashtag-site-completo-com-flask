from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Página Inicial do Projeto"

@app.route("/contato")
def contato():
    return "Qualquer dúvida mande um e-mail para diego_monutti@outlook.com"

if __name__ == '__main__':
    app.run(debug=True)