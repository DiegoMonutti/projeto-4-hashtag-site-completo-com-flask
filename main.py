from flask import Flask, render_template, url_for, request, flash, redirect
from forms import FormLogin, FormCriarConta

app = Flask(__name__)

lista_usuarios = ["Diego", "Ciclano", "Fulano", "Beltrano", "Manolo"]

app.config['SECRET_KEY'] = 'db457e5d385c1b7a1405355c6adc0866'

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/usuarios")
def usuarios():
    return render_template("usuarios.html", lista_usuarios=lista_usuarios)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    form_criarconta = FormCriarConta()

    if form_login.validate_on_submit() and 'botao_submit_login' in request.form:
        flash(f'Login feito com sucesso no e-mail: {form_login.email_login.data}', 'alert-success')
        return redirect(url_for('home'))

    if form_criarconta.validate_on_submit() and 'botao_submit_criarconta' in request.form:
        flash(f'Conta criada com sucesso no e-mail: {form_criarconta.email_criarconta.data}', 'alert-success')
        return redirect(url_for('home'))
    
    return render_template("login.html", form_login=form_login, form_criarconta=form_criarconta)

if __name__ == '__main__':
    app.run(debug=True)
