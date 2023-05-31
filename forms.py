from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class FormCriarConta(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired(message='Digite um nome de usuário válido')])
    email_criarconta = StringField('E-mail', validators=[DataRequired(), Email(message='Digite um endereço de e-mail válido')])
    senha_criarconta = PasswordField('Senha', validators=[DataRequired(), Length(6,20, message='Digite uma senha com 6 à 20 caracteres')])
    confirmacao_senha = PasswordField('Confirmação da Senha', validators=[DataRequired(message='Senha não corresponde com a anterior'), EqualTo('senha_criarconta')])
    botao_submit_criarconta = SubmitField('Criar Conta')

class FormLogin(FlaskForm):
    email_login = StringField('E-mail', validators=[DataRequired(), Email(message='Digite um endereço de e-mail válido')])
    senha_login = PasswordField('Senha', validators=[DataRequired(), Length(6,20, message='Digite sua senha corretamente')])
    lembrar_dados = BooleanField('Lembrar Dados de Acesso')
    botao_submit_login = SubmitField('Fazer Login')
    