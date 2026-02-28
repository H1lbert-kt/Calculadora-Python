import math


def lin():
    print('-' * 40)


def ler_float(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print('Digite apenas números válidos!')


def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b


def divisao(a, b):
    if b == 0:
        print('Não é possível dividir por zero!')
        return None
    return a / b


def potencia(a, b):
    return a ** b


def porcentagem(a, b):
    return (a * b) / 100


def raiz_quadrada(a):
    if a < 0:
        print('Não existe raiz quadrada real de número negativo!')
        return None
    return math.sqrt(a)


def menu():
    lin()
    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('5 - Potência')
    print('6 - Porcentagem')
    print('7 - Raiz Quadrada')
    print('0 - Sair')
    lin()


def main():
    while True:
        menu()

        try:
            opcao = int(input('Escolha uma opção: '))
        except ValueError:
            print('Digite apenas números inteiros!')
            continue

        if opcao == 0:
            print('Saindo...')
            break

        if opcao in [1, 2, 3, 4, 5, 6]:
            n1 = ler_float('Digite o primeiro número: ')
            n2 = ler_float('Digite o segundo número: ')

        if opcao == 1:
            resultado = soma(n1, n2)

        elif opcao == 2:
            resultado = subtracao(n1, n2)

        elif opcao == 3:
            resultado = multiplicacao(n1, n2)

        elif opcao == 4:
            resultado = divisao(n1, n2)

        elif opcao == 5:
            resultado = potencia(n1, n2)

        elif opcao == 6:
            resultado = porcentagem(n1, n2)

        elif opcao == 7:
            n1 = ler_float('Digite o número: ')
            resultado = raiz_quadrada(n1)

        else:
            print('Opção inválida!')
            continue

        if resultado is not None:
            print(f'Resultado: {resultado}')


if __name__ == "__main__":
    main()