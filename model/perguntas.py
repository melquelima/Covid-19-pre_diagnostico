RESPOSTAS = [
    [],
    ["M","F"],
    ["Entre 0 e 39 anos","Entre 40 e 49 anos","Entre 50 e 59 anos","Entre 60 e 69 anos","Entre 70 e 79 anos","80 ou mais"],
    ["Sim","Não"],
    ["Febre","Tosse","Cansaço ou fadiga","Dor ou pressão no peito","Perda de fala ou de movimento","Dificuldade para respirar ou falta de ar","Coriza","Dor de garganta","Dor de cabeça"],
    ["Sim","Não"],
    ["Sim","Não","Não sei responder"],
    ["Sim","Não"]

]

PERGUNTAS = [
    "1. Qual seu nome?",
    "2. Qual seu sexo (M – Masculino ou F – Feminino)?",
    "3. Qual sua idade?",
    '''4. Possui qualquer uma das condições médicas pré-existentes abaixo?
    Doenças cardíacas, Doenças pulmonares, Câncer, Diabetes''',
    "5. Tem apresentado alguns dos sintomas abaixo? Se sim, liste aqueles apresentados.",
    "6. Teve contato direto com alguém confirmado com COVID-19 nos últimos 7 dias?",
    "7. Frequentou algum local nos últimos 7 dias com alguma incidência comprovada de COVID-19, ou ainda algum hospital com casos registrados da doença?",
    "8. Frequentou algum local com alto fluxo de pessoas nos últimos 7 dias (festas,ônibus/metrôs lotados, comércio ambulante, mercados lotados, entre outros)?",
    "===CONFIRA O RESULTADO ABAIXO===="
]

BASE_HTML_PERGUNTA = '''<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n
<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n
p, li {{ white-space: pre-wrap; }}\n
</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt;\">{}</span></p></body></html>'''


BASE_HTML_RESPOSTA = '''<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n
<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n
p, li {{ white-space: pre-wrap; }}\n
</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:6pt; font-weight:400; font-style:normal;\">\n
{}
</body></html>'''

ITEM = "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; color:{};\">{}</span></p>\n"


PREDIAGNOSTICOS = {
    "A":"Chance de estar com COVID-19: Muito Alta. Procure o mais rápido possível um posto de saúde para fazer um teste.",
    "B":"Chance de estar com COVID-19: Alta/Média. Caso seja possível, é recomendável que você realize um teste para COVID-19, ou que então permaneça em casa em quarentena por no mínimo 14 dias.",
    "C":"Chance de estar com CODIV-19: Moderada. Caso seja possível, permaneça em casa em quarentena apor alguns dias.",
    "D":"Chance de estar com CODIV-19: Baixa. Continue mantendo a atenção."
}



