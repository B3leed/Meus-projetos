import time, random
while True:
    print("=== Jogo de Quiz ===")
    print("1 - Iniciar quiz")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '0':
        print("Até mais!")
        break

    elif opcao == '1':
      print("Iniciando o quiz...")
      time.sleep(1)
      print('Bem vindo ao jogo de quiz alfa')
      time.sleep(1)
      print('Você terá 3 perguntas para responder, cada uma com 4 alternativas.')
      time.sleep(1)
      print('Boa sorte!')
      time.sleep(1)
      print('qual é a capital do Brasil?')
      print('a) São Paulo')
      print('b) Brasília')
      print('c) Rio de Janeiro')
      print('d) Salvador')
    resposta1 = input('Digite a letra da alternativa correta: ')
    if resposta1 == 'b':
          print('Parabéns! Você acertou a primeira pergunta.')
    else:
          print('burro pra krl')
    
    time.sleep(1)
    print('qual é a capital da França?')
    print('a) Paris')
    print('b) Londres')
    print('c) Berlim')
    print('d) Roma')
    resposta2 = input('Digite a letra da alternativa correta: ')
    if resposta2 == 'a':
          print('Parabéns! Você acertou a segunda pergunta.')
    else:
          print('burro pra krl')
    
    time.sleep(1)

    print('qual é a capital da Itália?')
    print('a) Roma')
    print('b) Milão')
    print('c) Veneza')
    print('d) Florença')

    resposta3 = input('Digite a letra da alternativa correta: ')
    if resposta3 == 'a':
          
          print('Parabéns! Você acertou a terceira pergunta.')
    else:
          print('burro pra krl')


    print('como voce chegoua te aqui pergunta ultra secret ok?')
    time.sleep(1)
    print('voce vai arrumar um emprego quando?')
    
    time.sleep(1)
    print('a)nunca')
    print('b)jamais kkjk')
    print('c)com 30 anos')
    print('d)emprego oque é isso')
    rpst = input('escolha uma alternativa seu fudido')
    if rpst in ('a','b','c','d'):
        print('seu lixo')
    time.sleep(1)
    print('acabou saporra caralho')