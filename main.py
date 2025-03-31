cor_do_sinal= input("Qual a cor do sinal? ")

match cor_do_sinal:
    case "vermelho":
        print("PARE!")
    case "amarelo":
        print("ATENÇÃO!")
    case "verde":
        print("SIGA!")
    case _:
        print("Cor inválida!")