op = "soma"

#condicões
match op:
    case "soma":
        print(5 + 3)
    case "subtrai":
        print(5 - 3)
    case "multiplica":
        print(5 * 3)
    case "divide":
        print(5 / 3)
    case _:
        print("Operação inválida")