import random 

dados = {
    "D4": 4,
    "D6": 6,
    "D8": 8,
    "D10": 10,
    "D12": 12,
    "D20": 20,
}

tipos_de_dados = [
    "D4 -> 4",
    "D6 -> 6",
    "D8 -> 8",
    "D10 ->10",
    "D12 -> 12",
    "D20 -> 20",
]

Dados_existentes= ["D4", "D6", "D8", "D10", "D12", "D20"]

def girar_dado(tipo,quantidade):
    print("Resultado dos giros")
    for i in range(quantidade):
        resultado = random.randint(1, dados[tipo])
        print(f"Rolagem {i+1}: {resultado}")

while True:
    for i in tipos_de_dados:
        print(i)
    while True:
        entrada_tipo = input("Escolha um tipo de Dado dos que foram citados: ").upper()
        if entrada_tipo in Dados_existentes:
            break
        else:
            print("Dado invalido, digite um dos que estão na lista")
    while True:
        try:
            quantidade_vezes = int(input("digite a quantidade de vezes que quer que o dado gire: "))
            break
        except ValueError:
            print("Digite um numero")
    
    girar_dado(entrada_tipo, quantidade_vezes)

    saida= input("deseja ir novamente S para sim ou N para não: ").upper()
    if saida == "S":
        print("saindo...")
        break
    


        