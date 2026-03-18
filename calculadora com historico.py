historico = []
def soma(num1, num2):
    somar = num1 + num2
    return somar

def subtração(num1, num2):
    subtrair = num1 - num2
    return subtrair

def multiplicaçao(num1, num2):
    multiplicar = num1 * num2
    return multiplicar

def divisao(num1, num2):
    dividir = num1 / num2
    return dividir
                    
while True:
    escolha = int(input("soma [1] \n subtração [2] \n multiplicação [3] \n divisão [4] \n acessar hitórico [5]\n limpar histórico[6]\n sair[7]\nqual ação você deseja realizar: "))
    if escolha in [1,2,3,4]:
        num1 = float(input("escolha um número: "))
        num2 = float(input("escolha outro número: "))
        if escolha == 1:
            print(soma(num1, num2))
            historico.append(f"{num1} + {num2} = {soma(num1, num2)}")
            print("-"*30)
        elif escolha == 2:
            print(subtração(num1, num2))
            historico.append(f"{num1} - {num2} = {subtração(num1, num2)}")
            print("-"*30)
        elif escolha == 3: 
            print(multiplicaçao(num1, num2))
            historico.append(f"{num1} * {num2} = {multiplicaçao(num1, num2)}")
            print("-"*30)
        else:
            print(divisao(num1, num2))
            historico.append(f"{num1} / {num2} = {divisao(num1, num2)}")
            print("-"*30)
    elif escolha == 5:
        for c in historico:
            print(c)
            print("-"*30)
    elif escolha == 6:
            historico.clear
            print("historico apagado!")
            print("-"*30)
    elif escolha == 7:
        break
    else:
        print("resposta inválida")
        print("-"*30)