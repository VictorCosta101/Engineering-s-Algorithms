import time
import matplotlib.pyplot as plt
comandos = 0

def insertionSort(alist):
   global comandos 
   for index in range(1,len(alist)):
     #atribuicao do index
     comandos += 1
     currentvalue = alist[index]
     #Acesso a alist e atribuição de cuttentvalue => +2
     comandos += 2
     position = index
     #Atribução position = index +1
     comandos += 1
     while position > 0 and alist[position-1] > currentvalue:
         # comparação position>0 +1
         # Calculo position-1  +1
         # Acesso alist[position-1] +1
         # Comparação alist[position-1]>currentvalue +1
         # Teste Logico position>0 and alist[position-1]>currentvalue +1
         comandos += 5
         alist[position]=alist[position-1]
         # Acesso alist[position]+1
         # Calculo position-1  +1
         # Acesso alist[position-1] +1
         # Atribuição  alist[position]=alist[position-1] +1 
         comandos += 4
         position = position-1
         # Calculo position-1 +1
         # Atribuição position = position-1 +1
         comandos += 2

     alist[position]=currentvalue
     # Acesso alist[position] +1
     # Atribuição alist[position]=currentvalue +1
     comandos += 2
def normalize(data):
    min_val = min(data)
    max_val = max(data)
    return [(x - min_val) / (max_val - min_val) for x in data]

def medir_tempo(alist):
    start_time = time.perf_counter()  # Inicia a contagem do tempo
    insertionSort(alist)  # Executa o algoritmo de ordenação
    end_time = time.perf_counter()  # Para a contagem do tempo
    return end_time - start_time  # Retorna o tempo total gasto

# Tamanhos diferentes de entradas para testar o algoritmo
tamanhos = [10, 100, 1000, 5000, 10000]
tempos_reais = []  # Lista para armazenar os tempos de execução real
comandos_ram = []  # Lista para armazenar o número de operações RAM

# Testando o algoritmo para diferentes tamanhos de entrada
for tamanho in tamanhos:
    alist = list(range(tamanho, 0, -1))  # Lista decrescente (pior caso)
    comandos = 0  # Reseta o contador de comandos
    tempo_real = medir_tempo(alist)  # Mede o tempo de execução real
    tempos_reais.append(tempo_real)  # Armazena o tempo de execução real
    comandos_ram.append(comandos)  # Armazena o número de operações (RAM)


instr_count_norm = normalize(comandos_ram)
exec_time_norm = normalize(tempos_reais)

# Plotando os resultados (gráfico)
plt.plot(tamanhos, instr_count_norm, label='Comandos (Modelo RAM)', marker='o')
plt.plot(tamanhos, exec_time_norm, label='Tempo de Execução Real (s)', marker='o')
plt.xlabel('Tamanho da Entrada (n)')
plt.ylabel('Comandos ou Tempo (s)')
plt.title('Comparação: Modelo RAM vs Tempo Real')
plt.legend()
plt.show()
