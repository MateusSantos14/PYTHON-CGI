import cgitb, cgi
from scriptspython import MonetarioCalculadora

def retornarResultado(valor,atual,nova):
    resultado = calculadora.calcular(valor, atual, nova)
    if resultado=="select invalido":
        print("<p id='resposta'>Select inválido</p>")
    elif resultado=="Valor invalido":
        print("<p id='resposta'>Valor inválido</p>")
    else:
        print(f"<p id='resposta'>O valor <b>{valor}</b> na unidade <b>{atual}</b> equivale a "  
                f"<b>{resultado}</b> na unidade <b>{nova}</b></p> ")


cgitb.enable(display=0, logdir="./")
form = cgi.FieldStorage()
valor = form.getvalue('valor')
atual = form.getvalue('atual')
nova = form.getvalue('nova')
calculadora = MonetarioCalculadora()
print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<link rel='stylesheet' href='../style.css'>")
print("</head>")
print("<body>")
print("<h1>Resultado cálculo conversão monetária</h1><br>")
print("<a href='../monetario.html'><-Retornar para página do conversão</a><br>")
retornarResultado(valor,atual,nova)
print("</body>")
print("</html>")