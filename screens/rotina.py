import flet as ft


# ===========================
# NOVA PALETA
# ===========================

COR_FUNDO = "#F5F2EE"
COR_CARD = "#FFFFFF"
COR_ROSA = "#B98FA3"
COR_VERDE = "#8FAE9A"
COR_BEGE = "#E8C28F"
COR_TEXTO = "#333333"
COR_TEXTO_SECUNDARIO = "#6B625F"
COR_BRANCO = "#FFFFFF"


# ===========================
# CARD DE PERÍODO
# ===========================

def card_periodo(
    emoji,
    titulo,
    descricao,
    cor_icone,
    cor_fundo_icone,
    ao_clicar
):

    return ft.Container(
        width=365,
        height=125,
        bgcolor=COR_CARD,
        border_radius=22,
        padding=18,
        ink=True,
        on_click=ao_clicar,

        shadow=ft.BoxShadow(
            blur_radius=10,
            color="#18000000",
            offset=ft.Offset(0, 4)
        ),

        content=ft.Row(
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=18,

            controls=[
                ft.Container(
                    width=72,
                    height=72,
                    bgcolor=cor_fundo_icone,
                    border_radius=36,
                    alignment=ft.Alignment.CENTER,

                    content=ft.Text(
                        emoji,
                        size=38
                    )
                ),

                ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=6,
                    expand=True,

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
                            max_lines=2
                        )
                    ]
                ),

                ft.Icon(
                    ft.Icons.CHEVRON_RIGHT,
                    size=28,
                    color=cor_icone
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
                color=COR_BRANCO
            ),

            leading=ft.IconButton(
                icon=ft.Icons.ARROW_BACK,
                icon_color=COR_BRANCO,
                tooltip="Voltar",
                on_click=lambda e: page.navigate("/")
            ),

            bgcolor=COR_VERDE
        ),

        controls=[
            ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=18,
                expand=True,
                scroll=ft.ScrollMode.AUTO,

                controls=[
                    ft.Container(height=5),

                    ft.Container(
                        width=100,
                        height=100,
                        bgcolor="#EAF3EC",
                        border_radius=50,
                        alignment=ft.Alignment.CENTER,

                        content=ft.Icon(
                            ft.Icons.CALENDAR_MONTH,
                            size=55,
                            color=COR_VERDE
                        )
                    ),

                    ft.Text(
                        "Minha rotina",
                        size=28,
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
                        COR_BEGE,
                        "#FAEEDC",
                        lambda e: page.navigate("/rotina/manha")
                    ),

                    card_periodo(
                        "☀️",
                        "Tarde",
                        "Almoço, descanso e atividades",
                        COR_VERDE,
                        "#EAF3EC",
                        lambda e: page.navigate("/rotina/tarde")
                    ),

                    card_periodo(
                        "🌙",
                        "Noite",
                        "Jantar, higiene e preparação para dormir",
                        COR_ROSA,
                        "#F4E7EC",
                        lambda e: page.navigate("/rotina/noite")
                    ),

                    ft.Container(height=30)
                ]
            )
        ]
    )