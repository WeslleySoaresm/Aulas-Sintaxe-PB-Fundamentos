def calculate_total (price,  percent):
    """calcular o preço da conta incluido a gorjeta

    Args:
        price (_type_): _description_
        percent (_type_): _description
    """


    total = price + (price * percent)
    return total

price = 20
percent = 0.10
total_price = calculate_total(price, percent)

print (f"valor total da conta: R${total_price}")

#função que não retorna nada, apenas executa o bloco de codigo.
#função que se comporta como procedimento, que não tem return 


def imprimir_numeros(n): # n é o parametro que colocamos na linha 34
    for i in range(1, n +1):
        print(i)


#chamando a função e impressão do resultado

numero = 5

print(f"Números de 1 até {numero}")

#instanciando a função(chamando a função)

imprimir_numeros(numero)



def contar_ocorrencias(string, caractere):
    contador = 0
    for char in string:
        if char == caractere:
            contador += 1
    return contador


texto = "programção em python"
caractere_procurado = "a"
resultado = contar_ocorrencias(texto, caractere_procurado)
print(f"o caractere '{caractere_procurado}' parece {resultado} vezes na string")