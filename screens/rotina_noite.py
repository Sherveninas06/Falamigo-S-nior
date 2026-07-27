import flet as ft

from services.rotina import obter_rotina, atualizar_tarefa


# ===========================
# PALETA DE CORES
# ===========================

COR_FUNDO = "#F7FAFC"
COR_CARD = "#FFFFFF"
COR_PRIMARIA = "#4F6BED"
COR_TEXTO = "#111827"
COR_TEXTO_SECUNDARIO = "#64748B"
COR_SUCESSO = "#22C55E"


# ===========================
# TELA ROTINA DA MANHÃ
# ===========================

def tela_rotina_noite(page):

    tarefas_salvas = obter_rotina("noite")

    texto_progresso = ft.Text(
        "0 de 4 concluídas",
        size=16,
        weight=ft.FontWeight.BOLD,
        color=COR_TEXTO_SECUNDARIO
    )

    checkboxes = []

    def atualizar_progresso():

        total_concluidas = sum(
            1 for checkbox in checkboxes if checkbox.value
        )

        texto_progresso.value = (
            f"{total_concluidas} de {len(checkboxes)} concluídas"
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

        checkbox = ft.Checkbox(
            label=tarefa["tarefa"],
            value=tarefa.get("concluida", False),
            on_change=ao_marcar,

            label_style=ft.TextStyle(
                size=20,
                weight=ft.FontWeight.W_600,
                color=COR_TEXTO
            ),

            active_color=COR_SUCESSO
        )

        checkboxes.append(checkbox)

        return checkbox

    lista_checkboxes = [
        criar_checkbox(indice, tarefa)
        for indice, tarefa in enumerate(tarefas_salvas)
    ]

    total_inicial = sum(
        1 for tarefa in tarefas_salvas
        if tarefa.get("concluida", False)
    )

    texto_progresso.value = (
        f"{total_inicial} de {len(tarefas_salvas)} concluídas"
    )

    return ft.View(
        route="/rotina/noite",
        bgcolor=COR_FUNDO,
        padding=20,

        appbar=ft.AppBar(
            title=ft.Text(
                "Rotina da noite",
                size=22,
                weight=ft.FontWeight.BOLD,
                color=COR_TEXTO
            ),

            leading=ft.IconButton(
                icon=ft.Icons.ARROW_BACK,
                tooltip="Voltar",
                on_click=lambda e: page.navigate("/rotina")
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
                        "🌙",
                        size=55
                    ),

                    ft.Text(
                        "Minha Noite",
                        size=26,
                        weight=ft.FontWeight.BOLD,
                        color=COR_TEXTO
                    ),

                    ft.Text(
                        "Marque as atividades conforme forem concluídas.",
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