import flet as ft
from apiClient import Api

class Biblioteca:

    
    def __init__(self):

        self.titulo = ft.Text(
            "Biblioteca",
            size= 20,
            weight=ft.FontWeight.BOLD,

        )

    def add_tela(self):

        ContAba = ft.Column(
            alignment=ft.MainAxisAlignment.START,
            controls=[
                ft.Text("Biblioteca", size=24),
                
            ]

        )

        AbaLateral = ft.Stack(
            controls=[
                ft.Container(
                    left=-10,
                    top=-10,
                    width=200,
                    height=999,
                    content=ft.Container(
                                    width=200,
                                    height=999,
                                    padding=5,
                                    bgcolor=ft.Colors.GREY,
                                    content=ft.Column(
                                        controls=[
                                            ContAba,
                                        ]
                                    )
                                )
                ),
            ],
        )
  
            
            
            
        
        

        return AbaLateral

    
def main(page: ft.Page):
    page.title = "Biblioteca"
    page.add(Biblioteca().add_tela())

ft.run(main)


    


    

    

    

