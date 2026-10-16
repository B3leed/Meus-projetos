tarefas = [] # a tarefa esta em listas e nulo ja que assim uma valor pode ser adicionado a lista de tarefas

while True:
    print("=== Lista de tarefas ===")
    print("1 - Adicionar tarefa")
    print("2 - Remover tarefa")
    print("3 - Listar tarefas")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("Até mais!")
        break
    elif opcao == "1":
        tarefa = input("Digite a tarefa: ")
        tarefas.append(tarefa)
        print(f"Tarefa '{tarefa}' adicionada com sucesso!")
    elif opcao == "2":
        tarefa = input("Digite a tarefa que deseja remover: ")
        if tarefa in tarefas:
            tarefas.remove(tarefa)
            print(f'essa tarefa {tarefa} foi removida com sucesso!')
        else:
            print('essa tarefa nao foi encontrada bozo lol')
    elif opcao == "3":
        print("Tarefas:")
        for i, tarefa in enumerate(tarefas, start=1):
            print(f"{i}. {tarefa}")
