import requests

class Api:


    def __init__(self):
        self.ApiUrl = "http://127.0.0.1:8000"
        

    def listar(self):

        try:
            response = requests.get(f"{self.ApiUrl}/livros/")
            response.raise_for_status()
            livros = response.json()
            return livros

        except requests.exceptions.RequestException as e:
            print(f"Erro ao listar livros: {e}")
            return 


    def criar():
        print("Criar livro")
        pass

    def excluir():
        pass

    def filtrar():
        pass

    def editar():
        pass