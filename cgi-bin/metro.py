import cgitb, cgi
from scriptspython import MetroCalculo, enc_print


def retornarResultado(valor,atual,nova):
    resultado = calculadora.calcular(valor, atual, nova)
    if resultado=="select invalido":
        enc_print("<p id='resposta'>Select inválido</p>")
    elif resultado=="valor invalido":
        enc_print("<p id='resposta'>valor inválido</p>")
    else:
        print(f"<p id='resposta'>O valor <b>{valor}</b> na unidade <b>{atual}</b> equivale a "  
                f"<b>{resultado}</b> na unidade <b>{nova}</b></p> ")


cgitb.enable(display=0, logdir="./")
form = cgi.FieldStorage()
valor = form.getvalue('valor')
atual = form.getvalue('atual')
nova = form.getvalue('nova')
calculadora = MetroCalculo()
print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print('<meta charset="utf-8">')
print("</head>")
print("<body>")
enc_print("<h1>Resultado cálculo conversão de metragem</h1><br>")
enc_print("<a href='../metro.html'><-Retornar para página do conversão</a><br>")
retornarResultado(valor,atual,nova)
print("</body>")
print("</html>")