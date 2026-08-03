import flet as ft

from services.rotina import adicionar_tarefa


# ===========================
# NOVA PALETA
# ===========================

COR_FUNDO = "#F5F2EE"
COR_CARD = "#FFFFFF"
COR_VERDE = "#8FAE9A"
COR_VERDE_ESCURO = "#5F806B"
COR_VERDE_CLARO = "#EAF3EC"
COR_ROSA = "#B98FA3"
COR_ROSA_CLARO = "#F4E7EC"
COR_BEGE_CLARO = "#FAEEDC"
COR_TEXTO = "#333333"
COR_TEXTO_SECUNDARIO = "#6B625F"
COR_ERRO = "#D9534F"
COR_BRANCO = "#FFFFFF"


# ===========================
# TELA ADICIONAR TAREFA
# ===========================

def tela_adicionar_tarefa(page, periodo):

    nomes_periodos = {
        "manha": "Manhã",
        "tarde": "Tarde",
        "noite": "Noite"
    }

    emojis_periodos = {
        "manha": "🌅",
        "tarde": "☀️",
        "noite": "🌙"
    }

    cores_periodos = {
        "manha": COR_VERDE,
        "tarde": COR_VERDE,
        "noite": COR_ROSA
    }

    fundos_periodos = {
        "manha": COR_BEGE_CLARO,
        "tarde": "#FFF3D8",
        "noite": COR_ROSA_CLARO
    }

    nome_periodo = nomes_periodos.get(
        periodo,
        "Rotina"
    )

    emoji_periodo = emojis_periodos.get(
        periodo,
        "📅"
    )

    cor_periodo = cores_periodos.get(
        periodo,
        COR_VERDE
    )

    cor_fundo_periodo = fundos_periodos.get(
        periodo,
        COR_VERDE_CLARO
    )

    mensagem_erro = ft.Text(
        "",
        size=15,
        color=COR_ERRO,
        text_align=ft.TextAlign.CENTER
    )

    campo_tarefa = ft.TextField(
        label="Nova tarefa",
        hint_text="Ex.: Beber água",
        width=360,
        text_size=18,
        autofocus=True,

        color=COR_TEXTO,
        bgcolor=COR_CARD,
        filled=True,

        border_color=cor_periodo,
        focused_border_color=COR_VERDE_ESCURO,
        cursor_color=COR_VERDE_ESCURO,

        label_style=ft.TextStyle(
            color=COR_TEXTO,
            weight=ft.FontWeight.BOLD
        ),

        hint_style=ft.TextStyle(
            color=COR_TEXTO_SECUNDARIO
        ),

        border_radius=16
    )

    def voltar(e):

        page.navigate(
            f"/rotina/{periodo}"
        )

    def salvar(e):

        tarefa = campo_tarefa.value or ""

        if not tarefa.strip():

            mensagem_erro.value = (
                "Digite o nome da tarefa antes de salvar."
            )

            page.update()
            return

        foi_adicionada = adicionar_tarefa(
            periodo,
            tarefa
        )

        if foi_adicionada:

            page.navigate(
                f"/rotina/{periodo}"
            )

    return ft.View(
        route=f"/rotina/adicionar/{periodo}",
        bgcolor=COR_FUNDO,
        padding=20,

        appbar=ft.AppBar(
            title=ft.Text(
                f"Adicionar tarefa — {nome_periodo}",
                size=21,
                weight=ft.FontWeight.BOLD,
                color=COR_BRANCO
            ),

            leading=ft.IconButton(
                icon=ft.Icons.ARROW_BACK,
                icon_color=COR_BRANCO,
                tooltip="Voltar",
                on_click=voltar
            ),

            bgcolor=cor_periodo
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
                        width=105,
                        height=105,
                        bgcolor=cor_fundo_periodo,
                        border_radius=53,
                        alignment=ft.Alignment.CENTER,

                        content=ft.Text(
                            emoji_periodo,
                            size=55
                        )
                    ),

                    ft.Text(
                        f"Nova tarefa da {nome_periodo.lower()}",
                        size=26,
                        weight=ft.FontWeight.BOLD,
                        color=COR_TEXTO,
                        text_align=ft.TextAlign.CENTER
                    ),

                    ft.Text(
                        "Digite uma atividade para adicionar ao checklist.",
                        size=16,
                        color=COR_TEXTO_SECUNDARIO,
                        text_align=ft.TextAlign.CENTER,
                        width=330
                    ),

                    ft.Container(
                        width=375,
                        padding=18,
                        bgcolor="#FAF7F4",
                        border_radius=22,

                        content=ft.Column(
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=16,

                            controls=[
                                campo_tarefa,
                                mensagem_erro
                            ]
                        )
                    ),

                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=15,

                        controls=[
                            ft.OutlinedButton(
                                "Cancelar",
                                icon=ft.Icons.CLOSE,
                                on_click=voltar
                            ),

                            ft.FilledButton(
                                "Salvar tarefa",
                                icon=ft.Icons.SAVE,
                                bgcolor=cor_periodo,
                                color=COR_BRANCO,
                                on_click=salvar
                            )
                        ]
                    ),

                    ft.Container(
                        width=350,
                        padding=15,
                        bgcolor=COR_VERDE_CLARO,
                        border_radius=16,

                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=10,

                            controls=[
                                ft.Icon(
                                    ft.Icons.INFO_OUTLINE,
                                    color=COR_VERDE_ESCURO,
                                    size=24
                                ),

                                ft.Text(
                                    "A tarefa ficará salva no período escolhido.",
                                    size=14,
                                    color=COR_TEXTO,
                                    width=260,
                                    text_align=ft.TextAlign.CENTER
                                )
                            ]
                        )
                    ),

                    ft.Container(
                        height=30
                    )
                ]
            )
        ]
    )