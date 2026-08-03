import flet as ft

from screens.home import tela_home
from screens.comunicacao import tela_comunicacao
from screens.adicionar_comunicacao import tela_adicionar_comunicacao
from screens.rotina import tela_rotina
from screens.rotina_manha import tela_rotina_manha
from screens.rotina_tarde import tela_rotina_tarde
from screens.rotina_noite import tela_rotina_noite
from screens.familiares import tela_familiares
from screens.contato import tela_contato
from screens.adicionar_tarefa import tela_adicionar_tarefa

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

        elif page.route == "/rotina/manha":
            page.views.append(
                tela_rotina_manha(page)
            )

        elif page.route == "/rotina/tarde":
            page.views.append(
                tela_rotina_tarde(page)
            )

        elif page.route == "/rotina/noite":
            page.views.append(
                tela_rotina_noite(page)
            )

        elif page.route == "/familiares":
            page.views.append(
                tela_familiares(page)
            )

        elif page.route.startswith("/contato/"):
            tipo_contato = page.route.split("/")[-1]

            page.views.append(
                tela_contato(page, tipo_contato)
            )

        elif page.route.startswith("/rotina/adicionar/"):

            periodo = page.route.split("/")[-1]

            page.views.append(
            tela_adicionar_tarefa(page,periodo)
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
    ft.run(
        main,
        assets_dir="assets"
    )