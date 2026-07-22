import flet as ft

# ===========================
# PALETA DE CORES
# ===========================

COR_FUNDO = "#F7FAFC"
COR_CARD = "#FFFFFF"
COR_PRIMARIA = "#4F6BED"
COR_TEXTO = "#1F2937"
COR_SOS = "#E53935"


# ===========================
# CARD
# ===========================

def card(titulo, icone, ao_clicar):

    return ft.Container(
        width=320,
        height=95,
        bgcolor=COR_CARD,
        border_radius=20,
        padding=20,
        on_click=ao_clicar,
        ink=True,

        shadow=ft.BoxShadow(
            blur_radius=10,
            color="#22000000",
            offset=ft.Offset(0, 4)
        ),

        content=ft.Row(
            vertical_alignment=ft.CrossAxisAlignment.CENTER,

            controls=[
                ft.Icon(
                    icone,
                    size=40,
                    color=COR_PRIMARIA
                ),

                ft.Text(
                    titulo,
                    size=22,
                    weight=ft.FontWeight.BOLD,
                    color=COR_TEXTO
                )
            ]
        )
    )


# ===========================
# HOME
# ===========================

def tela_home(page):

    return ft.View(
        route="/comunicacao",
        bgcolor=COR_FUNDO,

        controls=[
            ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=25,
                expand=True,

                controls=[
                    ft.Container(
                        height=40
                    ),

                    ft.Container(
                        width=150,
                        height=150,
                        bgcolor=COR_PRIMARIA,
                        border_radius=65,
                        alignment=ft.Alignment.CENTER,

                        content=ft.Text(
                            "Ajudante",
                            color="white",
                            size=22,
                            weight=ft.FontWeight.BOLD
                        )
                    ),

                    card(
                        "Comunicação",
                        ft.Icons.RECORD_VOICE_OVER,
                        lambda e: page.navigate("/comunicacao")
                    ),

                    card(
                        "Rotina",
                        ft.Icons.CHECKLIST,
                        lambda e: print("Rotina")
                    ),

                    card(
                        "Família / Cuidador",
                        ft.Icons.PEOPLE,
                        lambda e: print("Família / Cuidador")
                    ),

                    ft.Container(
                        width=320,
                        height=80,
                        bgcolor=COR_SOS,
                        border_radius=20,
                        alignment=ft.Alignment.CENTER,

                        content=ft.Text(
                            "SOS",
                            size=30,
                            weight=ft.FontWeight.BOLD,
                            color="white"
                        )
                    )
                ]
            )
        ]
    )