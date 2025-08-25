list_email = ["email_1@gmail.com", "email_2@gmail.com", "email_3@gmail.com", "email_4@gmail.com"]
print(id(list_email))

list = list_email
print(id(list))


#Fazendo um append (adiconando um elemento ao array, faz com que ele mude de id-> que é i numero de referencia da memória.)

list.append("email_5@gmail.com")
print(id(list))
print(list)
print(list[1]) #pega o segundo indice da lsita


sentence = "Learnig Python is fun"
word = sentence.split(" ") #Split separa as palavras
print(word)

emails = "email_1@gmail.com,email_2@gmail.com,email_3@gmail.com,email_4@gmail.com"
L_emails = emails.split(",")
print(L_emails)


#####

L_words = sentence
joined_sentece = "".join(L_words)
print(joined_sentece)


L_words = ["Learnig", "Python", "is", "fun"]
joined_sentece = " ".join(L_words)
print(joined_sentece)

##
#Usando o split
espaco = "espaço e mais espaço"
L_espaco = espaco.split(" ")
print(L_espaco)

#usando o join
espaco_join = L_espaco
joined_espaco = " ".join(espaco_join)
print(joined_espaco)


#inserindo nomes e fazer o split para separar os nomes.
nomes_input = input("Insira nomes separados por espaços: ")
nomes_lista = nomes_input.split()
print(f"Lista antes do join: {nomes_lista}" )

for nome in nomes_lista: #Percorendo a lista com for
    print(f"Olá, {nome}!")


#refatorando em string. com hifen no entres os nomes 
list_nova = " - ".join(nomes_lista)
print(f"Lista depois do join {list_nova}")


palavras_com_espacos = ["     maça", "banana", "maça    ", " banana", "laranja  "]
palavras_unicas = [] #lista vazia

contador = 0 #contador das palavras repedito
for palavra in palavras_com_espacos:
    palavra_lstrip = palavra.strip() #tirando o espaço extra na entrada de dados.
    if palavra_lstrip not in palavras_unicas: #not não in estiver 
        palavras_unicas.append(palavra_lstrip)
    else:
        contador = contador + 1 #conta as palavras repetidos

print(palavras_unicas)
print(f"Palavras repetidas: {contador}")