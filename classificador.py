#DADOS
rodas = int(input("Quantidade de rodas: "))
peso = float(input("Peso bruto em kg: "))
pessoas = int(input("Quantidade de pessoas: "))

if rodas <= 3:
    print("A melhor categoria é: A")
elif peso <= 3500 and pessoas <= 8:
    print("A melhor categoria é: B")
elif peso > 6000:
    print("A melhor categoria é: E")
elif peso > 3500 and peso <= 6000:
    print("A melhor categoria é: C")
else: # Se chegou aqui, sobrou apenas a condição de mais de 8 pessoas
    print("A melhor categoria é: D")
