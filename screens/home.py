import flet as ft

# ===========================
# PALETA DE CORES
# ===========================

# Fundo
GRADIENTE_FUNDO = [
    "#FFF9F2",
    "#FAF2E8",
    "#F6ECE2",
    "#F2E5D8",
    "#EEE0D1",
]

# Cards
COR_CARD = "#FFFCF8"

# Botões
COR_PRIMARIA = "#6F8FAF"

# Confirmar
COR_VERDE = "#7A9D7E"

# Destaques
COR_TERRACOTA = "#C97B63"

# Texto
COR_TEXTO = "#4A4A4A"

# SOS
COR_SOS = "#C65D5D"



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
        route="/",

        controls=[
            ft.Container(
                expand=True,

                gradient=ft.LinearGradient(
                    begin=ft.Alignment.TOP_CENTER,      #topo
                    end=ft.Alignment.BOTTOM_CENTER,     #base
                    colors=GRADIENTE_FUNDO,
                ),

                content=ft.Column(
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
                                weight=ft.FontWeight.BOLD,
                            ),
                        ),

                        card(
                            "Comunicação",
                            ft.Icons.RECORD_VOICE_OVER,
                            lambda e: page.navigate("/comunicacao"),
                        ),

                        card(
                            "Rotina",
                            ft.Icons.CHECKLIST,
                            lambda e: page.navigate("/rotina"),
                        ),

                        card(
                            "Família / Cuidador",
                            ft.Icons.PEOPLE,
                            lambda e: page.navigate("/familiares"),
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
                                color="white",
                            ),
                        ),
                    ],
                ),
            ),
        ],
    )