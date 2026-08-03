import flet as ft

from services.rotina import (
    obter_rotina,
    atualizar_tarefa,
    excluir_tarefa
)


# ===========================
# NOVA PALETA
# ===========================

COR_FUNDO = "#F5F2EE"
COR_CARD = "#FFFFFF"
COR_VERDE = "#8FAE9A"
COR_VERDE_ESCURO = "#5F806B"
COR_VERDE_CLARO = "#EAF3EC"
COR_AMARELO_CLARO = "#FFF3D8"
COR_TEXTO = "#333333"
COR_TEXTO_SECUNDARIO = "#6B625F"
COR_VERMELHO = "#E57373"
COR_VERMELHO_CLARO = "#FDE8E6"
COR_BRANCO = "#FFFFFF"


# ===========================
# TELA ROTINA DA TARDE
# ===========================

def tela_rotina_tarde(page):

    tarefas_salvas = obter_rotina("tarde")

    indice_selecionado = {
        "valor": None
    }

    texto_exclusao = ft.Text(
        "",
        size=18,
        weight=ft.FontWeight.BOLD,
        color=COR_TEXTO,
        text_align=ft.TextAlign.CENTER
    )

    texto_progresso = ft.Text(
        "0 de 0 concluídas",
        size=16,
        weight=ft.FontWeight.BOLD,
        color=COR_VERDE_ESCURO
    )

    checkboxes = []

    def cancelar_exclusao(e):
        indice_selecionado["valor"] = None
        area_exclusao.visible = False
        page.update()

    def confirmar_exclusao(e):

        indice = indice_selecionado["valor"]

        if indice is None:
            return

        foi_excluida = excluir_tarefa(
            "tarde",
            indice
        )

        if foi_excluida:
            page.navigate("/rotina")
            page.navigate("/rotina/tarde")

    area_exclusao = ft.Container(
        visible=False,
        width=365,
        padding=20,
        bgcolor=COR_VERMELHO_CLARO,
        border_radius=20,

        shadow=ft.BoxShadow(
            blur_radius=8,
            color="#18000000",
            offset=ft.Offset(0, 3)
        ),

        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15,

            controls=[
                ft.Icon(
                    ft.Icons.DELETE_OUTLINE,
                    size=36,
                    color=COR_VERMELHO
                ),

                texto_exclusao,

                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=15,

                    controls=[
                        ft.OutlinedButton(
                            "Cancelar",
                            icon=ft.Icons.CLOSE,
                            on_click=cancelar_exclusao
                        ),

                        ft.FilledButton(
                            "Excluir",
                            icon=ft.Icons.DELETE,
                            bgcolor=COR_VERMELHO,
                            color=COR_BRANCO,
                            on_click=confirmar_exclusao
                        )
                    ]
                )
            ]
        )
    )

    def atualizar_progresso():

        total_concluidas = sum(
            1
            for checkbox in checkboxes
            if checkbox.value
        )

        texto_progresso.value = (
            f"{total_concluidas} de "
            f"{len(checkboxes)} concluídas"
        )

        page.update()

    def criar_checkbox(indice, tarefa):

        def ao_marcar(e):

            atualizar_tarefa(
                "tarde",
                indice,
                e.control.value
            )

            atualizar_progresso()

        def ao_segurar(e):

            indice_selecionado["valor"] = indice

            texto_exclusao.value = (
                f'Deseja excluir '
                f'"{tarefa["tarefa"]}"?'
            )

            area_exclusao.visible = True
            page.update()

        checkbox = ft.Checkbox(
            label=tarefa["tarefa"],

            value=tarefa.get(
                "concluida",
                False
            ),

            on_change=ao_marcar,

            label_style=ft.TextStyle(
                size=19,
                weight=ft.FontWeight.W_600,
                color=COR_TEXTO
            ),

            active_color=COR_VERDE
        )

        checkboxes.append(checkbox)

        return ft.Container(
            width=325,
            padding=10,
            bgcolor=COR_CARD,
            border_radius=14,
            ink=True,
            on_long_press=ao_segurar,

            shadow=ft.BoxShadow(
                blur_radius=5,
                color="#10000000",
                offset=ft.Offset(0, 2)
            ),

            content=checkbox
        )

    lista_checkboxes = [
        criar_checkbox(indice, tarefa)
        for indice, tarefa
        in enumerate(tarefas_salvas)
    ]

    total_inicial = sum(
        1
        for tarefa in tarefas_salvas
        if tarefa.get("concluida", False)
    )

    texto_progresso.value = (
        f"{total_inicial} de "
        f"{len(tarefas_salvas)} concluídas"
    )

    return ft.View(
        route="/rotina/tarde",
        bgcolor=COR_FUNDO,

        padding=ft.Padding(
            left=20,
            top=20,
            right=20,
            bottom=80
        ),

        floating_action_button=ft.FloatingActionButton(
            icon=ft.Icons.ADD,
            bgcolor=COR_VERDE,
            foreground_color=COR_BRANCO,
            tooltip="Adicionar tarefa",

            on_click=lambda e: page.navigate(
                "/rotina/adicionar/tarde"
            )
        ),

        appbar=ft.AppBar(
            title=ft.Text(
                "Rotina da tarde",
                size=22,
                weight=ft.FontWeight.BOLD,
                color=COR_BRANCO
            ),

            leading=ft.IconButton(
                icon=ft.Icons.ARROW_BACK,
                icon_color=COR_BRANCO,
                tooltip="Voltar",

                on_click=lambda e: page.navigate(
                    "/rotina"
                )
            ),

            actions=[
                ft.IconButton(
                    icon=ft.Icons.ADD,
                    icon_color=COR_BRANCO,
                    tooltip="Adicionar tarefa",

                    on_click=lambda e: page.navigate(
                        "/rotina/adicionar/tarde"
                    )
                )
            ],

            bgcolor=COR_VERDE
        ),

        controls=[
            ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=18,
                expand=True,
                scroll=ft.ScrollMode.AUTO,

                controls=[
                    ft.Container(
                        width=95,
                        height=95,
                        bgcolor=COR_AMARELO_CLARO,
                        border_radius=48,
                        alignment=ft.Alignment.CENTER,

                        content=ft.Text(
                            "☀️",
                            size=50
                        )
                    ),

                    ft.Text(
                        "Minha tarde",
                        size=28,
                        weight=ft.FontWeight.BOLD,
                        color=COR_TEXTO
                    ),

                    ft.Text(
                        "Marque as atividades conforme "
                        "forem concluídas.",
                        size=16,
                        color=COR_TEXTO_SECUNDARIO,
                        text_align=ft.TextAlign.CENTER
                    ),

                    ft.Container(
                        width=365,
                        padding=18,
                        bgcolor="#FAF7F4",
                        border_radius=22,

                        content=ft.Column(
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=12,
                            controls=lista_checkboxes
                        )
                    ),

                    area_exclusao,

                    ft.Container(
                        width=365,
                        padding=16,
                        border_radius=18,
                        bgcolor=COR_VERDE_CLARO,
                        alignment=ft.Alignment.CENTER,

                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=8,

                            controls=[
                                ft.Icon(
                                    ft.Icons.CHECK_CIRCLE,
                                    color=COR_VERDE_ESCURO,
                                    size=24
                                ),

                                texto_progresso
                            ]
                        )
                    ),

                    ft.Text(
                        "Pressione uma tarefa para excluir.",
                        size=14,
                        color=COR_TEXTO_SECUNDARIO,
                        text_align=ft.TextAlign.CENTER
                    ),

                    ft.Container(
                        height=60
                    )
                ]
            )
        ]
    )