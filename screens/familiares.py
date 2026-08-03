import flet as ft


COR_FUNDO = "#F7FAFC"
COR_CARD = "#FFFFFF"
COR_TEXTO = "#1E293B"
COR_TEXTO_SECUNDARIO = "#64748B"


def card_familiar(titulo, foto, rota, page):

    return ft.Container(
        width=150,
        height=180,
        bgcolor=COR_CARD,
        border_radius=20,
        padding=15,
        ink=True,
        on_click=lambda e: page.navigate(rota),

        shadow=ft.BoxShadow(
            blur_radius=10,
            color="#22000000",
            offset=ft.Offset(0, 4)
        ),

        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=12,

            controls=[
                ft.Container(
                    width=95,
                    height=95,
                    border_radius=50,
                    clip_behavior=ft.ClipBehavior.ANTI_ALIAS,

                    content=ft.Image(
                        src=foto,
                        width=95,
                        height=95,
                        fit=ft.BoxFit.COVER
                    )
                ),

                ft.Text(
                    titulo,
                    size=19,
                    weight=ft.FontWeight.BOLD,
                    color=COR_TEXTO
                )
            ]
        )
    )


def tela_familiares(page):

    return ft.View(
        route="/familiares",
        bgcolor=COR_FUNDO,
        padding=20,

        appbar=ft.AppBar(
            title=ft.Text(
                "Familiar / Cuidador",
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
                expand=True,
                scroll=ft.ScrollMode.AUTO,

                controls=[
                    ft.Text(
                        "Quem você deseja chamar?",
                        size=25,
                        weight=ft.FontWeight.BOLD,
                        color=COR_TEXTO,
                        text_align=ft.TextAlign.CENTER
                    ),

                    ft.Text(
                        "Toque na foto da pessoa",
                        size=16,
                        color=COR_TEXTO_SECUNDARIO
                    ),

                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=15,

                        controls=[
                            card_familiar(
                                "Filha",
                                "familiares/filha.jpg",
                                "/contato/filha",
                                page
                            ),

                            card_familiar(
                                "Filho",
                                "familiares/filho.jpg",
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
                                "familiares/genro.jpg",
                                "/contato/genro",
                                page
                            ),

                            card_familiar(
                                "Nora",
                                "familiares/nora.jpg",
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
                                "cuidadores/cuidador.jpg",
                                "/contato/cuidador",
                                page
                            ),

                            card_familiar(
                                "Cuidadora",
                                "cuidadores/cuidadora.jpg",
                                "/contato/cuidadora",
                                page
                            )
                        ]
                    )
                ]
            )
        ]
    )