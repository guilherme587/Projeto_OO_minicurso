from pyexpat import model
import tkinter as tk
from view import View, V1, V2, V3, V4
from model import Model
from controler import Controler

def main():
    #cria control
    control = Controler()

    #cria view
    view = View(control.tela, 'autogui_GUI')

    #cria model
    model = Model()

   #loop da view, inicializa model e view em control
    control.inicializa(view, model)
    control.executar()
    

if __name__ == '__main__':
    main()

'''
quero um gui para o autogui
quero pesquisar coisas
quero saber a posição do mouse na tela para configurar cliques
quero configurar exulções
'''