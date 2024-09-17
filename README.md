# Sistema Bancário em Python 🐍

Este projeto foi desenvolvido como parte dos desafios de código do Bootcamp DIO, NTT DATA - Engenharia de Dados com Python. Ele oferece uma oportunidade prática de aplicar conceitos de programação em um contexto de software financeiro básico.

### 📍 Introdução

O projeto "Sistema Bancário com Python" é uma aplicação simples que simula operações bancárias fundamentais. Ele foi desenvolvido como uma versão inicial e pode ser expandido para incluir funcionalidades mais complexas no futuro.

### 🎯 Objetivo Geral

O objetivo principal deste projeto é desenvolver um sistema que permita realizar as seguintes operações bancárias:
- Sacar
- Depositar
- Visualizar extrato

### 🚀 Funcionalidades

##### 📌 Depósito
    - Permite realizar depósitos de valores positivos;
    - O sistema é voltado para um único usuário, não sendo necessário identificar o número da agência ou conta bancária (essa funcionalidade será implementada no futuro);
    - Os depósitos são armazenados e exibidos na operação *Extrato*.

### 📌 Saque
    - O sistema permite até 3 saques diários, com um limite máximo de R$ 500,00 por saque;
    - Todos os saques são registrados e exibidos na operação *Extrato*.

### 📌 Extrato
    - Exibe todos os depósitos e saques realizados na conta, fornecendo um histórico completo das transações.

## 📚 Nota Importante
Ao implementar a funcionalidade de registro de transações, foi utilizada a função `.append()` do Python.

    Explicação:
    A função `append()` é um método embutido em Python que permite adicionar elementos a uma lista existente. Ela adiciona o elemento no final da lista, expandindo seu tamanho conforme necessário.
