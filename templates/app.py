#import do frameword
#import do render_template para leitura do HTML
#request para catputura dos dados 
from flask import Flask, render_template, request
#biblioteca para criar conexão com mysql
import mysql.connector

app = Flask(__name__)

#cria conexão com o MYSQL
bd_config = {
    'host':'localhost',
    'user':'root',
    'password':'escola',
    'database':'CADASTRO1'
} 
#crição de rota de arquivo HTML principal
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastra', methods = ['POST'])