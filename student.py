# Leia uma linha com o númnum = input().strip()
digitos = [int(x) for x in num][::-1]

soma = 0
for i, d in enumerate(digitos):
    if i % 2 == 0:
        soma += d
    else:
        dobro = d * 2
        soma += dobro if dobro < 10 else dobro - 9

print("Cartão válido" if soma % 10 == 0 else "Cartão inválido")
ero do cartão
numero = input()

# TODO: implemente a verificação pelo algoritmo de Luhn
# Siga as dicas do README.

# Ao final, imprima exatamente:
# print("Cartão válido")  ou  print("Cartão inválido")
