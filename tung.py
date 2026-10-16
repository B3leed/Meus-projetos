while True:
	print("=== Calculadora ===")
	print("1 - Somar")
	print("2 - Subtrair")
	print("3 - Multiplicar")
	print("4 - Dividir")
	print("5 - Potência")
	print("0 - Sair")

	opcao = input("Escolha uma opção: ")

	if opcao == "0":
		print("Até mais!")
		break

	if opcao not in ("1", "2", "3", "4"):
		print("Opção inválida.")
		continue

	try:
		primeiro_numero = float(input("Digite o primeiro número: "))
		segundo_numero = float(input("Digite o segundo número: "))
	except ValueError:
		print("Digite apenas números.")
		continue

	if opcao == "1":
		resultado = primeiro_numero + segundo_numero
	elif opcao == "2":
		resultado = primeiro_numero - segundo_numero
	elif opcao == "3":
		resultado = primeiro_numero * segundo_numero
	elif opcao == "4":
		resultado -= primeiro_numero / segundo_numero
	elif opcao =='5':
		resultado = primeiro_numero ** segundo_numero
	elif segundo_numero != 0:
		resultado = primeiro_numero / segundo_numero
	else:
		print("Não é possível dividir por zero.")
		continue

	print(f"Resultado: {resultado}")