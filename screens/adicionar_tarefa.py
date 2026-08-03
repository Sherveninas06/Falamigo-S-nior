import flet as ft

from services.rotina import adicionar_tarefa


COR_FUNDO = "#F7FAFC"
COR_CARD = "#FFFFFF"
COR_PRIMARIA = "#4F6BED"
COR_TEXTO = "#111827"
COR_ERRO = "#DC2626"


def tela_adicionar_tarefa(page, periodo):

    nomes_periodos = {
        "manha": "Manhã",
        "tarde": "Tarde",
        "noite": "Noite"
    }

    nome_periodo = nomes_periodos.get(
        periodo,
        "Rotina"
    )

    mensagem_erro = ft.Text(
        "",
        size=15,
        color=COR_ERRO
    )

    campo_tarefa = ft.TextField(
        label="Nova tarefa",
        hint_text="Ex.: Beber água",
        width=380,
        text_size=18,
        autofocus=True,

        color=COR_TEXTO,
        bgcolor=COR_CARD,
        filled=True,

        border_color=COR_PRIMARIA,
        focused_border_color="#2563EB",
        cursor_color="#2563EB",

        hint_style=ft.TextStyle(
            color="#64748B"
        ),

        label_style=ft.TextStyle(
            color=COR_PRIMARIA,
            weight=ft.FontWeight.BOLD
        ),

        border_radius=12
    )

    def voltar(e):
        page.navigate(
            f"/rotina/{periodo}"
        )

    def salvar(e):

        tarefa = campo_tarefa.value or ""

        if not tarefa.strip():
            mensagem_erro.value = (
                "Digite o nome da tarefa."
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
                color=COR_TEXTO
            ),

            leading=ft.IconButton(
                icon=ft.Icons.ARROW_BACK,
                tooltip="Voltar",
                on_click=voltar
            ),

            bgcolor=COR_CARD
        ),

        controls=[
            ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=22,

                controls=[
                    ft.Text(
                        f"Nova tarefa da {nome_periodo.lower()}",
                        size=25,
                        weight=ft.FontWeight.BOLD,
                        color=COR_TEXTO,
                        text_align=ft.TextAlign.CENTER
                    ),

                    campo_tarefa,

                    mensagem_erro,

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
                                "Salvar",
                                icon=ft.Icons.SAVE,
                                bgcolor=COR_PRIMARIA,
                                color="white",
                                on_click=salvar
                            )
                        ]
                    )
                ]
            )
        ]
    )