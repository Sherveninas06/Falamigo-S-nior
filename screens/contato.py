import flet as ft


COR_FUNDO = "#F7FAFC"
COR_CARD = "#FFFFFF"
COR_TEXTO = "#1E293B"
COR_AZUL = "#3B82F6"
COR_VERDE = "#22C55E"
COR_BRANCO = "#FFFFFF"


CONTATOS = {
    "filha": {
        "nome": "Isabela",
        "telefone": "5547999999999",
        "foto": "familiares/filha.jpg"
    },

    "filho": {
        "nome": "Mateus",
        "telefone": "5547988888888",
        "foto": "familiares/filho.jpg"
    },

    "genro": {
        "nome": "João",
        "telefone": "5547977777777",
        "foto": "familiares/genro.jpg"
    },

    "nora": {
        "nome": "Jasmin",
        "telefone": "5547966666666",
        "foto": "familiares/nora.jpg"
    },

    "cuidador": {
        "nome": "Fernando",
        "telefone": "5547955555555",
        "foto": "cuidadores/cuidador.jpg"
    },

    "cuidadora": {
        "nome": "Maria",
        "telefone": "5547944444444",
        "foto": "cuidadores/cuidadora.jpg"
    }
}


def tela_contato(page, tipo_contato):

    contato = CONTATOS[tipo_contato]

    def ligar(e):
        page.launch_url(
            f"tel:{contato['telefone']}"
        )

    def abrir_whatsapp(e):
        page.launch_url(
            f"https://wa.me/{contato['telefone']}"
        )

    return ft.View(
        route=f"/contato/{tipo_contato}",
        bgcolor=COR_FUNDO,
        padding=20,

        appbar=ft.AppBar(
            title=ft.Text(
                "Contato",
                size=22,
                weight=ft.FontWeight.BOLD,
                color=COR_TEXTO
            ),

            leading=ft.IconButton(
                icon=ft.Icons.ARROW_BACK,
                tooltip="Voltar",
                on_click=lambda e: page.navigate("/familiares")
            ),

            bgcolor=COR_CARD
        ),

        controls=[
            ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=25,
                expand=True,

                controls=[
                    ft.Container(
                        width=180,
                        height=180,
                        border_radius=90,
                        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,

                        content=ft.Image(
                            src=contato["foto"],
                            width=180,
                            height=180,
                            fit=ft.BoxFit.COVER
                        )
                    ),

                    ft.Text(
                        contato["nome"],
                        size=30,
                        weight=ft.FontWeight.BOLD,
                        color=COR_TEXTO
                    ),

                    ft.Container(
                        width=320,
                        height=75,
                        bgcolor=COR_AZUL,
                        border_radius=18,
                        ink=True,
                        on_click=ligar,
                        alignment=ft.Alignment.CENTER,

                        content=ft.Text(
                            "📞 LIGAR",
                            size=22,
                            weight=ft.FontWeight.BOLD,
                            color=COR_BRANCO
                        )
                    ),

                    ft.Container(
                        width=320,
                        height=75,
                        bgcolor=COR_VERDE,
                        border_radius=18,
                        ink=True,
                        on_click=abrir_whatsapp,
                        alignment=ft.Alignment.CENTER,

                        content=ft.Text(
                            "💬 MENSAGEM",
                            size=22,
                            weight=ft.FontWeight.BOLD,
                            color=COR_BRANCO
                        )
                    )
                ]
            )
        ]
    )