import flet as ft

from services.comunicacoes import adicionar_comunicacao


COR_FUNDO = "#F7FAFC"
COR_CARD = "#FFFFFF"
COR_PRIMARIA = "#4F6BED"
COR_TEXTO = "#1F2937"
COR_ERRO = "#DC2626"


def sugerir_emoji(frase):

    texto = frase.lower().strip()

    sugestoes = {
        "água": "💧",
        "agua": "💧",
        "sede": "💧",

        "comida": "🍽️",
        "fome": "🍽️",
        "almoço": "🍽️",
        "almoco": "🍽️",
        "jantar": "🍽️",

        "banheiro": "🚻",

        "dor": "🤕",
        "machucado": "🤕",
        "machucada": "🤕",

        "remédio": "💊",
        "remedio": "💊",
        "medicamento": "💊",

        "ajuda": "🆘",
        "socorro": "🆘",

        "sono": "😴",
        "dormir": "😴",
        "cansado": "😴",
        "cansada": "😴",

        "feliz": "😊",
        "bem": "😊",

        "triste": "😢",
        "mal": "😟",

        "obrigado": "🙏",
        "obrigada": "🙏",

        "telefone": "📱",
        "celular": "📱",

        "família": "👨‍👩‍👧",
        "familia": "👨‍👩‍👧",

        "frio": "🥶",
        "calor": "🥵",

        "sim": "✅",
        "não": "❌",
        "nao": "❌",
    }

    for palavra, emoji in sugestoes.items():
        if palavra in texto:
            return emoji

    return "💬"


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

        emoji_selecionado.value = sugerir_emoji(frase_digitada)

        page.update()

    campo_frase = ft.TextField(
        label="Palavra ou frase",
        hint_text="Ex.: Estou com fome",
        multiline=False,
        width=450,
        text_size=18,

        color="#1F2937",
        hint_style=ft.TextStyle(
            color="#6B7280"
        ),
        label_style=ft.TextStyle(
            color=COR_PRIMARIA,
            weight=ft.FontWeight.W_600
        ),

        border_color=COR_PRIMARIA,
        focused_border_color="#2563EB",
        cursor_color="#2563EB",

        bgcolor="#FFFFFF",
        border_radius=12,
        filled=True,

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

        adicionar_comunicacao(
            frase=frase,
            emoji=emoji_selecionado.value
        )

        page.navigate("/comunicacao")

    return ft.View(
        route="/adicionar_comunicacao",
        bgcolor=COR_FUNDO,
        padding=20,

        appbar=ft.AppBar(
            title=ft.Text(
                "Adicionar comunicação",
                weight=ft.FontWeight.BOLD
            ),

            leading=ft.IconButton(
                icon=ft.Icons.ARROW_BACK,
                on_click=lambda e: page.navigate("/comunicacao")
            ),

            bgcolor=COR_CARD
        ),

        controls=[
            ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=22,

                controls=[
                    ft.Text(
                        "Adicionar palavra ou frase",
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        color=COR_TEXTO
                    ),

                    campo_frase,

                    ft.Text(
                        "Emoji sugerido",
                        size=18,
                        weight=ft.FontWeight.BOLD,
                        color=COR_TEXTO
                    ),

                    emoji_selecionado,

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
                                on_click=salvar
                            )
                        ]
                    )
                ]
            )
        ]
    )