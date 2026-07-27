import flet as ft

from screens.home import tela_home
from screens.comunicacao import tela_comunicacao
from screens.adicionar_comunicacao import tela_adicionar_comunicacao
from screens.rotina import tela_rotina
from screens.rotina_manha import tela_rotina_manha
from screens.rotina_tarde import tela_rotina_tarde
from screens.rotina_noite import tela_rotina_noite 


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

        elif page.route =="/rotina/manha":
            page.views.append(
                tela_rotina_manha(page)
            )
        
        elif page.route =="/rotina/tarde":
            page.views.append(
                tela_rotina_tarde(page)
            )
        
        elif page.route =="/rotina/noite":
            page.views.append(
                tela_rotina_noite(page)
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