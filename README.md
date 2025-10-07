# Aplicação de Cálculo de Custos de Cartório

Este projeto consiste em uma aplicação em Python para o cálculo de custos de registro de imóveis, contemplando o registro da compra e venda e o registro da alienação fiduciária. Foi utilizada a biblioteca `pytest` para os testes unitários e o `pytest-cov` para a criação do relatório de cobertura dos testes.

### Funcionalidades

Esta aplicação permite calcular os custos totais para registrar um imóvel e um financiamento através da classe `CalculadoraCustosRegistro`, validando as regras de negócio baseadas em alíquotas e tabelas de emolumentos. O objetivo é garantir que os cálculos sejam precisos e que qualquer alteração seja verificada automaticamente pelos testes.

### Estrutura do projeto



calculadora_custos_cartorio/
│   app_cartorio.py
│   executar_calculo.py
│   requirements.txt
│   .gitignore
│
└───tests/
└───test_app_cartorio.py





Exemplo de uso da classe CalculadoraCustosRegistro:

<img width="1053" height="174" alt="image" src="https://github.com/user-attachments/assets/81146ae6-58f1-4ca5-b915-3b30b4a349cd" />

Sobre os testes

Os testes utilizam a biblioteca pytest junto ao plugin pytest-cov para aferir a cobertura de código da aplicação. Todos os testes estão localizados em calculadora_custos_cartorio/tests/test_app_cartorio.py. Os principais cenários consideram casos de sucesso para diferentes faixas de valores e casos de falha para entradas inválidas.

Regras de Negócio Testadas

    O cálculo de Emolumentos deve seguir a tabela progressiva corretamente.

    O FEPJ (Fundo Especial do Poder Judiciário) corresponde a 20% do valor dos emolumentos.

    O FARPEN (Fundo de Apoio ao Registro de Pessoas Naturais) é uma taxa fixa por ato.

    O ISSQN (Imposto Sobre Serviços de Qualquer Natureza) é calculado com uma alíquota de 5% sobre os emolumentos.

    Valores de imóvel ou financiamento inválidos (negativos ou não numéricos) devem levantar exceções.

    Operações com financiamento de valor zero devem gerar custo zero para o registro do financiamento.

Resultados do pytest-cov

A execução dos testes com o pytest-cov atinge 93% de cobertura de código.

<img width="588" height="259" alt="image" src="https://github.com/user-attachments/assets/ee58030f-335e-4b88-868b-076b514d94b4" />

<img width="1171" height="366" alt="image" src="https://github.com/user-attachments/assets/50955ff0-4767-42fe-95cb-cf9cf3a1799f" />

<img width="1171" height="366" alt="image" src="https://github.com/user-attachments/assets/e8f0c671-041c-4f46-950c-d4cf81dbb0dd" />



Tecnologias e Bibliotecas Utilizadas

Python 3.10+, pytest, pytest-cov

Como instalar e executar

Pré-requisitos: Python 3 e Git instalados.

1. Clone este repositório:
    https://github.com/caioenriquena/QA_VA1_2025

    cd calculadora-custos-cartorio

2. Crie um ambiente virtual e o ative (recomendado):
Bash

# Para macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Para Windows
python -m venv venv
.\venv\Scripts\activate


3. Instale as bibliotecas para teste:

A aplicação principal não precisa de bibliotecas externas, mas os testes sim.
Bash

pip install pytest pytest-cov

4. Para executar a simulação de exemplo:
Bash

python3 executar_calculo.py

5. Para executar os testes e ver o relatório de cobertura:
Bash

python3 -m pytest --cov=app_cartorio

6. Para gerar um relatório de cobertura em HTML:
Bash

python3 -m pytest --cov=app_cartorio --cov-report=html
