# importa classes principais para criar interface
from PyQt5.QtWidgets import QApplication, QLabel, QWidget


#Criar o aplicativo
app = QApplication([])

#Criar a janela
janela = QWidget()
janela.setWindowTitle("Minha Primeira Janela")

#Criar o texto dentro da janela
rotulo = QLabel("Olá, mundo!", parent=janela)

janela.resize(300,200)

janela.show()

app.exec()
























