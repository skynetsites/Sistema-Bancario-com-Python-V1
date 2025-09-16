# Desafio: Sistema Bancário em Python V1

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen)

Este projeto faz parte do desafio do curso de Python da DIO. Trata-se de um sistema bancário desenvolvido em Python, que permite realizar operações básicas de conta corrente, como depósitos, saques e consulta de extrato. É um projeto ideal para iniciantes praticarem lógica de programação, loops e estruturas condicionais.

## 💡 Funcionalidades
- **[d] Depositar**: Adicionar valores à conta.  
- **[s] Sacar**: Retirar valores da conta, respeitando limites e saldo disponível.  
- **[e] Extrato**: Visualizar todas as movimentações e o saldo atual.  
- **[q] Sair**: Encerra a aplicação.

## ⚙️ Regras Implementadas
- Limite máximo por saque: **R$ 500,00**  
- Número máximo de saques diários: **3**  
- Depósitos e saques devem ser valores positivos.  
- Histórico de movimentações armazenado em memória (extrato).  

## 🛠 Tecnologias Utilizadas
- Python 3.x  

## 🚀 Como Executar
Clone o repositório, entre no diretório do projeto e execute o script principal:

git clone https://github.com/skynetsites/sistema-bancario-com-python-v1.git  
cd sistema-bancario-com-python-v1  
python sistema_bancario_v1.py  

## 📌 Exemplo de uso no terminal
```text
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> d
Informe o valor do depósito: 1000
Depósito de R$ 1000.00 realizado com sucesso!

=> s
Informe o valor do saque: 200
Saque de R$ 200.00 realizado com sucesso!

=> e
================ EXTRATO =================
Depósito: R$ 1000.00
Saque: R$ 200.00
Saldo: R$ 800.00
==========================================

Desafio concluído! Um projeto prático do curso DIO de Python para você explorar, testar e aprimorar suas habilidades.
