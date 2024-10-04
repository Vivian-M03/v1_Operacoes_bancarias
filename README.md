# Sistema Bancário em Python 🐍

Este projeto foi desenvolvido como parte dos desafios de código do Bootcamp DIO, NTT DATA - Engenharia de Dados com Python. Ele oferece uma oportunidade prática de aplicar conceitos de programação em um contexto de software financeiro básico.

### 📍 Introdução

O projeto "Sistema Bancário com Python" é uma aplicação simples que simula operações bancárias fundamentais. Ele foi atualizado para corrigir erros e aprimorar funcionalidades, permitindo uma experiência mais robusta e funcional.

### 🎯 Objetivo Geral

O objetivo principal deste projeto é desenvolver um sistema que permita realizar as seguintes operações bancárias:
- Sacar
- Depositar
- Visualizar extrato
- Criar novos usuários e contas
- Listar contas

### 🚀 Funcionalidades

##### 📌 Depósito
- Permite realizar depósitos de valores positivos.
- Os depósitos são armazenados e exibidos na operação *Extrato*.
- A entrada do valor do depósito foi corrigida para garantir a conversão correta para um número (`float`), evitando erros ao manipular valores numéricos inseridos como strings.

##### 📌 Saque
- O sistema permite até 3 saques diários, com um limite máximo de R$ 500,00 por saque.
- Todos os saques são registrados e exibidos na operação *Extrato*.
- Assim como no depósito, a entrada do valor do saque foi corrigida para garantir que os valores sejam tratados como números, resolvendo possíveis erros de execução.

##### 📌 Extrato
- Exibe todos os depósitos e saques realizados na conta, fornecendo um histórico completo das transações.
- A função foi corrigida para verificar se o extrato está vazio usando uma string vazia (`""`) em vez de comparar com `'0'`.
- A formatação do saldo foi ajustada para exibir corretamente duas casas decimais com o uso do `.2f`.

##### 📌 Criação de Usuário
- Permite cadastrar um novo usuário no sistema.
- Os dados do usuário incluem nome completo, CPF, data de nascimento e endereço.
- Corrigido um erro onde o CPF não era armazenado corretamente, garantindo que o CPF seja parte do cadastro do usuário.

##### 📌 Criação de Conta
- Permite criar uma nova conta associada a um usuário existente.
- O sistema valida o CPF do usuário antes de criar a conta.
- Corrigido um erro que sobrescrevia a lista de contas em vez de adicionar novas contas corretamente. Agora, as contas são adicionadas de maneira apropriada com o uso de `append()`.

##### 📌 Listagem de Contas
- Permite listar todas as contas criadas no sistema, exibindo os detalhes da conta, como agência, número da conta e nome do titular.

### 📚 Nota Importante
Diversas melhorias foram aplicadas ao projeto para garantir sua funcionalidade correta:

- **Correção de comparações e formatação**: O código foi atualizado para evitar comparações incorretas entre diferentes tipos de dados (ex.: comparar um número com uma string).
  
- **Tratamento de valores numéricos**: A entrada de valores monetários agora é convertida corretamente para `float` antes de qualquer operação, garantindo que os cálculos financeiros sejam realizados sem erros.

- **Uso do `append()`**: Na criação de contas e no registro de transações (depósitos e saques), o método `append()` é utilizado corretamente para adicionar novos dados à lista de contas e ao histórico de transações sem sobrescrever dados existentes.
