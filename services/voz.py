import queue
import threading

import pyttsx3


# Guarda as frases que ainda precisam ser faladas
_fila_de_fala = queue.Queue()


def falar(texto: str) -> None:
    """
    Adiciona uma frase à fila de voz.
    """

    texto = texto.strip()

    if not texto:
        return

    _fila_de_fala.put(texto)


def selecionar_voz_portugues(motor) -> None:
    """
    Procura uma voz em português instalada no Windows.
    Caso não encontre, usa a voz padrão.
    """

    vozes = motor.getProperty("voices")

    for voz in vozes:
        informacoes = (
            f"{voz.id} "
            f"{getattr(voz, 'name', '')} "
            f"{getattr(voz, 'languages', '')}"
        ).lower()

        if (
            "portuguese" in informacoes
            or "português" in informacoes
            or "brazil" in informacoes
            or "brasil" in informacoes
            or "pt-br" in informacoes
        ):
            motor.setProperty("voice", voz.id)
            break


def processar_falas() -> None:
    """
    Processa uma frase por vez.
    Cria um novo motor para cada reprodução.
    """

    while True:
        texto = _fila_de_fala.get()

        motor = None

        try:
            motor = pyttsx3.init()

            motor.setProperty("rate", 155)
            motor.setProperty("volume", 1.0)

            selecionar_voz_portugues(motor)

            motor.say(texto)
            motor.runAndWait()

        except Exception as erro:
            print(f"Erro ao reproduzir a voz: {erro}")

        finally:
            if motor is not None:
                try:
                    motor.stop()
                except Exception:
                    pass

            _fila_de_fala.task_done()


_thread_de_voz = threading.Thread(
    target=processar_falas,
    daemon=True
)

_thread_de_voz.start()