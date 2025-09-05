## [Voltar ao início](../../README.md)

# Exercício Prática 1 - Introdução ao Python

## Objetivo

O objetivo deste exercício é aplicar os conceitos básicos de Python abordados na revisão, incluindo variáveis, tipos de dados, estruturas de controle e funções.

## Descrição do Problema

Desenvolva um programa básico em Python que rode no terminal e permita realizar um CRUD (Create, Read, Update, Delete) de alunos em uma faculdade.

Cada aluno deve possuir os seguintes atributos:

- Nome
- E-mail
- Curso (GES, GEC, GEA, etc.)
- Matrícula (gerada automaticamente com base no curso)

A matrícula deve ser composta pelo nome do curso (ou uma abreviação) seguido de um número sequencial. Exemplo:

- Aluno cadastrado no curso de **Engenharia de Software - GES** pode ter a matrícula **GES1**, **GES2**, etc.

## Requisitos

1. **Funções:**
   - O programa deve ser modularizado, com cada funcionalidade implementada em uma função separada.
2. **Estrutura de Dados:**

   - O programa deve usar uma lista ou um dicionário para armazenar as informações dos alunos.

3. **Interação com o Usuário:**
   - O programa deve interagir com o usuário através de um menu no terminal, permitindo que ele escolha entre as opções disponíveis.

## Exemplo de Solução usando Professores

### OBS: Este é apenas um exemplo. Seu programa deve implementar o CRUD para alunos:

```python
professores = []

def cadastrar_professor():
    nome = input("Digite o nome do professor: ")
    email = input("Digite o e-mail do professor: ")
    sala_de_atendimento = input("Digite a sala de atendimento do professor: ")
    professores.append({"nome": nome, "email": email, "sala_de_atendimento": sala_de_atendimento})
    print(f"Professor {nome} cadastrado com sucesso!")

def listar_professores():
    if not professores:
        print("Nenhum professor cadastrado.")
    else:
        for professor in professores:
            print(f"Nome: {professor['nome']}, E-mail: {professor['email']}, Sala: {professor['sala_de_atendimento']}")

def atualizar_professor():
    nome = input("Digite o nome do professor a ser atualizado: ")
    for professor in professores:
        if professor["nome"] == nome:
            professor["email"] = input("Digite o novo e-mail: ")
            professor["sala_de_atendimento"] = input("Digite a nova sala de atendimento: ")
            print("Professor atualizado com sucesso!")
            return
    print("Professor não encontrado.")

def remover_professor():
    nome = input("Digite o nome do professor a ser removido: ")
    for professor in professores:
        if professor["nome"] == nome:
            professores.remove(professor)
            print("Professor removido com sucesso!")
            return
    print("Professor não encontrado.")

def main():
    while True:
        print("\nMenu de Opções:")
        print("1. Cadastrar Professor")
        print("2. Listar Professores")
        print("3. Atualizar Professor")
        print("4. Remover Professor")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_professor()
        elif opcao == '2':
            listar_professores()
        elif opcao == '3':
            atualizar_professor()
        elif opcao == '4':
            remover_professor()
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
```

## Entrega

- **Execução:** Rode o arquivo `sistema_faculdade.py` no terminal e execute as seguintes instruções:

  - Cadastrar pelo menos 3 alunos.
  - Listar os alunos cadastrados.
  - Atualizar um aluno cadastrado.
  - Remover um aluno cadastrado.
  - Listar os alunos novamente para verificar se a remoção foi feita corretamente.

- **Formato:** Envie o link para o seu repositório no GitHub contendo o arquivo `sistema_faculdade.py` e um arquivo `logs.txt` com a saída do programa.

- **Critérios de Avaliação:**
  - Corretude do código.
  - Uso adequado das estruturas de controle e funções.
  - Implementação da lógica de gerenciamento de alunos utilizando listas ou dicionários.
  - Clareza e organização do código.

Boa sorte e mãos à obra!

---

[Voltar ao início](../../README.md)
