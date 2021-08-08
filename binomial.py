import math

def combinacao(n, x):
    return math.factorial(n) / (math.factorial(n - x) * math.factorial(x))

def distribuicao_binomial(n, x, p, q):
    return round(combinacao(n, x) * pow(p, x) * pow(q, (n - x)), 4)

def probabilidade_individual():
    n = int(input('Informe o número de observações: '))
    x = int(input('Informe o número de casos de sucesso: '))
    p_percentual = float(input('Digite a probabilidade de sucesso (em percentual, por exemplo, para 90% digite "90"): '))
    p = p_percentual / 100
    q = (100 - p_percentual) / 100
    r = distribuicao_binomial(n, x, p, q)
    r_percentual = r * 100
    print(f'O resultado é: {r:.4f}. Em percentual: {r_percentual:.2f}%')

def probabilidade_acumulada():
    n = int(input('Informe o número de observações: '))
    x = int(input('Informe o número máximo de casos de sucesso: '))
    p_percentual = float(input('Digite a probabilidade de sucesso (em percentual, por exemplo, para 90% digite "90"): '))
    p = p_percentual / 100
    q = (100 - p_percentual) / 100
    r = 0
    i = 0
    while i <= x:
        r += distribuicao_binomial(n, i, p, q)
        i += 1
    r_percentual = r * 100
    print(f'O resultado é: {r:.4f}. Em percentual: {r_percentual:.2f}%')

def menu():
    print('*-------------------------------------------*')
    print('*       Cálculo de fórmula binomial         *')
    print('*-------------------------------------------*')
    print('')
    print('1 - Probabilidade binomial individual')
    print('2 - Probabilidade binomial acumulada')
    print('3 - Sair')
    opcao = int(input("Selecione a opção desejada: "))
    if opcao < 1 and opcao > 3:
        menu()
    return opcao

def main():
    opcao = menu()
    if opcao == 1:
        probabilidade_individual()
    elif opcao == 2:
        probabilidade_acumulada()
    elif opcao == 3:
        print("Programa finalizado")
    else:
        menu()
    
if __name__ == '__main__':
    main()