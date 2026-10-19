# Monitoramento de Níveis de Água

Atividade da **Agenda 11 — Desenvolvimento de Sistemas I**, desenvolvida por **Gabriel Morais Marcondes**, estudante da ETEC.

O programa simula no terminal o enchimento e o esvaziamento de um reservatório. Cada nível apresenta uma mensagem com uma cor específica, utilizando a biblioteca Colorama.

## Níveis do reservatório

| Nível | Situação | Cor |
| --- | --- | --- |
| 1 | Muito baixo (crítico) | Vermelho |
| 2 | Baixo | Amarelo |
| 3 | Médio | Verde |
| 4 | Alto | Ciano |
| 5 | Muito alto (alerta) | Azul |

## Como executar

É necessário ter Python 3.10 ou superior instalado. Abra o terminal na pasta do projeto e execute:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe main.py
```

Se já estiver usando um ambiente Python com as dependências instaladas:

```powershell
python -m pip install -r requirements.txt
python main.py
```

As cores devem ser observadas em um terminal com suporte a cores, como o Windows Terminal ou o terminal do VS Code.

## Funcionamento

- A lista `niveis` armazena as cinco situações do reservatório.
- A função `definir_cor()` retorna a cor de cada nível e rejeita níveis fora do intervalo de 1 a 5.
- A função `exibir_situacao()` mostra o nível e a mensagem correspondente.
- A função `simular_reservatorio()` percorre os níveis de 1 a 5 no enchimento e de 4 a 1 no esvaziamento. O nível 5 não se repete, pois já aparece no final do enchimento.
- `time.sleep()` cria uma pausa de um segundo entre as leituras.
- `Style.RESET_ALL` e `init(autoreset=True)` restauram a formatação padrão do terminal.

Não é necessário digitar dados: os níveis são definidos no código. A simulação termina automaticamente após cerca de nove segundos.

## Exemplo de saída

```text
=== MONITORAMENTO DO RESERVATÓRIO ===

--- ENCHIMENTO ---
Nível 1: Muito baixo (crítico)
Nível 2: Baixo
Nível 3: Médio
Nível 4: Alto
Nível 5: Muito alto (alerta)

--- ESVAZIAMENTO ---
Nível 4: Alto
Nível 3: Médio
Nível 2: Baixo
Nível 1: Muito baixo (crítico)

Simulação finalizada.
```

## Arquivos

- `main.py`: código da simulação.
- `requirements.txt`: dependência externa do projeto.
- `.gitignore`: exclusão de ambientes virtuais e arquivos locais do versionamento.
- `README.md`: documentação e instruções de execução.
