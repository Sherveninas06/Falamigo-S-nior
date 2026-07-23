import flet as ft

COR_FUNDO = "#F7FAFC"
COR_CARD = "#FFFFFF"
COR_PRIMARIA = "#4F6BED"
COR_TEXTO = "#1F2937"


def card_periodo(emoji, titulo, descricao, ao_clicar):

    return ft.Container(
        width=320,
        height=130,
        bgcolor=COR_CARD,
        border_radius=20,
        padding=20,
        ink=True,
        on_click=ao_clicar,

        shadow=ft.BoxShadow(
            blur_radius=8,
            color="#22000000",
            offset=ft.Offset(0,3)
        ),

        content=ft.Row(
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=18,

            controls=[
                ft.Text(
                    emoji,
                    size=48
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
                            color="#64748B"
                        )
                    ]
                )
            ]
        )
    )

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

                controls=[
                    ft.Text(
                        "Minha Rotina",
                        size=26,
                        weight=ft.FontWeight.BOLD,
                        color=COR_TEXTO
                    ),

                    ft.Text(
                        "Escolha um período do dia",
                        size=16,
                        color="#64748B"
                    ),

                    card_periodo(
                        "🌅",
                        "Manhã",
                        "Atividades para começar o dia",
                        lambda e: page.navigate("/rotina/manha")
                    ),

                    card_periodo(
                        "☀️",
                        "Tarde",
                        "Atividaes durante a tarde",
                        lambda e: page.navigate("/rotina/tarde")
                    ),

                    card_periodo(
                        "🌙",
                        "Noite",
                        "Atividade antes de dormir",
                        lambda e: page.navigate("/rotina/noite")
                    )
                ]
            )
        ]
    )