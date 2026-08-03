import json
import os


PASTA_PROJETO = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

CAMINHO_ARQUIVO = os.path.join(
    PASTA_PROJETO,
    "data",
    "rotinas.json"
)


ROTINAS_PADRAO = {
    "manha": [
        {
            "tarefa": "Higiene matinal",
            "concluida": False
        },
        {
            "tarefa": "Arrumar a cama",
            "concluida": False
        },
        {
            "tarefa": "Café da manhã",
            "concluida": False
        },
        {
            "tarefa": "Remédios",
            "concluida": False
        },
        {
            "tarefa": "Caminhada ou exercício",
            "concluida": False
        }
    ],

    "tarde": [
        {
            "tarefa": "Almoçar",
            "concluida": False
        },
        {
            "tarefa": "Novela da tarde",
            "concluida": False
        },
        {
            "tarefa": "Ler um livro",
            "concluida": False
        },
        {
            "tarefa": "Cuidar da horta",
            "concluida": False
        }
    ],

    "noite": [
        {
            "tarefa": "Jantar",
            "concluida": False
        },
        {
            "tarefa": "Novela da Noite",
            "concluida": False
        },
        {
            "tarefa": "Ler um livro",
            "concluida": False
        },
        {
            "tarefa": "remédios",
            "concluida": False
        },
        {
            "tarefa": "Higiene noturna",
            "concluida": False
        }
    ]
}


def salvar_rotinas(rotinas):

    pasta_data = os.path.dirname(CAMINHO_ARQUIVO)

    os.makedirs(
        pasta_data,
        exist_ok=True
    )

    with open(
        CAMINHO_ARQUIVO,
        "w",
        encoding="utf-8"
    ) as arquivo:

        json.dump(
            rotinas,
            arquivo,
            ensure_ascii=False,
            indent=4
        )


def carregar_rotinas():

    print("\n--- TESTE DA ROTINA ---")
    print("Arquivo procurado:", CAMINHO_ARQUIVO)
    print("Arquivo existe:", os.path.exists(CAMINHO_ARQUIVO))

    if not os.path.exists(CAMINHO_ARQUIVO):

        print("O arquivo não existia. Criando rotinas.json...")

        salvar_rotinas(ROTINAS_PADRAO)

        return ROTINAS_PADRAO

    try:
        with open(
            CAMINHO_ARQUIVO,
            "r",
            encoding="utf-8"
        ) as arquivo:

            rotinas = json.load(arquivo)

        print("Dados encontrados:", rotinas)

        if "manha" not in rotinas:
            print("A chave 'manha' não foi encontrada.")

            rotinas["manha"] = ROTINAS_PADRAO["manha"]
            salvar_rotinas(rotinas)

        return rotinas

    except json.JSONDecodeError as erro:

        print("ERRO NO JSON:", erro)
        print("O arquivo será recriado.")

        salvar_rotinas(ROTINAS_PADRAO)

        return ROTINAS_PADRAO

    except Exception as erro:

        print("ERRO INESPERADO:", erro)

        return ROTINAS_PADRAO


def obter_rotina(periodo):

    rotinas = carregar_rotinas()

    tarefas = rotinas.get(periodo, [])

    print("Período solicitado:", periodo)
    print("Quantidade de tarefas:", len(tarefas))
    print("-----------------------\n")

    return tarefas


def atualizar_tarefa(
    periodo,
    indice,
    concluida
):

    rotinas = carregar_rotinas()

    if periodo not in rotinas:
        return False

    if indice < 0 or indice >= len(rotinas[periodo]):
        return False

    rotinas[periodo][indice]["concluida"] = concluida

    salvar_rotinas(rotinas)

    return True

def adicionar_tarefa(periodo, nome_tarefa):

    nome_tarefa = nome_tarefa.strip()

    if not nome_tarefa:
        return False

    rotinas = carregar_rotinas()

    if periodo not in rotinas:
        rotinas[periodo] = []

    nova_tarefa = {
        "tarefa": nome_tarefa,
        "concluida": False
    }

    rotinas[periodo].append(nova_tarefa)

    salvar_rotinas(rotinas)

    return True

def excluir_tarefa(periodo, indice):

    rotinas = carregar_rotinas()
    
    if periodo not in rotinas:
        return False

    if indice < 0 or indice >= len(rotinas[periodo]):
        return False

    rotinas[periodo].pop(indice)

    salvar_rotinas(rotinas)

    return True