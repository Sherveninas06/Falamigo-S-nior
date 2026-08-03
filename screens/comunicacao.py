import flet as ft

from services.voz import falar
from services.comunicacoes import (
    carregar_comunicacoes,
    salvar_comunicacoes
)


# ===========================
# PALETA DE CORES
# ===========================

COR_FUNDO = "#F7FAFC"
COR_CARD = "#FFFFFF"
COR_PRIMARIA = "#4F6BED"
COR_TEXTO = "#1F2937"
COR_VERMELHO = "#DC2626"


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
        height=135,
        bgcolor=COR_CARD,
        border_radius=20,
        padding=12,
        alignment=ft.Alignment.CENTER,

        # Clique normal: fala a frase
        on_click=ao_clicar,

        # Pressionar e segurar: oferece opção de exclusão
        on_long_press=ao_segurar,

        ink=True,

        shadow=ft.BoxShadow(
            blur_radius=8,
            color="#22000000",
            offset=ft.Offset(0, 3)
        ),

        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=8,

            controls=[
                ft.Text(
                    emoji,
                    size=42
                ),

                ft.Text(
                    frase,
                    size=18,
                    weight=ft.FontWeight.BOLD,
                    color=COR_TEXTO,
                    text_align=ft.TextAlign.CENTER
                )
            ]
        )
    )


# ===========================
# TELA COMUNICAÇÃO
# ===========================

def tela_comunicacao(page):

    comunicacoes = carregar_comunicacoes()

    mensagem = ft.Text(
        "Nenhuma frase selecionada.",
        size=18,
        color="#64748B",
        text_align=ft.TextAlign.CENTER
    )

    def selecionar_frase(frase):

        mensagem.value = f'Você selecionou: "{frase}"'
        mensagem.color = COR_PRIMARIA
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

            salvar_comunicacoes(comunicacoes_atualizadas)

            #Fechar a janela 
            page.pop_dialog()

            # Reabre a tela para atualizar os cartões
            page.navigate("/")
            page.navigate("/comunicacao")

        janela_exclusao = ft.AlertDialog(
            modal=True,

            title=ft.Text(
                "Excluir cartão",
                weight=ft.FontWeight.BOLD
            ),

            content=ft.Text(
                f'Deseja excluir o cartão "{frase}"?',
                size=17
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
                    color="white",
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
            bottom=20
        ),

        floating_action_button=ft.FloatingActionButton(
            icon=ft.Icons.ADD,
            bgcolor=COR_PRIMARIA,
            foreground_color="white",
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
                color = "#000000"
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
                spacing=18,
                expand=True,
                scroll=ft.ScrollMode.AUTO,

                controls=[
                    ft.Text(
                        "Como você está se sentindo?",
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        color=COR_TEXTO,
                        text_align=ft.TextAlign.CENTER
                    ),

                    ft.Text(
                        "Toque para falar. Pressione para excluir.",
                        size=16,
                        color="#64748B",
                        text_align=ft.TextAlign.CENTER
                    ),

                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=15,
                        run_spacing=15,
                        wrap=True,

                        controls=[
                            card_comunicacao(
                                item["emoji"],
                                item["frase"],

                                # Toque normal
                                lambda e, frase=item["frase"]:
                                    selecionar_frase(frase),

                                # Pressionar e segurar
                                lambda e, frase=item["frase"]:
                                    abrir_exclusao(frase)
                            )

                            for item in comunicacoes
                        ]
                    ),

                    mensagem,

                    ft.Container(
                        height=90
                    )
                ]
            )
        ]
    )