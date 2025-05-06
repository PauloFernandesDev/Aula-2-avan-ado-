from biblioteca import Pessoa
repetiraluno = True
repetiracao = True
decisao = 0
aluno01 = Pessoa(78, "João Pessoa", 22)
aluno02 = Pessoa(69, "Marcio", 28)

print(f"***************")

while repetiraluno:
    escolha = int(input(f"Escolha o aluno: [1] - {aluno01.nome} [2] - {aluno02.nome}: "))
    match escolha:
        case 1:
            print(f"***************")
            print(f"Nome do aluno: {aluno01.nome}\nIdade: {aluno01.idade}\nPeso: {aluno01.peso}")
            repetiracao = True
            while repetiracao:
                acao = int(input("Escolha uma acão : [1] - Comer, [2] - Falar, [3] - Dormir : "))
                match acao:
                    case 1:
                        comida = input("Escolha qual comida:")
                        aluno01.comer(comida)
                        if aluno02.statusComendo:
                            acaostatus = int(input("Deseja parar de comer [1]-Sim / [2] - Não: "))
                            match acaostatus:
                                case 1 :
                                    aluno01.pararComer()
                                case 2 :
                                    print("Ok!")
                                case _ :
                                    print("Opção inválida!")
                    case 2:
                        aluno01.falar()
                        if aluno02.statusFalando:
                            acaostatus = int(input("Deseja parar de falar [1]-Sim / [2] - Não: "))
                            match acaostatus:
                                case 1 :
                                    aluno01.pararFalar()
                                case 2 :
                                    print("Ok!")
                                case _ :
                                    print("Opção inválida!")
                    case 3:
                        aluno01.dormir()
                        if aluno02.statusDormindo:
                            acaostatus = int(input("Deseja parar de dormir [1]-Sim / [2] - Não: "))
                            match acaostatus:
                                case 1 :
                                    aluno01.pararDormir()
                                case 2 :
                                    print("Ok!")
                                case _ :
                                    print("Opção inválida!")

                    case _:
                        print("Opção inválida!")
                decisao = int(input("Deseja realizar uma nova ação? [1]-Sim / [2]-Não: "))
                if decisao == 2:
                    repetiracao = False
        case 2:
            print(f"***************")
            print(f"Nome do aluno: {aluno02.nome}\nIdade: {aluno02.idade}\nPeso: {aluno02.peso}")
            repetiracao = True
            while repetiracao:
                acao = int(input("Escolha uma acão : [1] - Comer, [2] - Falar, [3] - Dormir : "))
                match acao:
                    case 1:
                        comida = input("Escolha qual comida:")
                        aluno02.comer(comida)
                        if aluno02.statusComendo:
                            acaostatus = int(input("Deseja parar de comer [1]-Sim / [2] - Não: "))
                            match acaostatus:
                                case 1 :
                                    aluno02.pararComer()
                                case 2 :
                                    print("Ok!")
                                case _ :
                                    print("Opção inválida!")


                    case 2:
                        aluno02.falar()
                        if aluno02.statusFalando:
                            acaostatus = int(input("Deseja parar de falar [1]-Sim / [2] - Não: "))
                            match acaostatus:
                                case 1 :
                                    aluno02.pararFalar()
                                case 2 :
                                    print("Ok!")
                                case _ :
                                    print("Opção inválida!")
                    case 3:
                        aluno02.dormir()
                        if aluno02.statusDormindo:
                            acaostatus = int(input("Deseja parar de dormir [1]-Sim / [2] - Não: "))
                            match acaostatus:
                                case 1 :
                                    aluno02.pararDormir()
                                case 2 :
                                    print("Ok!")
                                case _ :
                                    print("Opção inválida!")
                    case _:
                        print("Opção inválida!")
                decisao = int(input("Deseja realizar uma nova ação? [1]-Sim / [2]-Não: "))
                if decisao == 2:
                    repetiracao = False
        case _:
            print("Opção Inválida")
    decisaoaluno = int(input("Deseja selecionar outro aluno? [1]-Sim / [2]-Não: "))
    if decisaoaluno == 2:
        repetiraluno = False