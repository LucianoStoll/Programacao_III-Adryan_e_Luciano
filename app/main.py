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

        self.titulo = ft.Text(
            "Biblioteca",
            size= 20,
            weight=ft.FontWeight.BOLD,

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
        return ft.Container(
            expand=True,
            padding=30,
            content=ft.Column(
                controls=[
                    self.titulo,
                    ft.FloatingActionButton(icon=ft.Icons.ADD, content="Adicionar Livro", on_click=Api.criar),
                ],
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


     


    

    

    
