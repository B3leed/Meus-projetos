perguntasFacil = [
    {
        'pergunta': 'Qual é o processo pelo qual os seres vivos mudam ao longo do tempo?',
        'opcoes': ['A) Evolução', 'B) Revolução', 'C) Mutação', 'D) Adaptação'],
        'resposta_correta': 'A'
    },
    {
        'pergunta': 'Quem é conhecido como o pai da teoria da evolução?',
        'opcoes': ['A) Isaac Newton', 'B) Charles Darwin', 'C) Albert Einstein', 'D) Gregor Mendel'],
        'resposta_correta': 'B'
    },
    {
        'pergunta': 'Qual é o mecanismo principal da evolução?',
        'opcoes': ['A) Seleção natural', 'B) Gravidade', 'C) Fotossíntese', 'D) Respiração celular'],
        'resposta_correta': 'A'
    }
]
Perguntashard = [
    {
        'pergunta': 'Quem foi o principal líder francês durante as Guerras Napoleônicas?',
        'opcoes': ['A) Luís XVI', 'B) Napoleão Bonaparte', 'C) Carlos X', 'D) Maximilien Robespierre'],
        'resposta_correta': 'B'
    },
    {
        'pergunta': 'Em que ano ocorreu a Batalha de Waterloo?',
        'opcoes': ['A) 1804', 'B) 1812', 'C) 1815', 'D) 1821'],
        'resposta_correta': 'C'
    },
    {
        'pergunta': 'Qual país foi invadido por Napoleão em 1812, em uma campanha que terminou em desastre?',
        'opcoes': ['A) Espanha', 'B) Rússia', 'C) Áustria', 'D) Prússia'],
        'resposta_correta': 'B'
    }
]

import time
import random


def embaralhar_perguntas(perguntas):
    perguntas_embaralhadas = perguntas.copy()
    random.shuffle(perguntas_embaralhadas)
    if len(perguntas_embaralhadas) > 1 and perguntas_embaralhadas == perguntas:
        perguntas_embaralhadas.append(perguntas_embaralhadas.pop(0))
    return perguntas_embaralhadas


def mostrar_ranking():
    try:
        with open('ranking.txt', 'r', encoding='utf-8') as arquivo:
            ranking = []
            for linha in arquivo:
                pontuacao, nome, tempo = linha.strip().split(';')
                ranking.append((int(pontuacao), nome, float(tempo)))
    except FileNotFoundError:
        print('Ainda não há pontuações no ranking.')
        return

    ranking.sort(key=lambda resultado: (-resultado[0], resultado[2]))
    print('\n=== RANKING ===')
    print('Posição | Jogador | Pontos | Tempo')
    print('-----------------------------------')
    for posicao, resultado in enumerate(ranking, start=1):
        pontuacao, nome, tempo = resultado
        print(f'{posicao}º | {nome} | {pontuacao} pontos | {tempo:.2f} segundos')


while True: 
    print('bem vindo ao quiz de evolução')
    print('1. Iniciar quiz')
    time.sleep(1)
    print('2. Ver ranking')
    time.sleep(1)
    print('3. Sair')

    opcao = input('Escolha uma opção: ').strip().lower()

    if opcao == '1':
        print('Iniciando o quiz...')
        time.sleep(1)

        usuario = input('Digite seu nome: ').strip()

        pontuacao = 0
        
        dificuldade = input('Escolha a dificuldade (facil/dificil): ').lower().strip()
        if dificuldade == 'facil':
            print('Você escolheu a dificuldade fácil.')
            print ('Responda as perguntas com a letra correspondente à resposta correta (A, B, C ou D).')
            time.sleep(1)
            perguntas = embaralhar_perguntas(perguntasFacil)
            inicio_contagem = time.perf_counter()
            for pergunta in perguntas:
                print(pergunta['pergunta'])
                for opcao in pergunta['opcoes']:
                    print(opcao)
                resposta = input('Digite sua resposta: ').upper().strip()
                if resposta == pergunta['resposta_correta']:
                    print('Resposta correta!')
                    pontuacao += 100
                else:
                    print('Resposta incorreta.')
                time.sleep(1)
                print('Sua pontuação atual é:', pontuacao)


        elif dificuldade == 'dificil':
            print('Você escolheu a dificuldade difícil.')
            print ('Responda as perguntas com a letra correspondente à resposta correta (A, B, C ou D).')
            time.sleep(1)
            perguntas = embaralhar_perguntas(Perguntashard)
            inicio_contagem = time.perf_counter()
            for pergunta in perguntas:
                print(pergunta['pergunta'])
                for opcao in pergunta['opcoes']:
                    print(opcao)
                resposta = input('Digite sua resposta: ').upper().strip()
                if resposta == pergunta['resposta_correta']:
                    print('Resposta correta!')
                    pontuacao += 250
                else:
                    print('Resposta incorreta.')
                print('Sua pontuação atual é:', pontuacao)
        
        else:
            print('Dificuldade inválida. Escolha facil ou dificil.')
            continue

        tempo_decorrido = time.perf_counter() - inicio_contagem
        print('Quiz finalizado!')
        print('Sua pontuação final foi:', pontuacao)
        print(f'Você demorou {tempo_decorrido:.2f} segundos.')

        with open('ranking.txt', 'a', encoding='utf-8') as arquivo:
            arquivo.write(f'{pontuacao};{usuario};{tempo_decorrido:.2f}\n')

        mostrar_ranking()

    elif opcao == '2':
        mostrar_ranking()

        
    elif opcao == '3':
        print('Saindo do quiz...')
        time.sleep(1)
        break
