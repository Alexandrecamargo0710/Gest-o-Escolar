import re
import os

Dados = {}
Opção = ""

def Limpar_Terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def Menu ():
    global Opção
    print("\n--- SISTEMA DE GESTÃO ESCOLAR ---")
    print("0. Adicionar aluno")
    print("1. Adicionar nota")
    print("2. Remover aluno e notas")
    print("3. Remover nota")
    print("4. Listar alunos e notas")
    print("5. Sair")
    
    # Pega a opção, remove espaços em branco e a torna minúscula para consistência
    Opção = input("Escolha a opção: ").strip()

def Adicionar_aluno ():
    Limpar_Terminal ()
    while True:
        Aluno = input("Digite o nome do aluno: ").strip().title()
        Aluno = re.sub(r'[^A-Za-zÀ-ÿ\s]', '', Aluno).strip()
        if not Aluno:
            Limpar_Terminal ()
            print("Nome do aluno não pode ser vazio.")
            continue

        elif Aluno in Dados:
            print(f"ERRO: O aluno '{Aluno}' já está cadastrado.")
            return

        else:
            Dados[Aluno] = []
            print(f"✅ Aluno '{Aluno}' adicionado com sucesso.")
            break

def Adicionar_nota ():
    Limpar_Terminal ()
    while True:
        if not Dados:
            print("Nenhum aluno cadastrado. Adicione um aluno primeiro (Opção 0).")
            break
        Aluno = input("Selecione um aluno: ").strip().title()

        if Aluno in Dados:
            try: 
                Nota_str = input(f"Digite uma nota ao {Aluno}: ").replace(",", ".")
                Nota = float(Nota_str)
                if 0 <= Nota <= 10:
                    Dados[Aluno].append(Nota)
                    Limpar_Terminal ()
                    print(f"✅ Nota {Nota} ao '{Aluno}' adicionado com sucesso.")
                    break
                else:
                    Limpar_Terminal ()
                    print("A nota deve ser maior ou igual a 0 e menor que 10")
                    continue
            except ValueError:
                Limpar_Terminal ()
                print("Valor inválido")
                continue
        else:
            Limpar_Terminal ()
            print("Aluno não encontrado")
            continue

def Remover_alunoEnotas ():
    Limpar_Terminal ()
    if not Dados:
        Limpar_Terminal ()
        print("Nenhum aluno cadastrado. Adicione um aluno primeiro (Opção 0).")
    else:
        Aluno = input("Digite o aluno que queira remover: ").strip().title()
        if Aluno in Dados:
            Confirmar = input(f"Tem certeza que deseja apagar {Aluno} e suas notas? S/N: ").strip().upper()
            if Confirmar == "S":
                del Dados[Aluno]
                print(f"✅ Aluno '{Aluno}' e suas notas removidos com sucesso.")
            else:
                print("Operação cancelada!")
        else:
            print("Aluno não encontrado")

def Remover_nota():
    Limpar_Terminal ()
    if not Dados:
        Limpar_Terminal ()
        print("Nenhum aluno cadastrado. Adicione um aluno primeiro (Opção 0).")
        return

    Aluno = input("Digite o aluno que queira remover a nota: ").strip().title()
    if Aluno in Dados:
        Notas = Dados[Aluno]
        
        if not Notas:
            print(f"{Aluno} não tem notas cadastradas") 
            return
        
        print(f"\nNotas de {Aluno}:")
        for i, nota in enumerate(Notas):
            print(f"[{i}] - Nota: {nota}")

        try:
            indice_str = input("Digite o ÍNDICE da nota que deseja remover (o número entre colchetes, ex: 0): ")
            indice = int(indice_str)
            
            if 0 <= indice < len(Notas):
                nota_removida = Notas.pop(indice)
                print(f"✅ Nota {nota_removida} removida de {Aluno}.")
            else:
                print("ERRO: Índice de nota inválido.")
        except ValueError:
            print("ERRO: Entrada inválida. Por favor, digite um número inteiro para o índice.")
    else:
        print(f"ERRO: Aluno '{Aluno}' não encontrado.")

def Listar ():
    Limpar_Terminal ()
    if not Dados:
        print("Nenhum aluno cadastrado. Adicione um aluno primeiro (Opção 0).")
    else:
       print("\n📋 LISTA DE ALUNOS E NOTAS:")
       for Aluno, Notas in Dados.items():
            if Notas:
                Media = sum(Notas) / len(Notas)
                print(f"\n👤 Aluno: {Aluno}, Nota: {Notas} | Média = {Media:.1f}")
            else:
                print(f"\n👤 {Aluno}: Nenhuma nota cadastrada.")
            print("-" * 40)
    input("\nPressione enter para sair...")

while Opção != "5":
    Menu()
    if Opção == "0":
        Adicionar_aluno ()
    elif Opção == "1":
        Adicionar_nota ()
    elif Opção == "2":
        Remover_alunoEnotas ()
    elif Opção == "3":
        Remover_nota ()
    elif Opção == "4":
        Listar ()
    elif Opção == "5":
        print("👋 Saindo do sistema. Até mais!")
        break
    else:
        if Opção.strip() != "":
            Limpar_Terminal ()
            print("❌ Opção inválida. Por favor, escolha uma opção entre 0 e 5.")