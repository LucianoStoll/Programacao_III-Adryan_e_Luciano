import flet as ft
from apiClient import Api

FUNDO = "#192C30"
MENU = "#243F46"
CARD = "#253F46"
DESTAQUE = "#FED36A"
TEXTO = "#CDECEF"
TEXTO_SECUNDARIO = "#A9C1C3"

class Biblioteca:
    
    def __init__(self):

        self.api = Api()

        self.listar_livros = ft.ListView()

        self.titulo = ft.Text(
            "Biblioteca",
            size= 20,
            weight=ft.FontWeight.BOLD,
        )

    def Listar_Livros(self):
        Livros = self.api.listar()
        
        if not Livros:
            return

        self.listar_livros.controls.clear()

        for livro in Livros["Livros"]:
            self.listar_livros.controls.append(
                ft.Text(
                    f'Titulo: {livro["titulo"]}\n'
                    f'Autor: {livro["autor"]}\n'
                    f'Ano: {livro["ano"]}\n'
                )
            )
        
    
    def criar_aba_lateral(self):
        return ft.Container(
            width=100,
            bgcolor=MENU,
            border_radius=10,
            padding=5,
            content=ft.Column(
                controls=[
                    ft.Icon(
                        ft.Icons.LOCAL_LIBRARY,
                        size=45,
                        color=TEXTO,
                    ),
                    ft.Button(content="Home"),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )

    def criar_principal(self):
        self.Listar_Livros()

        return ft.Container(
            expand=True,
            padding=30,
            content=ft.Column(
                controls=[
                    self.titulo,
                    self.listar_livros,
                    #ft.FloatingActionButton(icon=ft.Icons.ADD, content="Adicionar Livro", on_click=Api.criar),
                ],
                expand=True,
            ),
        )

    def add_tela(self):
        return ft.Row(
            controls=[
                self.criar_aba_lateral(),
                self.criar_principal(),
            ],
            expand=True,
            spacing=0,
        )

    
def main(page: ft.Page):
    page.title = "Biblioteca"
    page.bgcolor = FUNDO
    page.padding = 0
    page.add(Biblioteca().add_tela())

ft.run(main)


     


    

    

    
