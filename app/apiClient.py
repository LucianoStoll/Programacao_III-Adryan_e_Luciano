import requests

class Api:


    def __init__(self):
        self.ApiUrl = "http://127.0.0.1:8000"
        

    def listar(self):
        Livros = requests.get(f"{self.ApiUrl}/livros/")
        return Livros.json()
        

    def criar():
        print("Criar livro")
        pass

    def excluir():
        pass

    def filtrar():
        pass

    def editar():
        pass