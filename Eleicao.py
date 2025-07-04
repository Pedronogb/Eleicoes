class Candidato:
    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero
        self.votos = 0
    def __str__(self):
        return f"Candidato: {self.nome} | Número: {self.numero}"

candidatos = []
senha = 1234

def menu():
    print("########## ELEIÇÕES 2026 ##########")
    print()
    print("1 - Cadastrar Candidato")
    print("2 - Votar")
    print("3 - Mostrar resultado da eleição")
    print("0 - Sair")

def cadastrar_candidato():
    s = int(input("Digite a senha: "))
    if s == senha:
        try:
            nome = input("\nNome do candidato: ")
            if not nome:
                raise ValueError("Nome não pode estar vazio!")

            numero_str = input("Número do candidato: ")
            if not numero_str:
                raise ValueError("Número não pode estar vazio!")

            numero = int(numero_str)

            for c in candidatos:
                if c.numero == numero:
                    raise ValueError("Já existe um candidato com esse número!")

            candidato = Candidato(nome, numero)
            candidatos.append(candidato)
            print("Candidato cadastrado com sucesso!")

        except ValueError as erro:
            print("❌ Erro ao cadastrar: ", erro)

    else:
        print("Senha Incorreta!")
        return

def votar():
    if not candidatos:
        print("Nenhum candidato cadastrado ainda!")
        return

    try:
        voto = int(input("\nDigite o número do candidato: "))
        for candidato in candidatos:
            if voto == candidato.numero:
                candidato.votos += 1
                print(f"Voto confirmado: {candidato.nome}")
                return candidato
        print("Candidato não encontrado!")
    except ValueError:
        print("Digite um número válido!")

def mostrar_resultado():
    s = int(input("\nDigite a senha: "))
    if s == senha:
        for candidato in candidatos:
            print (f"{candidato.nome} ({candidato.numero}) - {candidato.votos} voto(s)")
        e = input("Encerrar votação? ").lower()
        if e == "sim":
            if all(c.votos == 0 for c in candidatos):
                print("\n🟡 Nenhum voto foi registrado ainda.")
                return

                # Descobre o maior número de votos
            vencedor = max(candidatos, key=lambda c: c.votos)
            empatados = [c for c in candidatos if c.votos == vencedor.votos]

            if len(empatados) > 1:
                print("\n⚠️ Houve um EMPATE entre os seguintes candidatos:")
                for c in empatados:
                    print(f"- {c.nome} ({c.numero}) com {c.votos} voto(s)")
            else:
                print(f"\n🎉 VENCEDOR: {vencedor.nome} ({vencedor.numero}) com {vencedor.votos} voto(s)!")
        elif e == "não":
            print("Votação continua.")
        else:
            print("Opção inválida!")
    else:
        print("Senha Incorreta!")
        return

while True:
    menu()
    try:
        opcao = int(input("Digite uma opção: "))
        if opcao == 1:
            cadastrar_candidato()
        elif opcao == 2:
            votar()
        elif opcao == 3:
            mostrar_resultado()
        elif opcao == 0:
            print("\nSaindo dessa bomba!")
            break
        else:
            print("Opção inválida!")
    except ValueError:
        print("Erro: Digite apenas números!")











