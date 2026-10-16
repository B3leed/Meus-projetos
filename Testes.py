 #a=123
#print(a)

# num1 = float(input("Digite um número: "))
# num2 = float(input("Digite outro número: "))
# tipo_de_operacao = input("Digite a operação desejada (+, -, *, /, %, **): ")

# if tipo_de_operacao == "+":
#     Resultado = num1 + num2
# elif tipo_de_operacao == "-":
#     Resultado = num1 - num2
# elif tipo_de_operacao == "*":
#     Resultado = num1 * num2
# elif tipo_de_operacao == "/":
#     Resultado = num1 / num2
# elif tipo_de_operacao == "%":
#     Resultado = num1 % num2
# elif tipo_de_operacao == "**":
#     Resultado = num1 ** num2
# else:
#     print("Operação inválida!")

# print("O resultado da operação é: ", Resultado)


# senha = ('calabreso123')
# tentativa_de_senha = input("Digite a senha: ")
# if tentativa_de_senha != senha:
#     print("acesso negado!")
# else:
#     print("acesso permitido!")

# minhas_tuplas = [("Maçã", "Banana"), ("Verde", "Vermelho")] #uma tupla dentro de uma lista, ou seja, uma lista de tuplas.
# print(minhas_tuplas [1][0])
# if minhas_tuplas [0][0] == "Maçã":
#     print("A primeira fruta é uma Maçã") #uma tupla é imutável, ou seja, não pode ser alterada depois de criada.

# dados = {"nome": "João", "idade": 30, "cidade": "São Paulo"} #um dicionário é uma coleção de pares chave-valor.
# print(dados["nome"]) #acessando o valor da chave "nome"
# print(dados["idade"], "anos") #acessando o valor da chave "idade"
# print(dados["cidade"], 'SP') #acessando o valor da chave "cidade"

# dados = {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo'}
# print(dados['idade'], "anos")  # Acessando o valor da chave 'idade'
# dados['idade'] = 31  # Alterando o valor da chave 'idade'
# print(dados['idade'], "anos")  # Acessando o valor da chave 'idade' após a alteração

# contador = 10
# while contador >= 1:
#     print(f"Contagem: {contador}")
#     contador -= 1
#     if contador == 0:
#         print("Fim da contagem!")

# senha = 123
# tentativa = int(input("Digite a senha: "))# input() retorna uma string, então é necessário converter para int
# if tentativa == senha:
#     print("Acesso permitido!")
# while tentativa != senha: #while é uma estrutura de repetição que executa um bloco de código enquanto uma condição for verdadeira.
#     print("Acesso negado!")
#     tentativa = int(input("Digite a senha: "))
#     if tentativa == senha:
#         print("Acesso permitido!")
#     else:
#         print("Acesso negado!")

# compras = ["maçã", "banana", "laranja", "abacaxi", "melancia"]
# for item in compras:
#     print(f"Item da lista: {item}")

# numeros = [1, 2, 3, 4, 5]
# for numero in numeros:
#     print(f"Número da lista: {numero}")

# numeros = [ 6, 2, 9, 0, 8, 2, 1, 5, 6]
# for numero in numeros:
#  if numero % 2 == 0:
#   break
#  print(numero)

# numeros = [ 6, 2, 9, 0, 8, 2, 1, 5, 6]
# for numero in numeros:
#  if numero % 2 == 0:
#   continue
#  print(numero)

# def ola():
#     print("Ola melhor programador!")
#     tentativa = input('voce e o melhor programador do mundo?')
#     if tentativa == 'sim' or 'Sim':
#         print('voce e o melhor programador do mundo!')
#     else:
#         print('voce nao e o melhor programador do mundo!')
        
# ola()

# import time
# print ("Iniciando o programa...")
# time.sleep(2)  # Pausa por 2 segundos   
# print('pronto para iniciar o programa')


# import random, time

# numero_aleatorio = random.randint(1, 100)  # Gera um número aleatório entre 1 e 100 #em caso de numero quebrado é uniform
# print ('numero gerando aguarde...')
# time.sleep(1)  # Pausa por 1 segundo
# print("Número aleatório gerado:", numero_aleatorio)

# import time, random

# while True:
#     numero_aleatorio = random.randint(1, 50)
#     print(numero_aleatorio)
#     time.sleep(1)  # Pausa por 1 segundo
#     if numero_aleatorio % 2 != 0:
#         print("Número ímpar encontrado! Encerrando o programa.")
#         break

# import time, random

# while True:
#     numero_aleatorio = random.randint(1, 50)
#     print(numero_aleatorio)
#     time.sleep(1)  # Pausa por 1 segundo
#     if numero_aleatorio % 2 == 0:
#         print("Número par encontrado! Encerrando o programa.")
#         break