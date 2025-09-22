from pymongo import MongoClient
from google_books import buscar_livros

client = MongoClient("mongodb://localhost:27017/")
db = client["libris"]
colecao = db["livros"]

def buscaresalvar(query):
    dados = buscar_livros(query)
    for item in dados.get("items", []):
        livro = {
            "titulo": item["volumeInfo"].get("title"),
            "autor": item["volumeInfo"].get("authors", ["Desconhecido"]),
            "sinopse": item["volumeInfo"].get("description", ""),
            "genero": item["volumeInfo"].get("categories", []),
            "avaliacao": item["volumeInfo"].get("averageRating", 0)
        }
        colecao.insert_one(livro)

buscaresalvar("ficção científica")