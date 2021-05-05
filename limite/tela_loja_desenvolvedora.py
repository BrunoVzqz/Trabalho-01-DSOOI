from limite.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg


class TelaLojaDesenvolvedora(TelaAbstrata):

    def __init__(self):
        self.__window = None

    def open(self, lista_desenvolvedoras): # -> 'mostra_menu'
        self.tela_opcoes(lista_desenvolvedoras)
        button_key, values = self.__window.Read()
        if button_key is None:
            button_key = 0
        return button_key, values

    def tela_opcoes(self, lista_desenvolvedoras):
        sg.theme('Reddit')
        layout = [[sg.Text(" Desenvolvedoras Disponiveis: " + " ,".join(lista_desenvolvedoras))],
                  [sg.Text('Por favor selecione uma desenvolvedora', font=('Helvetica', 10))],
                  [sg.Combo(values=lista_desenvolvedoras, size=(17, 1))],
                  [sg.Submit(font=('Helvetica', 10)), sg.Cancel(font=('Helvetica', 10))]]
        self.__window = sg.Window("Desenvolvedoras", element_justification='center',
                                  finalize=True).Layout(layout)

    def close(self):
        self.__window.Close()