

import re
import sys
import unicodedata

alunos = {} 
contadores_por_curso = {} 


def remover_acentos(txt: str) -> str:
    return unicodedata.normalize("NFKD", txt).encode("ASCII", "ignore").decode()

def extrair_abreviacao(curso: str) -> str:
    if not curso:
        return "CUR"
    curso_up = curso.strip().upper()

    if "-" in curso_up:
        tail = curso_up.split("-")[-1].strip()
        if re.fullmatch(r"[A-Z]{2,6}", tail):
            return tail

    if re.fullmatch(r"[A-Z]{2,6}", curso_up):
        return curso_up

    s = remover_acentos(curso_up)
    letras = re.sub(r"[^A-Z]", "", s)
    return (letras[:3] or "CUR")

def gerar_matricula(abrev: str) -> str:
    abrev = abrev.upper()
    ultimo = contadores_por_curso.get(abrev, 0) + 1
    contadores_por_curso[abrev] = ultimo
    return f"{abrev}{ultimo}"

def email_existe(email: str) -> bool:
    email = email.strip().lower()
    for registro in alunos.values():
        if registro["email"].lower() == email:
            return True
    return False

def encontrar_por_email(email: str):
    email = email.strip().lower()
    for mat, registro in alunos.items():
        if registro["email"].lower() == email:
            return mat, registro
    return None, None

def imprimir_linha_aluno(matricula: str, registro: dict):
    print(f"{matricula:<8} | {registro['nome']:<25} | {registro['email']:<30} | {registro['curso']}")

def pausar():
    input("\nPressione ENTER para continuar...")


def cadastrar_aluno():
    print("\n=== Cadastrar Aluno ===")
    nome = input("Nome: ").strip()
    email = input("E-mail: ").strip()
    curso = input("Curso (ex.: 'Engenharia de Software - GES' ou 'GES'): ").strip()

    if not nome or not email or not curso:
        print("Erro: todos os campos são obrigatórios.")
        return

    if email_existe(email):
        print("Erro: já existe um aluno cadastrado com esse e-mail.")
        return

    abrev = extrair_abreviacao(curso)
    matricula = gerar_matricula(abrev)

    alunos[matricula] = {
        "nome": nome,
        "email": email,
        "curso": curso,
        "abrev": abrev,
    }
    print(f"Aluno cadastrado com sucesso! Matrícula: {matricula}")

def listar_alunos():
    print("\n=== Lista de Alunos ===")
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    print(f"{'Matr.':<8} | {'Nome':<25} | {'E-mail':<30} | Curso")
    print("-" * 85)
    for matricula, registro in alunos.items():
        imprimir_linha_aluno(matricula, registro)

def atualizar_aluno():
    print("\n=== Atualizar Aluno ===")
    chave = input("Informe a matrícula OU e-mail do aluno: ").strip()


    registro = alunos.get(chave)
    matricula = chave if registro else None


    if not registro:
        matricula, registro = encontrar_por_email(chave)

    if not registro:
        print("Aluno não encontrado.")
        return

    print("Deixe em branco para manter o valor atual.")
    novo_nome = input(f"Novo nome [{registro['nome']}]: ").strip() or registro["nome"]
    novo_email = input(f"Novo e-mail [{registro['email']}]: ").strip() or registro["email"]
    novo_curso = input(f"Novo curso [{registro['curso']}]: ").strip() or registro["curso"]


    if novo_email.lower() != registro["email"].lower() and email_existe(novo_email):
        print("Erro: já existe um aluno com esse e-mail.")
        return


    curso_mudou = (novo_curso.strip() != registro["curso"].strip())
    if curso_mudou:
        print("\nO curso foi alterado. A matrícula segue o padrão <ABREV><N>.")
        resp = input("Deseja gerar uma NOVA matrícula para o novo curso? (s/N): ").strip().lower()
        if resp == "s":
            nova_abrev = extrair_abreviacao(novo_curso)
            nova_matricula = gerar_matricula(nova_abrev)
        
            del alunos[matricula]
            alunos[nova_matricula] = {
                "nome": novo_nome,
                "email": novo_email,
                "curso": novo_curso,
                "abrev": nova_abrev,
            }
            print(f"Aluno atualizado com sucesso! Nova matrícula: {nova_matricula}")
            return
        else:
            print("Mantendo a matrícula antiga.")


    registro["nome"] = novo_nome
    registro["email"] = novo_email
    registro["curso"] = novo_curso
    print("Aluno atualizado com sucesso!")

def remover_aluno():
    print("\n=== Remover Aluno ===")
    chave = input("Informe a matrícula OU e-mail do aluno a remover: ").strip()


    if chave in alunos:
        del alunos[chave]
        print("Aluno removido com sucesso!")
        return


    matricula, registro = encontrar_por_email(chave)
    if registro:
        del alunos[matricula]
        print("Aluno removido com sucesso!")
    else:
        print("Aluno não encontrado.")


def menu():
    while True:
        print("\nMenu de Opções")
        print("1. Cadastrar Aluno")
        print("2. Listar Alunos")
        print("3. Atualizar Aluno")
        print("4. Remover Aluno")
        print("5. Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_aluno()
            pausar()
        elif opcao == "2":
            listar_alunos()
            pausar()
        elif opcao == "3":
            atualizar_aluno()
            pausar()
        elif opcao == "4":
            remover_aluno()
            pausar()
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")
            pausar()

def main():
    try:
        menu()
    except KeyboardInterrupt:
        print("\nEncerrado pelo usuário.")
        sys.exit(0)

if __name__ == "__main__":
    main()
