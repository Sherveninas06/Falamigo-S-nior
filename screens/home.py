import flet as ft


# ===========================
# PALETA DE CORES
# ===========================

COR_FUNDO = "#F5F2EE"
COR_CARD = "#FFFFFF"
COR_ROSA = "#B98FA3"
COR_VERDE = "#8FAE9A"
COR_VERMELHO = "#E57373"
COR_BEGE = "#E8C28F"
COR_TEXTO = "#333333"
COR_TEXTO_SECUNDARIO = "#6B625F"


# ===========================
# CARD PEQUENO
# ===========================

def card_pequeno(
    titulo,
    subtitulo,
    icone,
    cor_icone,
    ao_clicar
):

    return ft.Container(
        width=175,
        height=180,
        bgcolor=COR_CARD,
        border_radius=22,
        padding=18,
        ink=True,
        on_click=ao_clicar,

        shadow=ft.BoxShadow(
            blur_radius=12,
            color="#22000000",
            offset=ft.Offset(0, 4)
        ),

        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10,

            controls=[
                ft.Icon(
                    icone,
                    size=48,
                    color=cor_icone
                ),

                ft.Text(
                    titulo,
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    color=COR_TEXTO,
                    text_align=ft.TextAlign.CENTER
                ),

                ft.Text(
                    subtitulo,
                    size=15,
                    color=COR_TEXTO_SECUNDARIO,
                    text_align=ft.TextAlign.CENTER
                )
            ]
        )
    )


# ===========================
# CARD LARGO
# ===========================

def card_largo(
    titulo,
    subtitulo,
    icone,
    cor_fundo,
    cor_icone,
    ao_clicar
):

    return ft.Container(
        width=365,
        height=110,
        bgcolor=cor_fundo,
        border_radius=22,
        padding=20,
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
                ft.Icon(
                    icone,
                    size=48,
                    color=cor_icone
                ),

                ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=4,

                    controls=[
                        ft.Text(
                            titulo,
                            size=20,
                            weight=ft.FontWeight.BOLD,
                            color=COR_TEXTO
                        ),

                        ft.Text(
                            subtitulo,
                            size=15,
                            color=COR_TEXTO_SECUNDARIO,
                            width=240
                        )
                    ]
                )
            ]
        )
    )


# ===========================
# BOTÃO SOS
# ===========================

def botao_sos(ao_clicar):

    return ft.Container(
        width=365,
        height=90,
        bgcolor=COR_VERMELHO,
        border_radius=22,
        padding=18,
        ink=True,
        on_click=ao_clicar,

        shadow=ft.BoxShadow(
            blur_radius=12,
            color="#25000000",
            offset=ft.Offset(0, 4)
        ),

        content=ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15,

            controls=[
                ft.Container(
                    width=52,
                    height=52,
                    bgcolor="#FFFFFF",
                    border_radius=26,
                    alignment=ft.Alignment.CENTER,

                    content=ft.Icon(
                        ft.Icons.PHONE,
                        size=30,
                        color=COR_VERMELHO
                    )
                ),

                ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=2,

                    controls=[
                        ft.Text(
                            "SOS Emergência",
                            size=22,
                            weight=ft.FontWeight.BOLD,
                            color="#FFFFFF"
                        ),

                        ft.Text(
                            "Toque para ligar",
                            size=15,
                            color="#FFFFFF"
                        )
                    ]
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
        bgcolor=COR_FUNDO,
        padding=20,

        controls=[
            ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
                expand=True,
                scroll=ft.ScrollMode.AUTO,

                controls=[
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,

                        controls=[
                            ft.Column(
                                spacing=5,

                                controls=[
                                    ft.Text(
                                        "Olá, Maria!",
                                        size=30,
                                        weight=ft.FontWeight.BOLD,
                                        color="#8B3F5B"
                                    ),

                                    ft.Text(
                                        "Como posso te ajudar hoje?",
                                        size=18,
                                        color=COR_TEXTO,
                                        width=220
                                    )
                                ]
                            ),

                            ft.Container(
                                width=95,
                                height=95,
                                bgcolor="#F4E7EC",
                                border_radius=48,
                                alignment=ft.Alignment.CENTER,

                                content=ft.Text(
                                    "👵",
                                    size=55
                                )
                            )
                        ]
                    ),

                    ft.Container(
                        width=170,
                        height=170,
                        bgcolor="#F4E7EC",
                        border_radius=85,
                        alignment=ft.Alignment.CENTER,

                        content=ft.Icon(
                            ft.Icons.HEADSET_MIC,
                            size=78,
                            color=COR_ROSA
                        )
                    ),

                    ft.Text(
                        "Ajudante",
                        size=28,
                        weight=ft.FontWeight.BOLD,
                        color="#9B4E68"
                    ),

                    ft.Text(
                        "Toque para falar comigo",
                        size=17,
                        color=COR_TEXTO
                    ),

                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=15,

                        controls=[
                            card_pequeno(
                                "Comunicação",
                                "Fale com facilidade",
                                ft.Icons.CHAT_BUBBLE,
                                COR_ROSA,
                                lambda e: page.navigate("/comunicacao")
                            ),

                            card_pequeno(
                                "Rotina",
                                "Suas atividades do dia",
                                ft.Icons.CALENDAR_MONTH,
                                COR_VERDE,
                                lambda e: page.navigate("/rotina")
                            )
                        ]
                    ),

                    card_largo(
                        "Família / Cuidador",
                        "Fale com quem você ama",
                        ft.Icons.PEOPLE,
                        "#F8E8CF",
                        COR_BEGE,
                        lambda e: page.navigate("/familiares")
                    ),

                    botao_sos(
                        lambda e: print("SOS")
                    ),

                    ft.Container(
                        height=20
                    )
                ]
            )
        ]
    )