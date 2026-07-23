import flet as ft


# ===========================
# PALETA DE CORES
# ===========================

COR_FUNDO = "#F7FAFC"
COR_CARD = "#FFFFFF"
COR_PRIMARIA = "#4F6BED"
COR_TEXTO = "#1F2937"
COR_TEXTO_SECUNDARIO = "#64748B"


# ===========================
# CARD DE PERÍODO
# ===========================

def card_periodo(emoji, titulo, descricao, ao_clicar):

    return ft.Container(
        width=320,
        height=125,
        bgcolor=COR_CARD,
        border_radius=20,
        padding=20,
        ink=True,
        on_click=ao_clicar,

        shadow=ft.BoxShadow(
            blur_radius=10,
            color="#22000000",
            offset=ft.Offset(0, 4)
        ),

        content=ft.Row(
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=18,

            controls=[
                ft.Text(
                    emoji,
                    size=45
                ),

                ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=5,

                    controls=[
                        ft.Text(
                            titulo,
                            size=22,
                            weight=ft.FontWeight.BOLD,
                            color=COR_TEXTO
                        ),

                        ft.Text(
                            descricao,
                            size=15,
                            color=COR_TEXTO_SECUNDARIO,
                            width=210
                        )
                    ]
                )
            ]
        )
    )


# ===========================
# TELA ROTINA
# ===========================

def tela_rotina(page):

    return ft.View(
        route="/rotina",
        bgcolor=COR_FUNDO,
        padding=20,

        appbar=ft.AppBar(
            title=ft.Text(
                "Rotina",
                size=22,
                weight=ft.FontWeight.BOLD,
                color=COR_TEXTO
            ),

            leading=ft.IconButton(
                icon=ft.Icons.ARROW_BACK,
                tooltip="Voltar",
                on_click=lambda e: page.navigate("/")
            ),

            bgcolor=COR_CARD
        ),

        controls=[
            ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
                scroll=ft.ScrollMode.AUTO,
                expand=True,

                controls=[
                    ft.Container(height=10),

                    ft.Text(
                        "Minha rotina",
                        size=26,
                        weight=ft.FontWeight.BOLD,
                        color=COR_TEXTO
                    ),

                    ft.Text(
                        "Escolha um período do dia",
                        size=16,
                        color=COR_TEXTO_SECUNDARIO
                    ),

                    card_periodo(
                        "🌅",
                        "Manhã",
                        "Higiene, café, remédios e exercícios",
                        lambda e: page.navigate("/rotina/manha")
                    ),

                    card_periodo(
                        "☀️",
                        "Tarde",
                        "Atividades durante a tarde",
                        lambda e: print("Rotina da tarde")
                    ),

                    card_periodo(
                        "🌙",
                        "Noite",
                        "Atividades antes de dormir",
                        lambda e: print("Rotina da noite")
                    )
                ]
            )
        ]
    )