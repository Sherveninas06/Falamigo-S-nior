import flet as ft

from urllib.parse import quote


# ===========================
# NOVA PALETA
# ===========================

COR_FUNDO = "#F5F2EE"
COR_CARD = "#FFFFFF"

COR_PANCHO = "#C89A6B"
COR_PANCHO_ESCURO = "#9A6A3D"
COR_PANCHO_CLARO = "#F8E8D4"

COR_AZUL = "#4F7DBD"
COR_AZUL_ESCURO = "#365F96"
COR_AZUL_CLARO = "#E7EFF9"

COR_VERDE = "#6FAF79"
COR_VERDE_ESCURO = "#4F8158"
COR_VERDE_CLARO = "#E8F3EA"

COR_TEXTO = "#333333"
COR_TEXTO_SECUNDARIO = "#6B625F"
COR_BRANCO = "#FFFFFF"


# ===========================
# CONTATOS
# ===========================

CONTATOS = {
    "filha": {
        "nome": "Isabela",
        "telefone": "5547999999999",
        "foto": "familiares/Filha.jpg"
    },

    "filho": {
        "nome": "Mateus",
        "telefone": "5547988888888",
        "foto": "familiares/Filho.jpg"
    },

    "genro": {
        "nome": "João",
        "telefone": "5547977777777",
        "foto": "familiares/Genro.jpg"
    },

    "nora": {
        "nome": "Jasmin",
        "telefone": "5547966666666",
        "foto": "familiares/Nora.jpg"
    },

    "cuidador": {
        "nome": "Fernando",
        "telefone": "5547955555555",
        "foto": "cuidadores/Cuidador.jpg"
    },

    "cuidadora": {
        "nome": "Maria",
        "telefone": "5547944444444",
        "foto": "cuidadores/Cuidadora.jpg"
    }
}


# ===========================
# BOTÃO DE AÇÃO
# ===========================

def botao_acao(
    titulo,
    subtitulo,
    icone,
    cor_fundo,
    cor_icone,
    ao_clicar
):

    return ft.Container(
        width=355,
        height=95,
        bgcolor=cor_fundo,
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
            spacing=16,

            controls=[
                ft.Container(
                    width=58,
                    height=58,
                    bgcolor=COR_BRANCO,
                    border_radius=29,
                    alignment=ft.Alignment.CENTER,

                    content=ft.Icon(
                        icone,
                        size=31,
                        color=cor_icone
                    )
                ),

                ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=3,

                    controls=[
                        ft.Text(
                            titulo,
                            size=21,
                            weight=ft.FontWeight.BOLD,
                            color=COR_BRANCO
                        ),

                        ft.Text(
                            subtitulo,
                            size=14,
                            color=COR_BRANCO
                        )
                    ]
                )
            ]
        )
    )


# ===========================
# TELA DO CONTATO
# ===========================

def tela_contato(page, tipo_contato):

    contato = CONTATOS.get(tipo_contato)

    if contato is None:

        return ft.View(
            route=f"/contato/{tipo_contato}",
            bgcolor=COR_FUNDO,
            padding=20,

            appbar=ft.AppBar(
                title=ft.Text(
                    "Contato",
                    color=COR_BRANCO
                ),

                leading=ft.IconButton(
                    icon=ft.Icons.ARROW_BACK,
                    icon_color=COR_BRANCO,
                    on_click=lambda e: page.navigate(
                        "/familiares"
                    )
                ),

                bgcolor=COR_PANCHO
            ),

            controls=[
                ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,

                    controls=[
                        ft.Text(
                            "Contato não encontrado.",
                            size=20,
                            color=COR_TEXTO
                        )
                    ]
                )
            ]
        )

    def ligar(e):

        numero = contato["telefone"]

        page.launch_url(
            f"tel:{numero}"
        )

    def abrir_sms(e):

        numero = contato["telefone"]

        mensagem = (
            "Olá! Estou entrando em contato "
            "pelo aplicativo Ajudante."
        )

        mensagem_codificada = quote(
            mensagem
        )

        page.launch_url(
            f"sms:{numero}?body={mensagem_codificada}"
        )

    telefone_exibicao = contato["telefone"]

    return ft.View(
        route=f"/contato/{tipo_contato}",
        bgcolor=COR_FUNDO,

        padding=ft.Padding(
            left=20,
            top=20,
            right=20,
            bottom=40
        ),

        appbar=ft.AppBar(
            title=ft.Text(
                "Contato",
                size=22,
                weight=ft.FontWeight.BOLD,
                color=COR_BRANCO
            ),

            leading=ft.IconButton(
                icon=ft.Icons.ARROW_BACK,
                icon_color=COR_BRANCO,
                tooltip="Voltar",

                on_click=lambda e: page.navigate(
                    "/familiares"
                )
            ),

            bgcolor=COR_PANCHO
        ),

        controls=[
            ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=22,
                expand=True,
                scroll=ft.ScrollMode.AUTO,

                controls=[
                    ft.Container(
                        height=5
                    ),

                    ft.Container(
                        width=205,
                        height=205,
                        bgcolor=COR_PANCHO_CLARO,
                        border_radius=103,
                        padding=7,
                        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,

                        shadow=ft.BoxShadow(
                            blur_radius=12,
                            color="#20000000",
                            offset=ft.Offset(0, 5)
                        ),

                        content=ft.Image(
                            src=contato["foto"],
                            width=191,
                            height=191,
                            fit=ft.BoxFit.COVER
                        )
                    ),

                    ft.Text(
                        contato["nome"],
                        size=31,
                        weight=ft.FontWeight.BOLD,
                        color=COR_TEXTO,
                        text_align=ft.TextAlign.CENTER
                    ),


                    

                    botao_acao(
                        "LIGAR",
                        "Abrir o telefone",
                        ft.Icons.PHONE,
                        COR_AZUL,
                        COR_AZUL_ESCURO,
                        ligar
                    ),

                    botao_acao(
                        "MENSAGEM SMS",
                        "Abrir o aplicativo de mensagens",
                        ft.Icons.MESSAGE,
                        COR_VERDE,
                        COR_VERDE_ESCURO,
                        abrir_sms
                    ),

                    ft.Container(
                        width=340,
                        padding=15,
                        bgcolor=COR_PANCHO_CLARO,
                        border_radius=18,

                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=10,

                            controls=[
                                ft.Icon(
                                    ft.Icons.INFO_OUTLINE,
                                    color=COR_PANCHO_ESCURO,
                                    size=24
                                ),

                                ft.Text(
                                    "A mensagem será aberta no celular "
                                    "para você confirmar o envio.",
                                    size=14,
                                    color=COR_TEXTO,
                                    width=265,
                                    text_align=ft.TextAlign.CENTER
                                )
                            ]
                        )
                    ),

                    ft.Container(
                        height=20
                    )
                ]
            )
        ]
    )