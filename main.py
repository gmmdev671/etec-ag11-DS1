import time

from colorama import Fore, Style, init


# Inicializa o suporte a cores no terminal.
init(autoreset=True)

# Situações do reservatório, do nível 1 ao 5.
niveis = [
    "Muito baixo (crítico)",
    "Baixo",
    "Médio",
    "Alto",
    "Muito alto (alerta)",
]


def definir_cor(nivel):
    """Retorna a cor correspondente ao nível informado."""
    cores = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE]

    if 1 <= nivel <= len(cores):
        return cores[nivel - 1]

    raise ValueError("O nível deve estar entre 1 e 5.")


def exibir_situacao(nivel):
    """Exibe o nível atual e a situação do reservatório."""
    if not 1 <= nivel <= len(niveis):
        print(Fore.RED + "Erro: nível inválido!" + Style.RESET_ALL)
        return

    situacao = niveis[nivel - 1]
    cor = definir_cor(nivel)
    print(cor + f"Nível {nivel}: {situacao}" + Style.RESET_ALL)


def simular_reservatorio():
    """Simula o enchimento e o esvaziamento do reservatório."""
    intervalo = 1
    print("=== MONITORAMENTO DO RESERVATÓRIO ===")

    print("\n--- ENCHIMENTO ---")
    for nivel in range(1, len(niveis) + 1):
        exibir_situacao(nivel)
        time.sleep(intervalo)

    print("\n--- ESVAZIAMENTO ---")
    # O nível 5 já foi exibido ao final do enchimento.
    for nivel in range(len(niveis) - 1, 0, -1):
        exibir_situacao(nivel)
        time.sleep(intervalo)

    print("\nSimulação finalizada.")
    print(Style.RESET_ALL, end="")


if __name__ == "__main__":
    simular_reservatorio()
