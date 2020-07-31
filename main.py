


import sys
from model.window import Ui_MainWindow
from PyQt5 import QtWidgets
from model.perguntas import *

class MyWin(QtWidgets.QMainWindow):
        def __init__(self,parent=None):
            QtWidgets.QWidget.__init__(self,parent)
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            self.labels = ["l_nome","l_sexo","l_idade","l_r4",None,"l_r6","l_r7","l_r8","l_pre","l_gr"]
            self.comboboxes = ["cb1","cb2","cb3","cb4","cb5","cb6","cb7","cb8","cb9"]
            self.radioButtons = ["rb1","rb2","rb3","rb4","rb5","rb6","rb7","rb8","rb9"]

            self.ui.next.clicked.connect(self.next)

            self.ocultaCheckButtons()
            self.ocultaRadioButtons()
            self.resetResults()

            self.perguntaAtual = 0

            self.renderPergunta()
            self.ui.hiddenchk.setHidden(True)

            self.resultados = []
            self.diagnosticos = {   "Entre 0 e 39 anos" :{"F":{"value":"Baixo","color":"#07ff37"},"M":{"value":"Baixo","color":"#07ff37"}},
                                    "Entre 40 e 49 anos":{"F":{"value":"Baixo-Médio","color":"#bcff07"},"M":{"value":"Baixo-Médio","color":"#bcff07"}},
                                    "Entre 50 e 59 anos":{"F":{"value":"Médio","color":"#fffe07"},"M":{"value":"Médio","color":"#fffe07"}},
                                    "Entre 60 e 69 anos":{"F":{"value":"Médio-Alto","color":"#ffc507"},"M":{"value":"Alto","color":"#ff9707"}},
                                    "Entre 70 e 79 anos":{"F":{"value":"Alto","color":"#ff9707"},"M":{"value":"Alto-Muito Alto","color":"#ff5e07"}},
                                    "80 ou mais"        :{"F":{"value":"Muito Alto","color":"#ff0745"},"M":{"value":"Muito Alto","color":"#ff0745"}},
                                }
                

        def resetResults(self): # limpa todas as variaveis na tela
            for x in self.labels:
                if not x is None:
                    self.setTextLabel(x,"--")
            self.ui.textBrowser_2.setHtml("")
            self.ui.next.setText("Próxima")
            self.ui.inputText.setText("")

        def setTextLabel(self,lbl,text,color="#a5a8ab",bgcolor="transparent"): # coloca um texto em um label
            label = getattr(self.ui,lbl)
            label.setStyleSheet(f"QLabel{{color:{color};background-color:{bgcolor}}}")
            label.setText(text)
        
        def renderPergunta(self):
            getres = lambda y:[x for x in self.resultados if y in x][0][y]
            thereisop = lambda y:bool([x for x in self.resultados if y in x])

            self.ui.tb_pergunta.setHtml(BASE_HTML_PERGUNTA.format(PERGUNTAS[self.perguntaAtual]))
        
            if self.perguntaAtual != 8:
                if self.perguntaAtual == 0:
                    self.ui.inputText.setHidden(False)
                else:
                    tp = "check" if self.perguntaAtual == 4 else "radio"
                    self.mostra_opcoes(RESPOSTAS[self.perguntaAtual],tp)
            else:
                self.mostra_opcoes([])
                self.mostra_pre_diagnostico("A" if thereisop("5") and  "Sim" in getres("5") else None)
    
        def mostra_opcoes(self,opcoes,tp="radio"):
            self.ocultaRadioButtons()
            self.ocultaCheckButtons()
            itens = self.radioButtons if tp =="radio" else self.comboboxes
            for x,y in zip(opcoes,itens):
                obj = getattr(self.ui,y)
                obj.setText(x)
                obj.setHidden(False)

        def mostra_resposta(self):
            response = self.getSelectedOption()

            if 0 < self.perguntaAtual < 8 and not self.labels[self.perguntaAtual] is None:
                self.resultados.append({str(self.perguntaAtual):response})
                resp = "-".join(response)
                self.setTextLabel(self.labels[self.perguntaAtual],resp,("red" if "Sim" in resp else ("orange" if "responder" in resp else "lime"))) 
            if self.perguntaAtual == 0:
                self.setTextLabel("l_nome",self.ui.inputText.text(),"lime")
            if self.perguntaAtual == 4:
                self.resultados.append({str(self.perguntaAtual):response})
                html = [ITEM.format("#ffaa00" if x in RESPOSTAS[4][0:3] else( "#ff0000" if x in RESPOSTAS[4][3:6] else "#ffff00"),x) for x in response]
                self.ui.textBrowser_2.setHtml(BASE_HTML_RESPOSTA.format("\n".join(html)))

                #prediagnostico
                self.prediagnostico = sum(list(set([12 if x in RESPOSTAS[4][0:3] else(20 if x in RESPOSTAS[4][3:6] else 6) for x in response])))
                self.setTextLabel("l_pre",str(self.prediagnostico))

        def mostra_pre_diagnostico(self,letra = None):
            getres = lambda y:[x for x in self.resultados if y in x][0][y]

            if letra == None:
                p5 = self.prediagnostico
                p7 = 6 if getres("6") == ["Sim"] else (0 if getres("6") == ["Não"] else 3)
                p8 = 6 if getres("7") == ["Sim"] else 0
                result = (p5+ p7+p8)/50
                letra = "A" if 0.7 <= result <= 1 else ("B" if 0.5 <= result < 0.7 else ("C" if 0.3 <= result < 0.5 else "D"))


            self.ui.tb_pergunta.setHtml(BASE_HTML_PERGUNTA.format(f"===CONFIRA O RESULTADO ABAIXO====<br/>{PREDIAGNOSTICOS[letra]}"))

            idade = getres("2")[0]
            sexo = getres("1")[0]

            self.setTextLabel("l_gr",self.diagnosticos[idade][sexo]["value"],"black",self.diagnosticos[idade][sexo]["color"])

        def next(self):
            getres = lambda y:[x for x in self.resultados if y in x][0][y]

            if self.getSelectedOption() != [] or (self.ui.inputText.text() != "" and self.perguntaAtual == 0) or self.perguntaAtual in [4,8]:
                self.mostra_resposta()

                if self.perguntaAtual == 8:
                    self.perguntaAtual = 0
                    self.resetResults()
                    self.resultados = []
                else:
                    if self.perguntaAtual == 4  and len(getres("4")) >= 3:
                        self.perguntaAtual = 6
                    elif self.perguntaAtual == 5 and "Sim" in getres("5"):
                        self.perguntaAtual = 8
                    else:
                        self.perguntaAtual = self.perguntaAtual + 1
                    

                if self.perguntaAtual == 8:
                    self.ui.next.setText("Finalizar")


                self.renderPergunta()

        def getSelectedOption(self):
            itens = self.comboboxes + self.radioButtons
            resposta = []
            for x in itens:
                obj = getattr(self.ui,x)
                if obj.isChecked():
                    resposta.append(obj.text())
            return resposta

        def ocultaRadioButtons(self):
            for x in self.radioButtons:
                obj = getattr(self.ui,x)
                obj.setHidden(True)
                obj.setChecked(False)
            self.ui.inputText.setHidden(True)
        
        def ocultaCheckButtons(self):
            for x in self.comboboxes:
                obj = getattr(self.ui,x)
                obj.setHidden(True)
                obj.setChecked(False)
            
            self.ui.hiddenchk.setChecked(True)
            self.ui.inputText.setHidden(True)
                      


#radioButton.isChecked():

if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        myapp = MyWin()
        myapp.show()
        sys.exit(app.exec_())