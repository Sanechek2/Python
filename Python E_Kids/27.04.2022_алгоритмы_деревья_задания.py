
# Алгоритмы
#
# 1.  Линейный поиск (Linear Search)
# 2.  Двоичный поиск (Binary Search)
# 
# 3.  Двоичные деревья (Binary Trees)
# 4.  Алгоритм поиска вглубь (DFS)
# 5.  Алгоритм поиска вширь (BFS)
# 
# 6.  Сортировка пузырьковая (Bubble Sort)
# 7.  Сортировка выбором (Selection Sort)
# 8. Сортировка вставками (Insert Sort)
# 9. Coртировка слиянием (Merge Sort)
# 10.  Алгоритм Хаффмана (Huffman Compression)
# 11.  Поиск подстроки (Substring Search)







# 1. Факториал
#
# Задачка: имеется 5 карточек, пронумерованных от 1 до 5.
# Выкладывая эти карточки в случайном порядке, сколько пятизначных чисел мы можем получить?
#


            



def fact(n):
    if n == 1:
        return 1
    
    otvet = n * fact(n-1) 
    return otvet
                
otvet = fact(6)
print (otvet)
        








# 2. Двоичные деревья (Binary Trees)
#
# Задание:
# Написать класс Node (то есть "Узел"), который имеет поле значения (например число),
# а так же два указателя - на левого и на правого "ребёнка".
# Мы хотим создать двоичное дерево с узлами 1, 2, 3, 4, 5
# Выписать все узлы дерева тремя способами: прямым, обратным, и центрированным
#
#         1
#     2       3
#  4     5
#
# Прямой обход:   1 2 4 5 3 
# Обратный обход: 4 5 2 3 1
# Центрированный: 4 2 5 1 3
#


class Node:
    def __init__(self, chislo):
        self.number = chislo 
        self.left = None
        self.right= None
        
        def __repr__(self):
            return (f'Node{self.number}')

        
        
        
tree = Node(1)
tree.left = Node(2)
tree.left.left = Node(4)
tree.left.right = Node(5)
tree.right= Node(3)
tree.right.left = Node(6)
tree.right.right = Node(42)

        
    
def show ( node ):
    if node == None:  
        return
        
    
    show(node.left)
    
    show(node.right)
    print (node.number)
    
    
show (tree)
# def (  ):

# def (  ):










#
# 3. Найти число 42 в дереве (поиск вширь)

line = []
history = []
line.append(tree)


def broad (N):
    print (f'\nПоиск числа {N} вширь')
    steps = 0
    while len(line) > 0:
    
        klient = line[0]
        print(f'Look to node wih number {klient.number}')
        steps +=1
        
        
        
        if klient.number == N:
            print(f'Horey! We found {N}')
            break
        else:
            
            line.pop(0)
            
            if klient.left != None:
                line.append(klient.left)
            if klient.right != None:
                line.append(klient.right)
            
    if len(line) == 0:
        print(f'Number {N} not found steps need {steps}')  
        
    

broad(3)
print(line)


#
# 4. Найти число 42 в дереве (поиск вглубь)
















