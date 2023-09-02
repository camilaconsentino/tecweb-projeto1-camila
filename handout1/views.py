from utils import load_data, load_template, build_response
from urllib.parse import unquote_plus
from database import *
from exemplo_de_uso import db

def index(request):
    # A string de request sempre começa com o tipo da requisição (ex: GET, POST)
    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[1]
        params = {}
        # Preencha o dicionário params com as informações do corpo da requisição
        # O dicionário conterá dois valores, o título e a descrição.
        # Posteriormente pode ser interessante criar uma função que recebe a
        # requisição e devolve os parâmetros para desacoplar esta lógica.
        # Dica: use o método split da string e a função unquote_plus
        for chave_valor in corpo.split('&'):
            chave, valor = chave_valor.split('=')
            valor = unquote_plus(valor, encoding='utf-8')
            params[chave] = valor

        #coloca a nova note no banco de dados
        db = Database("banco")
        db.add(Note(title=params["titulo"], content=params["detalhes"]))

        return build_response(code=303, reason="See Other", headers='Location: /')

    # Cria uma lista de <li>'s para cada anotação
    # Se tiver curiosidade: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=dados.title, details=dados.content,id=dados.id)
        for dados in load_data()
    ]
    notes = '\n'.join(notes_li)

    body = load_template('index.html').format(notes=notes)

    return build_response(body)

def delete(request, id):
    db.delete(id)
    return build_response(code=303, reason='See Other', headers='Location: /')

'''
def edit(request, id):
    request = request.replace('\r', '')
    partes = request.split('\n\n')
    corpo = partes[1]
    title = unquote_plus(corpo.split('&')[1].split('=')[1]).replace('+', ' ')
    content = unquote_plus(corpo.split('&')[2].split('=')[1]).replace('+', ' ')
    db.update(Note(id=id, title=title, content=content))
    return build_response(code=303, reason='See Other', headers='Location: /')
'''