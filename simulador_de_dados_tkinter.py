import random
import tkinter as tk
from tkinter import ttk

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
    resultados =[]
    for i in range(quantidade):
        resultado = random.randint(1, dados[tipo])
        resultados.append(f"Rolagem {i+1}: {resultado}")
    
    label_resultado_final.config(text=f"\n".join(resultados))


def girar_os_dados():
    entrada_tipo= escolha_tipo.get()
    entrada_quantidade_giros = int(entrada_quantidade.get())

    girar_dado(entrada_tipo, entrada_quantidade_giros)

janela=tk.Tk()
janela.title("Simulador de dados")
janela.geometry("500x300")

label_escolha_tipo = tk.Label(janela, text="## Escolha o tipo de dado: ")
label_escolha_tipo.grid(row=0, column=0, padx=5, pady=5)

escolha_tipo =ttk.Combobox(janela,
    values=["D4",
    "D6",
    "D8",
    "D10",
    "D12",
    "D20"])
escolha_tipo.grid(row=1, column=0, padx=5, pady=5)
escolha_tipo.current(0)

label_escolha_quantidade = tk.Label(janela, text="## Escolha a quantidade de vezes que o dado vai ser girado: ")
label_escolha_quantidade.grid(row=0, column=1, padx=5, pady=5)

entrada_quantidade=tk.Entry(janela)
entrada_quantidade.grid(row=1, column=1, padx=5, pady=5)

botao_girar=tk.Button(janela,text="Girar",width= 20, command=girar_os_dados)
botao_girar.grid(row=2, column=0, columnspan=2, pady=5)


label_resultado_final=tk.Label(janela,text="")
label_resultado_final.grid(row=3, column=0, columnspan=2, pady=5)

janela.mainloop()