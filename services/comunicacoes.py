import json
from pathlib import Path


# Caminho do arquivo que armazenará as comunicações
PASTA_DATA = Path(__file__).resolve().parent.parent / "data"
ARQUIVO_COMUNICACOES = PASTA_DATA / "comunicacoes.json"


COMUNICACOES_PADRAO = [
    {"emoji": "✅", "frase": "Sim"},
    {"emoji": "❌", "frase": "Não"},
    {"emoji": "🙏", "frase": "Obrigada"},
    {"emoji": "🤲", "frase": "Por favor"},
    {"emoji": "😊", "frase": "Estou bem"},
    {"emoji": "😟", "frase": "Estou mal"},
    {"emoji": "🔁", "frase": "Repita"},
    {"emoji": "🆘", "frase": "Pode me ajudar?"},
]


def criar_arquivo_inicial():
    """Cria a pasta e o arquivo JSON caso ainda não existam."""

    PASTA_DATA.mkdir(parents=True, exist_ok=True)

    if not ARQUIVO_COMUNICACOES.exists():
        salvar_comunicacoes(COMUNICACOES_PADRAO)


def carregar_comunicacoes():
    """Retorna todas as comunicações salvas."""

    criar_arquivo_inicial()

    try:
        with open(
            ARQUIVO_COMUNICACOES,
            "r",
            encoding="utf-8"
        ) as arquivo:

            return json.load(arquivo)

    except (json.JSONDecodeError, OSError):
        salvar_comunicacoes(COMUNICACOES_PADRAO)
        return COMUNICACOES_PADRAO.copy()


def salvar_comunicacoes(comunicacoes):
    """Salva a lista completa no arquivo JSON."""

    PASTA_DATA.mkdir(parents=True, exist_ok=True)

    with open(
        ARQUIVO_COMUNICACOES,
        "w",
        encoding="utf-8"
    ) as arquivo:

        json.dump(
            comunicacoes,
            arquivo,
            ensure_ascii=False,
            indent=4
        )


def adicionar_comunicacao(frase, emoji):
    """Adiciona uma palavra ou frase nova."""

    frase = frase.strip()

    if not frase:
        return False

    comunicacoes = carregar_comunicacoes()

    nova_comunicacao = {
        "emoji": emoji,
        "frase": frase
    }

    comunicacoes.append(nova_comunicacao)

    salvar_comunicacoes(comunicacoes)

    return True