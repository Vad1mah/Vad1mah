N = int(input('Введите число вершин графа: '))
edge_list = []
binded_edges = []
nums = 2

for edge in range(int(input('Введите число рёбер: '))):
    Flag_for_connecting = False
    Flag_for_adding = True
    num_1, num_2 = input("Введите точки ребра через пробел: ").split()
    edge_list.append([num_1, num_2])
    if edge == 0:
        binded_edges.append([num_1, num_2])
        continue
    
    for binded in range(len(binded_edges)):
        if num_1 in binded_edges[binded] or num_2 in binded_edges[binded]:
            Flag_for_connecting = True
            Flag_for_adding = False
            
        if Flag_for_connecting:
            if num_1 in binded_edges[binded]:
                binded_edges[binded].append(num_2)
            else:
                binded_edges[binded].append(num_1)
            nums += 1
            break
            
    if Flag_for_adding:
        binded_edges.append([num_1, num_2])
        nums += 2

print('\nN =', N)
print('Рёбра:')
for edge in edge_list:
    print(*edge)
print('\nДля этого набора ответ =', N - nums + len(binded_edges) - 1)