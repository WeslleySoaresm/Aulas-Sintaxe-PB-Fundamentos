def imprimir_invertido_slicing(texto):
    """
    Recebe uma string e imprime a sua versão invertida usando slicing.

    Esta é a forma mais comum e eficiente de inverter uma string em Python.

    Args:
        texto (str): A string a ser invertida.
    """
    string_invertida = texto[::-1]
    print(string_invertida)

# --- Exemplo de Uso ---
print("Usando o método de slicing:")
imprimir_invertido_slicing("Python")
imprimir_invertido_slicing("amor")
imprimir_invertido_slicing("Esta frase será invertida")




def imprimir_invertido_join(texto):
    """
    Recebe uma string e imprime a sua versão invertida usando reversed() e join().

    Esta forma é muito legível e também bastante eficiente.

    Args:
        texto (str): A string a ser invertida.
    """
    string_invertida = "".join(reversed(texto))
    print(string_invertida)

# --- Exemplo de Uso ---
print("\nUsando o método com reversed() e join():")
imprimir_invertido_join("Python")
imprimir_invertido_join("roma")





def imprimir_invertido_loop(texto):
    """
    Recebe uma string e imprime a sua versão invertida usando um laço for.

    Esta é a forma mais didática de entender o algoritmo de inversão.

    Args:
        texto (str): A string a ser invertida.
    """
    string_invertida = ""  # Começamos com uma string vazia
    for caractere in texto:
        # Adiciona o novo caractere NO INÍCIO da string de resultado
        string_invertida = caractere + string_invertida
    
    print(string_invertida)

# --- Exemplo de Uso ---
print("\nUsando o método com o laço for:")
imprimir_invertido_loop("amor")