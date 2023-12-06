input_file = open('Пичугин_у234_vvod2.txt', 'r')
output_file = open('Пичугин_у234_vivod2.txt', 'w')

M = int(input_file.readline())  
N = int(input_file.readline())  
D = [input_file.readline().split() for i in range(N)]

y = []
for i in range(M):  
    y.append([])
    for j in range(N):
        y[i].append(D[j][i])
D = [i[::-1] for i in y]

k = int(input_file.readline())

D.sort(key=lambda x: x[N - k])

y = []
for i in range(N):  
    y.append([])
    for j in range(M):
        y[i].append(D[j][i])
D = y[::-1]

for i in D:  
    output_file.write(' '.join(str(x) for x in i) + '\n')

input_file.close()
output_file.close()
