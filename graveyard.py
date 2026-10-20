import time

input("Pressione Enter para iniciar o contador...")
inicio = time.perf_counter()

input("Pressione Enter novamente para parar...")
tempo_decorrido = time.perf_counter() - inicio

print(f"Tempo decorrido: {tempo_decorrido:.2f} segundos")
