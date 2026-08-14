import flet_tts

tts = None


def iniciar_tts(page):
    global tts

    if tts is None:
        tts = flet_tts.FletTts()

        page.overlay.append(tts)
        page.update()

    return tts


def falar(page, texto):
    iniciar_tts(page)

    # Para qualquer fala anterior
    tts.parar()

    # Fala o novo texto
    tts.falar(texto)


def parar_voz():
    global tts

    if tts is not None:
        tts.parar()