import flet as ft


# ===========================
# NOVA PALETA
# ===========================

COR_FUNDO = "#F5F2EE"
COR_CARD = "#FFFFFF"
COR_PANCHO = "#C89A6B"
COR_PANCHO_ESCURO = "#9A6A3D"
COR_PANCHO_CLARO = "#F8E8D4"
COR_TEXTO = "#333333"
COR_TEXTO_SECUNDARIO = "#6B625F"
COR_BRANCO = "#FFFFFF"


# ===========================
# CARD DO CONTATO
# ===========================

def card_familiar(
    titulo,
    foto,
    rota,
    page
):

    return ft.Container(
        width=165,
        height=205,
        bgcolor=COR_CARD,
        border_radius=22,
        padding=14,
        ink=True,

        on_click=lambda e: page.navigate(
            rota
        ),

        shadow=ft.BoxShadow(
            blur_radius=10,
            color="#18000000",
            offset=ft.Offset(0, 4)
        ),

        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=12,

            controls=[
                ft.Container(
                    width=110,
                    height=110,
                    bgcolor=COR_PANCHO_CLARO,
                    border_radius=55,
                    padding=5,
                    clip_behavior=ft.ClipBehavior.ANTI_ALIAS,

                    content=ft.Image(
                        src=foto,
                        width=100,
                        height=100,
                        fit=ft.BoxFit.COVER
                    )
                ),

                ft.Text(
                    titulo,
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    color=COR_TEXTO,
                    text_align=ft.TextAlign.CENTER
                ),

                ft.Text(
                    "Toque para abrir",
                    size=13,
                    color=COR_TEXTO_SECUNDARIO,
                    text_align=ft.TextAlign.CENTER
                )
            ]
        )
    )


# ===========================
# TELA FAMÍLIA / CUIDADOR
# ===========================

def tela_familiares(page):

    return ft.View(
        route="/familiares",
        bgcolor=COR_FUNDO,

        padding=ft.Padding(
            left=20,
            top=20,
            right=20,
            bottom=50
        ),

        appbar=ft.AppBar(
            title=ft.Text(
                "Família / Cuidador",
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

            bgcolor=COR_PANCHO
        ),

        controls=[
            ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=18,
                expand=True,
                scroll=ft.ScrollMode.AUTO,

                controls=[
                    ft.Container(
                        width=100,
                        height=100,
                        bgcolor=COR_PANCHO_CLARO,
                        border_radius=50,
                        alignment=ft.Alignment.CENTER,

                        content=ft.Icon(
                            ft.Icons.PEOPLE,
                            size=55,
                            color=COR_PANCHO_ESCURO
                        )
                    ),

                    ft.Text(
                        "Quem você deseja chamar?",
                        size=27,
                        weight=ft.FontWeight.BOLD,
                        color=COR_TEXTO,
                        text_align=ft.TextAlign.CENTER
                    ),

                    ft.Text(
                        "Toque na foto de um familiar ou cuidador.",
                        size=16,
                        color=COR_TEXTO_SECUNDARIO,
                        text_align=ft.TextAlign.CENTER,
                        width=340
                    ),

                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=15,

                        controls=[
                            card_familiar(
                                "Filha",
                                "familiares/Filha.jpg",
                                "/contato/filha",
                                page
                            ),

                            card_familiar(
                                "Filho",
                                "familiares/Filho.jpg",
                                "/contato/filho",
                                page
                            )
                        ]
                    ),

                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=15,

                        controls=[
                            card_familiar(
                                "Genro",
                                "familiares/Genro.jpg",
                                "/contato/genro",
                                page
                            ),

                            card_familiar(
                                "Nora",
                                "familiares/Nora.jpg",
                                "/contato/nora",
                                page
                            )
                        ]
                    ),

                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=15,

                        controls=[
                            card_familiar(
                                "Cuidador",
                                "cuidadores/Cuidador.jpg",
                                "/contato/cuidador",
                                page
                            ),

                            card_familiar(
                                "Cuidadora",
                                "cuidadores/Cuidadora.jpg",
                                "/contato/cuidadora",
                                page
                            )
                        ]
                    ),

                    ft.Container(
                        height=30
                    )
                ]
            )
        ]
    )