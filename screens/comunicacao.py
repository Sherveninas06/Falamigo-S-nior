import flet as ft

from services.voz import falar
from services.comunicacoes import (
    carregar_comunicacoes,
    salvar_comunicacoes
)


# ===========================
# NOVA PALETA
# ===========================

COR_FUNDO = "#F5F2EE"
COR_CARD = "#FFFFFF"
COR_ROSA = "#B98FA3"
COR_ROSA_ESCURO = "#8B3F5B"
COR_ROSA_CLARO = "#F4E7EC"
COR_TEXTO = "#333333"
COR_TEXTO_SECUNDARIO = "#6B625F"
COR_VERMELHO = "#E57373"
COR_BRANCO = "#FFFFFF"


# ===========================
# CARTÃO DE COMUNICAÇÃO
# ===========================

def card_comunicacao(
    emoji,
    frase,
    ao_clicar,
    ao_segurar
):

    return ft.Container(
        width=150,
        height=145,
        bgcolor=COR_CARD,
        border_radius=22,
        padding=12,
        alignment=ft.Alignment.CENTER,
        on_click=ao_clicar,
        on_long_press=ao_segurar,
        ink=True,

        shadow=ft.BoxShadow(
            blur_radius=10,
            color="#18000000",
            offset=ft.Offset(0, 4)
        ),

        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,

            controls=[
                ft.Container(
                    width=65,
                    height=65,
                    bgcolor=COR_ROSA_CLARO,
                    border_radius=33,
                    alignment=ft.Alignment.CENTER,

                    content=ft.Text(
                        emoji,
                        size=36
                    )
                ),

                ft.Text(
                    frase,
                    size=17,
                    weight=ft.FontWeight.BOLD,
                    color=COR_TEXTO,
                    text_align=ft.TextAlign.CENTER,
                    max_lines=2
                )
            ]
        )
    )


# ===========================
# TELA DE COMUNICAÇÃO
# ===========================

def tela_comunicacao(page):

    comunicacoes = carregar_comunicacoes()

    mensagem = ft.Text(
        "Toque em um cartão para falar.",
        size=16,
        color=COR_TEXTO_SECUNDARIO,
        text_align=ft.TextAlign.CENTER
    )

    def selecionar_frase(frase):

        mensagem.value = f'Você selecionou: "{frase}"'
        mensagem.color = COR_ROSA_ESCURO
        mensagem.weight = ft.FontWeight.BOLD

        page.update()

        falar(frase)

    # ===========================
    # EXCLUIR CARTÃO
    # ===========================

    def abrir_exclusao(frase):

        def cancelar_exclusao(e):
            page.pop_dialog()

        def confirmar_exclusao(e):

            comunicacoes_atualizadas = carregar_comunicacoes()

            comunicacoes_atualizadas = [
                item
                for item in comunicacoes_atualizadas
                if item["frase"] != frase
            ]

            salvar_comunicacoes(
                comunicacoes_atualizadas
            )

            page.pop_dialog()

            page.navigate("/")
            page.navigate("/comunicacao")

        janela_exclusao = ft.AlertDialog(
            modal=True,
            bgcolor="#FFFFFF",
            
            title=ft.Text(
                "Excluir cartão",
                weight=ft.FontWeight.BOLD,
                color=COR_TEXTO
            ),

            content=ft.Text(
                f'Deseja excluir o cartão "{frase}"?',
                size=17,
                color=COR_TEXTO
            ),

            actions=[
                ft.TextButton(
                    "Cancelar",
                    on_click=cancelar_exclusao
                ),

                ft.FilledButton(
                    "Excluir",
                    icon=ft.Icons.DELETE,
                    bgcolor=COR_VERMELHO,
                    color=COR_BRANCO,
                    on_click=confirmar_exclusao
                )
            ],

            actions_alignment=ft.MainAxisAlignment.END
        )

        page.show_dialog(janela_exclusao)

    return ft.View(
        route="/comunicacao",
        bgcolor=COR_FUNDO,

        padding=ft.Padding(
            left=20,
            top=20,
            right=20,
            bottom=80
        ),

        floating_action_button=ft.FloatingActionButton(
            icon=ft.Icons.ADD,
            bgcolor=COR_ROSA,
            foreground_color=COR_BRANCO,
            tooltip="Adicionar palavra ou frase",

            on_click=lambda e: page.navigate(
                "/adicionar_comunicacao"
            )
        ),

        appbar=ft.AppBar(
            title=ft.Text(
                "Comunicação",
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

            actions=[
                ft.IconButton(
                    icon=ft.Icons.ADD,
                    icon_color=COR_BRANCO,
                    tooltip="Adicionar",
                    on_click=lambda e: page.navigate(
                        "/adicionar_comunicacao"
                    )
                )
            ],

            bgcolor=COR_ROSA
        ),

        controls=[
            ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=18,
                scroll=ft.ScrollMode.AUTO,
                expand=True,

                controls=[
                    ft.Text(
                        "Como você está se sentindo?",
                        size=25,
                        weight=ft.FontWeight.BOLD,
                        color=COR_TEXTO,
                        text_align=ft.TextAlign.CENTER
                    ),

                    ft.Text(
                        "Toque para falar. Pressione para excluir.",
                        size=16,
                        color=COR_TEXTO_SECUNDARIO,
                        text_align=ft.TextAlign.CENTER
                    ),

                    ft.Container(
                        width=370,
                        padding=15,
                        bgcolor="#FAF7F4",
                        border_radius=22,

                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=15,
                            run_spacing=15,
                            wrap=True,

                            controls=[
                                card_comunicacao(
                                    item["emoji"],
                                    item["frase"],

                                    lambda e, frase=item["frase"]:
                                        selecionar_frase(frase),

                                    lambda e, frase=item["frase"]:
                                        abrir_exclusao(frase)
                                )

                                for item in comunicacoes
                            ]
                        )
                    ),

                    ft.Container(
                        width=340,
                        padding=14,
                        bgcolor=COR_ROSA_CLARO,
                        border_radius=16,
                        alignment=ft.Alignment.CENTER,

                        content=mensagem
                    ),

                    ft.Container(
                        height=70
                    )
                ]
            )
        ]
    )