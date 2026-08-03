import flet as ft

from services.comunicacoes import adicionar_comunicacao


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
COR_ERRO = "#D9534F"
COR_BRANCO = "#FFFFFF"


# ===========================
# SUGESTÃO DE EMOJI
# ===========================

def sugerir_emoji(frase):

    texto = frase.lower().strip()

    sugestoes = {
        "água": "💧",
        "agua": "💧",
        "sede": "🥤",

        "comida": "🍽️",
        "fome": "🍽️",
        "comer": "🍎",
        "café": "☕",
        "cafe": "☕",

        "banheiro": "🚻",

        "dor": "🤕",
        "machucado": "🩹",
        "machucada": "🩹",

        "remédio": "💊",
        "remedio": "💊",
        "medicamento": "💊",

        "médico": "🩺",
        "medico": "🩺",
        "ambulância": "🚑",
        "ambulancia": "🚑",

        "ajuda": "🆘",
        "socorro": "🆘",
        "urgente": "⚠️",

        "sono": "😴",
        "dormir": "🛏️",
        "descansar": "🛌",
        "cansado": "😴",
        "cansada": "😴",

        "feliz": "🥰",
        "bem": "😊",
        "triste": "😢",
        "mal": "😟",
        "medo": "😨",
        "bravo": "😡",
        "brava": "😡",
        "abraço": "🤗",
        "abraco": "🤗",

        "telefone": "📞",
        "ligar": "📞",
        "ouvi": "👂",
        "devagar": "🗣️",
        "entendi": "👌",

        "sentar": "🪑",
        "caminhar": "🚶",
        "sair": "🚪",
        "casa": "🏠",

        "sim": "✅",
        "não": "❌",
        "nao": "❌",

        "obrigado": "🙏",
        "obrigada": "🙏",
        "por favor": "🤲",
        "repita": "🔁"
    }

    for palavra, emoji in sugestoes.items():
        if palavra in texto:
            return emoji

    return "💬"


# ===========================
# TELA ADICIONAR COMUNICAÇÃO
# ===========================

def tela_adicionar_comunicacao(page):

    emoji_selecionado = ft.Text(
        "💬",
        size=55
    )

    mensagem_erro = ft.Text(
        "",
        size=15,
        color=COR_ERRO,
        text_align=ft.TextAlign.CENTER
    )

    def atualizar_emoji(e):

        frase_digitada = campo_frase.value or ""

        emoji_selecionado.value = sugerir_emoji(
            frase_digitada
        )

        mensagem_erro.value = ""

        page.update()

    campo_frase = ft.TextField(
        label="Palavra ou frase",
        hint_text="Ex.: Estou com sede",
        multiline=True,
        min_lines=1,
        max_lines=3,
        width=360,
        text_size=18,
        autofocus=True,

        color=COR_TEXTO,
        bgcolor=COR_CARD,
        filled=True,

        border_color=COR_ROSA,
        focused_border_color=COR_ROSA_ESCURO,
        cursor_color=COR_ROSA_ESCURO,

        label_style=ft.TextStyle(
            color=COR_ROSA_ESCURO,
            weight=ft.FontWeight.BOLD
        ),

        hint_style=ft.TextStyle(
            color=COR_TEXTO_SECUNDARIO
        ),

        border_radius=16,
        on_change=atualizar_emoji
    )

    def salvar(e):

        frase = campo_frase.value or ""

        if not frase.strip():

            mensagem_erro.value = (
                "Digite uma palavra ou frase antes de salvar."
            )

            page.update()
            return

        foi_salvo = adicionar_comunicacao(
            frase=frase,
            emoji=emoji_selecionado.value
        )

        if foi_salvo:
            page.navigate("/comunicacao")

    return ft.View(
        route="/adicionar_comunicacao",
        bgcolor=COR_FUNDO,
        padding=20,

        appbar=ft.AppBar(
            title=ft.Text(
                "Adicionar comunicação",
                size=21,
                weight=ft.FontWeight.BOLD,
                color=COR_BRANCO
            ),

            leading=ft.IconButton(
                icon=ft.Icons.ARROW_BACK,
                icon_color=COR_BRANCO,
                tooltip="Voltar",
                on_click=lambda e: page.navigate(
                    "/comunicacao"
                )
            ),

            bgcolor=COR_ROSA
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

                    ft.Text(
                        "Adicionar palavra ou frase",
                        size=25,
                        weight=ft.FontWeight.BOLD,
                        color=COR_TEXTO,
                        text_align=ft.TextAlign.CENTER
                    ),

                    ft.Text(
                        " ",
                        size=16,
                        color=COR_TEXTO_SECUNDARIO,
                        text_align=ft.TextAlign.CENTER,
                        width=340
                    ),

                    campo_frase,

                    ft.Container(
                        width=180,
                        height=150,
                        bgcolor=COR_ROSA_CLARO,
                        border_radius=26,
                        alignment=ft.Alignment.CENTER,

                        shadow=ft.BoxShadow(
                            blur_radius=10,
                            color="#18000000",
                            offset=ft.Offset(0, 4)
                        ),

                        content=ft.Column(
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=8,

                            controls=[
                                ft.Text(
                                    "Emoji sugerido",
                                    size=17,
                                    weight=ft.FontWeight.BOLD,
                                    color=COR_ROSA_ESCURO
                                ),

                                emoji_selecionado
                            ]
                        )
                    ),

                    mensagem_erro,

                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=15,

                        controls=[
                            ft.OutlinedButton(
                                "Cancelar",
                                icon=ft.Icons.CLOSE,
                                on_click=lambda e: page.navigate(
                                    "/comunicacao"
                                )
                            ),

                            ft.FilledButton(
                                "Salvar",
                                icon=ft.Icons.SAVE,
                                bgcolor=COR_ROSA,
                                color=COR_BRANCO,
                                on_click=salvar
                            )
                        ]
                    ),

                    ft.Container(
                        height=30
                    )
                ]
            )
        ]
    )