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



l =  ["milk", "eggs", "breads"]
print(l[0]) # pega a posição do elemento da array
print(l[len(l)-1])# pega  o ultimo elemento

l.append("cheese") #adiciona final da lista 
print(l)


l.insert(2, "bacon") #adiciona em um posicão especifica 
print(l)


m = ["coffe", "sugar", "butter", "cookie"]
print(m)

l.extend(m) # Fazendo uma extend na lista l colcoando uma junção com lsita m

print(l)


#removendo algo a lista. Pop


print(l.pop()) #remove o ultio elemento e retorna o valor 
print(l)

print(l.pop(1)) #remove o elemento na posição especifica 
print(l)


l[1] = "ovo" #modificando a posição 1 da lista l 
print(l)


print("butter" in ["milk", "bread", "eggs", "cheese"])
print("bread" in ["milk", "bread", "eggs", "cheese"])