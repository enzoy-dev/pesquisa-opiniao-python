# Pesquisa de opinião - TudoWeb

TOTAL_ENTREVISTADOS = 10  

excelente = 0
ruim = 0

for i in range(1, TOTAL_ENTREVISTADOS + 1):
    print(f"\nEntrevistado {i}")

    nome = input("Nome: ")
    idade = int(input("Idade: "))

    print("1 - Excelente")
    print("2 - Bom")
    print("3 - Ruim")

    opiniao = int(input("Opinião: "))

    if opiniao == 1:
        excelente += 1
    elif opiniao == 3:
        ruim += 1
    elif opiniao != 2:
        print("Opinião inválida!")

print("\n===== RESULTADO DA PESQUISA =====")
print(f"Quantidade de EXCELENTE: {excelente}")
print(f"Quantidade de RUIM: {ruim}")