# Importar o framework flash
from flask import Flask

#Criar a aplicação
app = Flask(__name__)

# define uma rota para o endereço principal "/"
@app.route("/")
def home():
    return "Bem-vindo a aula 06 de Python!"

#define uma rota extra chamada "/sobre"
@app.route("/sobre")
def sobre():
    return "Essa é a pagina Sobre"

#Roda o servidor local com debug ativado
if __name__ =="__main__":
    app.run(debug=True)