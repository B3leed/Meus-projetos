import random


PERGUNTAS = [
	{
		"texto": "Qual é a capital do Brasil?",
		"alternativas": ["São Paulo", "Brasília", "Rio de Janeiro", "Salvador"],
		"correta": "b",
	},
	{
		"texto": "Qual é a capital da França?",
		"alternativas": ["Paris", "Londres", "Berlim", "Roma"],
		"correta": "a",
	},
	{
		"texto": "Qual é a capital da Itália?",
		"alternativas": ["Roma", "Milão", "Veneza", "Florença"],
		"correta": "a",
	},
	{
		"texto": "Qual linguagem é usada neste jogo?",
		"alternativas": ["Python", "HTML", "CSS", "SQL"],
		"correta": "a",
	},
]


def iniciar_quiz():
	perguntas = PERGUNTAS.copy()
	random.shuffle(perguntas)
	pontos = 0

	print("\n=== Quiz de conhecimentos gerais ===")
	print(f"Você terá {len(perguntas)} perguntas. Boa sorte!\n")

	for numero, pergunta in enumerate(perguntas, start=1):
		print(f"{numero}. {pergunta['texto']}")
		for indice, alternativa in enumerate(pergunta["alternativas"]):
			letra = chr(ord("a") + indice)
			print(f"{letra}) {alternativa}")

		while True:
			resposta = input("Digite a letra da resposta: ").strip().lower()
			if resposta in ("a", "b", "c", "d"):
				break
			print("Resposta inválida. Digite apenas a, b, c ou d.")

		if resposta == pergunta["correta"]:
			pontos += 1
			print("Correto! +1 ponto\n")
		else:
			print(f"Resposta errada. A correta era {pergunta['correta']}.\n")

	print(f"Fim de jogo! Você fez {pontos}/{len(perguntas)} pontos.")
	if pontos == len(perguntas):
		print("Perfeito! Você acertou tudo!")
	elif pontos >= len(perguntas) // 2:
		print("Bom trabalho!")
	else:
		print("Continue praticando!")


while True:
	print("\n=== Jogo de Quiz ===")
	print("1 - Iniciar quiz")
	print("0 - Sair")
	opcao = input("Escolha uma opção: ").strip()

	if opcao == "1":
		iniciar_quiz()
	elif opcao == "0":
		print("Até mais!")
		break
	else:
		print("Opção inválida. Escolha 1 ou 0.")
