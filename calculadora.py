import math

#definir funções

def lin():
    print('-' * 30)

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b 

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
        return a / b
    
def potencia(a, b):
    return a ** b

def porcentagem(a, b):
    return (a * b) / 100

def raiz(a):
    return math.sqrt(a)
    
#definir estrutura de repetição

while True:
    lin()
    lin()
    print('1 - soma')
    print('2 - subtração')
    print('3 - multiplicação')
    print('4 - divisão')
    print('5 - potência')
    print('6 - porcentagem')
    print('7 - raiz quadrada')
    print('0 - sair')
    lin()
    lin()

#tratamento de erros

    try:
        opcao = int(input('Qual opção você escolhe? '))
    except ValueError:
        print('Apenas números!!')
        continue

    if opcao > 7:
        print('Errado, reeleia as opções.')
        continue
    elif opcao < 0:
        print('Errado, reeleia as opções.')
        continue

    if opcao == 0:
            print('saindo....')
            break
    
    if opcao == 7:
        try:
            r1 = float(input('Escolha um número: '))
        except ValueError:
            print('Apenas números!!')
            continue
        if r1 < 0:
            print('Errado, número negativo!')
            continue
        else:
            print('RESULTADO:',raiz(r1))
            continue

    try:
        s1 = float(input('Digite o primeiro número: '))
        s2 = float(input('Digite outro número: '))
    except ValueError:
        print('Apenas números!!')
        continue
    
    


#Definindo operações nas escolhas
    
    if opcao == 1:
        print('RESULTADO',soma(s1, s2)
          )

    elif opcao == 2:
        print('RESULTADO',subtracao(s1, s2)
          )

    elif opcao == 3:
        print('RESULTADO',multiplicacao(s1, s2)
              )

    elif opcao == 4:
        try:
            r1 = divisao(s1, s2)
            print('RESULTADO:',r1)
        except ZeroDivisionError:
            print('Erro, divisão por zero!!')

    elif opcao == 5:
        print('RESULTADO',potencia(s1, s2))
    
    elif opcao == 6:
        print('RESULTADO',porcentagem(s1, s2))