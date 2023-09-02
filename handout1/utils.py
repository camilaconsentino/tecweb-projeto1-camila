import json
from database import *
from exemplo_de_uso import db

def extract_route(request):
    return request.split()[1][1:]
    linhas = request.split("\n")
    primeira_linha = linhas[0]
    primeira_linha = primeira_linha.split(" ")
    response = primeira_linha[1]
    return response[1:]

'''
request = "GET /img/logo-getit.png HTTP/1.1\nHost: 0.0.0.0:8080\nConnection: keep-alive\nUser-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36\nAccept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8\nReferer: http://0.0.0.0:8080/\nAccept-Encoding: gzip, deflate\nAccept-Language: en-US,en;q=0.9,pt;q=0.8"

response = extract_route(request)
print(response)

'''

def read_file(path):
    with open(path, "rb") as file:
        conteudo = file.read()
    return conteudo
    
def load_data():
    db = Database('banco')
    notes = db.get_all()
    return notes
    
def load_template(arq):
    path = "templates/{name}".format(name=arq)
    with open(path, 'r') as file:
        conteudo = file.read()
    return conteudo

def build_response(body='', code=200, reason='OK', headers=''):
    if headers=='':
        string = "HTTP/1.1 {code} {reason}\n\n{body}".format(code=code, reason=reason, body=body)
    else:
        string = "HTTP/1.1 {code} {reason}\n{headers}\n\n{body}".format(code=code, reason=reason, headers=headers, body=body) 
    return string.encode()
