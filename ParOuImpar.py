def parOuImpar(n):
 
    if n % 2 == 0:
        print(f"numero par {n}")
    else:
        print(f"Numero Impar {n}")    

   


parOuImpar(30)



def eh_par(n):
    """
    Verifica se um número é par.

    Args:
        n (int): O número a ser verificado.
    
    Returns:
        bool: True se o número for par, False caso contrário.
    """
    return n % 2 == 0

# Como usar:
numero_teste = 50
if eh_par(numero_teste):
    print(f"{numero_teste} é um número par, podemos continuar.")
else:
    print(f"{numero_teste} não é par, operação cancelada.")



def eh_par(n):
    """Verifica se um número é par."""
    return n % 2 == 0

# Loop principal para permitir várias verificações
while True:
    entrada = input("Digite um número para verificar (ou 'sair' para terminar): ")

    if entrada.lower() == 'sair':
        print("Até à próxima!")
        break

    # Tenta converter a entrada para um número inteiro
    try:
        numero = int(entrada)
        
        # Usa a nossa função para decidir a mensagem
        if eh_par(numero):
            print(f"✔️  O número {numero} é PAR.\n")
        else:
            print(f"✔️  O número {numero} é ÍMPAR.\n")
            
    except ValueError:
        # Se o utilizador digitar um texto que não é um número
        print("❌ Entrada inválida. Por favor, digite um número inteiro.\n")