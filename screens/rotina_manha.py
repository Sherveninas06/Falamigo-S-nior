import flet as ft


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

def tela_rotina_manha(page):

    texto_progresso = ft.Text(
        "0 de 4 concluídas",
        size=16,
        weight=ft.FontWeight.BOLD,
        color=COR_TEXTO_SECUNDARIO
    )

    def atualizar_progresso(e):

        tarefas = [
            higiene_matinal,
            cafe_manha,
            remedios,
            exercicio
        ]

        total_concluidas = sum(
            1 for tarefa in tarefas if tarefa.value
        )

        texto_progresso.value = (
            f"{total_concluidas} de {len(tarefas)} concluídas"
        )

        page.update()

    higiene_matinal = ft.Checkbox(
        label="Higiene matinal",
        value=False,
        on_change=atualizar_progresso,

        label_style=ft.TextStyle(
            size=20,
            weight=ft.FontWeight.W_600,
            color="#111827"
        )
    )

    cafe_manha = ft.Checkbox(
        label="Café da manhã",
        value=False,
        on_change=atualizar_progresso,

        label_style=ft.TextStyle(
            size=20,
            weight=ft.FontWeight.W_600,
            color="#111827"
        )
    )

    remedios = ft.Checkbox(
        label="Remédios",
        value=False,
        on_change=atualizar_progresso,

        label_style=ft.TextStyle(
            size=20,
            weight=ft.FontWeight.W_600,
            color="#111827"
        )
    )

    exercicio = ft.Checkbox(
        label="Exercícios físicos",
        value=False,
        on_change=atualizar_progresso,

        label_style=ft.TextStyle(
            size=20,
            weight=ft.FontWeight.W_600,
            color="#111827"
        )
    )

    return ft.View(
        route="/rotina/manha",
        bgcolor=COR_FUNDO,
        padding=20,

        appbar=ft.AppBar(
            title=ft.Text(
                "Rotina da manhã",
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
                        "🌅",
                        size=55
                    ),

                    ft.Text(
                        "Minha manhã",
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

                            controls=[
                                higiene_matinal,
                                cafe_manha,
                                remedios,
                                exercicio
                            ]
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