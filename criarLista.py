even_numbers = list(range(2, 11, 2)) # lista 1
print(even_numbers)


print(len(even_numbers)) # len -> tamanho do array  da lista 1 

#Ranger() funçao 

for _ in range(3):
    print("Olá, mundo!")



frutas = ["maçã", "banana", "cereja"]
for i in range(len(frutas)):
    print(f"O índice {i} corresponde a fruta: {frutas[i]}")


soma_dos_pares = 0
for num in range(0, 11, 2):
    soma_dos_pares += num
print(f"A soma dos números pares de 0 a 10 é: {soma_dos_pares}")



