#import do frameword
#import do render_template para leitura do HTML
#request para catputura dos dados 
from flask import Flask, render_template, request
#biblioteca para criar conexão com mysql
import mysql.connector



#cria conexão com o MYSQL
bd_config = {
    'host':'localhost',
    'user':'root',
    'password':'escola',
    'database':'CADASTRO1'
}