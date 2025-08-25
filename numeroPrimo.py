def eh_primo(numero):
    """
    Verifica se um número inteiro fornecido é um número primo.

    Um número primo é um número natural maior que 1 que tem exatamente
    dois divisores distintos: 1 e ele mesmo.

    Args:
        numero (int): O número inteiro a ser verificado.

    Returns:
        bool: True se o número for primo, False caso contrário.
    """
    # Passo 1: Tratar os casos especiais.
    # Números primos devem ser maiores que 1.
    if numero <= 1:
        return False
    
    # Passo 2: Percorrer os divisores possíveis.
    # Só precisamos de testar de 2 até à raiz quadrada do número.
    # Usamos int(numero**0.5) para calcular a raiz quadrada e converter para inteiro.
    # Adicionamos +1 porque a função range() exclui o valor final.
    for i in range(2, int(numero**0.5) + 1):
        
        # Passo 3: Verificar se há um divisor exato.
        # Se o resto da divisão de 'numero' por 'i' for 0, encontrámos um divisor.
        if numero % i == 0:
            # Se encontrarmos qualquer divisor, já sabemos que não é primo.
            # Podemos parar a função imediatamente e retornar False.
            return False
            
    # Passo 4: Se o laço terminar...
    # Se o laço 'for' terminar sem nunca encontrar um divisor,
    # significa que o número é primo.
    return True

# --- Exemplos de Uso ---

print(f"O número 7 é primo? Resposta: {eh_primo(7)}")
print(f"O número 10 é primo? Resposta: {eh_primo(10)}")
print(f"O número 97 é primo? Resposta: {eh_primo(97)}")
print(f"O número 1 não é primo. Verificação: {eh_primo(1)}")
print(f"O número 2 é primo. Verificação: {eh_primo(2)}")





# A nossa função eh_primo() definida acima
def eh_primo(numero):
    """Verifica se um número inteiro é primo."""
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Loop principal para interação com o utilizador
while True:
    entrada = input("Digite um número para verificar se é primo (ou 'sair'): ")

    if entrada.lower() == 'sair':
        print("Até à próxima!")
        break

    try:
        num = int(entrada)
        
        # Chama a nossa função e usa o retorno (True/False) para decidir a mensagem
        if eh_primo(num):
            print(f"✔️ Sim, o número {num} é primo!\n")
        else:
            print(f"❌ Não, o número {num} não é primo.\n")
            
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.\n")