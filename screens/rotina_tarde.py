import flet as ft

from services.rotina import (
    obter_rotina,
    atualizar_tarefa,
    excluir_tarefa
)


# ===========================
# PALETA DE CORES
# ===========================

COR_FUNDO = "#F7FAFC"
COR_CARD = "#FFFFFF"
COR_PRIMARIA = "#4F6BED"
COR_TEXTO = "#111827"
COR_TEXTO_SECUNDARIO = "#64748B"
COR_SUCESSO = "#22C55E"
COR_VERMELHO = "#DC2626"


# ===========================
# TELA ROTINA DA MANHÃ
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
        color=COR_TEXTO_SECUNDARIO
    )

    checkboxes = []

    # ===========================
    # CANCELAR EXCLUSÃO
    # ===========================

    def cancelar_exclusao(e):

        indice_selecionado["valor"] = None
        area_exclusao.visible = False

        page.update()

    # ===========================
    # CONFIRMAR EXCLUSÃO
    # ===========================

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

    # ===========================
    # ÁREA DE EXCLUSÃO
    # ===========================

    area_exclusao = ft.Container(
        visible=False,
        width=340,
        padding=20,
        bgcolor="#FEF2F2",
        border_radius=16,

        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15,

            controls=[
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
                            color="white",
                            on_click=confirmar_exclusao
                        )
                    ]
                )
            ]
        )
    )

    # ===========================
    # ATUALIZAR PROGRESSO
    # ===========================

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

    # ===========================
    # CRIAR CHECKBOX
    # ===========================

    def criar_checkbox(indice, tarefa):

        def ao_marcar(e):

            atualizar_tarefa(
                "manha",
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
                size=20,
                weight=ft.FontWeight.W_600,
                color=COR_TEXTO
            ),

            active_color=COR_SUCESSO
        )

        checkboxes.append(checkbox)

        return ft.Container(
            border_radius=12,
            padding=5,
            ink=True,
            on_long_press=ao_segurar,
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
        padding=20,

        floating_action_button=ft.FloatingActionButton(
            icon=ft.Icons.ADD,
            bgcolor=COR_PRIMARIA,
            foreground_color="white",
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
                color=COR_TEXTO
            ),

            leading=ft.IconButton(
                icon=ft.Icons.ARROW_BACK,
                tooltip="Voltar",
                on_click=lambda e: page.navigate(
                    "/rotina"
                )
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
                        "☀️",
                        size=55
                    ),

                    ft.Text(
                        "Minha Tarde",
                        size=26,
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
                        width=340,
                        bgcolor=COR_CARD,
                        border_radius=20,
                        padding=20,

                        shadow=ft.BoxShadow(
                            blur_radius=10,
                            color="#22000000",
                            offset=ft.Offset(0, 4)
                        ),

                        content=ft.Column(
                            spacing=18,
                            controls=lista_checkboxes
                        )
                    ),

                    # A área de exclusão fica aqui:
                    # depois da lista de tarefas
                    # e antes do progresso.
                    area_exclusao,

                    ft.Container(
                        width=340,
                        padding=15,
                        border_radius=15,
                        bgcolor="#ECFDF5",
                        alignment=ft.Alignment.CENTER,
                        content=texto_progresso
                    )
                ]
            )
        ]
    )