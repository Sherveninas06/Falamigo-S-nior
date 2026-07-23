import flet as ft

from screens.home import tela_home
from screens.comunicacao import tela_comunicacao
from screens.adicionar_comunicacao import tela_adicionar_comunicacao
from screens.rotina import tela_rotina

def main(page: ft.Page):

    page.title = "Ajudante"
    page.bgcolor = "#F7FAFC"
    page.padding = 0

    def mudar_rota(e=None):

        print(f"Rota atual: {page.route}")

        page.views.clear()

        page.views.append(
            tela_home(page)
        )

        if page.route == "/comunicacao":
            page.views.append(
                tela_comunicacao(page)
            )

        elif page.route == "/adicionar_comunicacao":
            page.views.append(
                tela_adicionar_comunicacao(page)
            )

        elif page.route == "/rotina":
            page.views.append(
                tela_rotina(page)
            )

        page.update()

    def voltar_tela(e):

        if len(page.views) > 1:
            page.views.pop()

        page.navigate(page.views[-1].route)

    page.on_route_change = mudar_rota
    page.on_view_pop = voltar_tela

    page.route = "/"
    mudar_rota()


if __name__ == "__main__":
    ft.run(main)