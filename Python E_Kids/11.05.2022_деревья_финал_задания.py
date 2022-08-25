import random
# Алгоритмы
#
# 1.  Линейный поиск (Linear Search)
# 2.  Двоичный поиск (Binary Search)
# 3.  Двоичные деревья (Binary Trees)
# 4.  Алгоритм поиска вглубь (BFS)
# 
# 5.  Алгоритм поиска вширь (DFS)
# 
# 6.  Сортировка пузырьковая (Bubble Sort)
# 7.  Сортировка выбором (Selection Sort)
# 8. Сортировка вставками (Insert Sort)
# 9. Coртировка слиянием (Merge Sort)
# 10.  Алгоритм Хаффмана (Huffman Compression)
# 11.  Поиск подстроки (Substring Search)






# (прошлые занятия) Двоичные деревья (Binary Trees)

class Node:
    
    def __init__(self, chislo):
        self.number = chislo
        self.left = None
        self.right = None
        
    def __repr__(self):
        return f'Node({self.number})'
        
tree = Node( 1 )
tree.left = Node( 2 )
tree.right = Node( 3 )
tree.left.left = Node( 4 )
tree.left.right = Node( 5 )
tree.right.left = Node( 6 )
tree.right.right = Node( 42 )
    
    
    
def show (  node  ):

    if node == None:
        return
    
    show( node.left )    
    show( node.right )
    print( node.number )
    

# show( tree )








#
# (прошлые занятия) Поиск в дереве вширь (с помощью "очереди")
# 


line = []
line.append( tree )


def broad( N ):
    print(f'\nПоиск числа {N} вширь')
    steps = 0
    while len(line) > 0:
    
        klient = line[0]
        
        print(f'\Cмотрим на узел с числом {klient.number}')
        steps += 1
        if klient.number == N:
            print( f'\Ура! Нашлось число {N}, потребовалось шагов: {steps}' )
            break
        else:
            
            line.pop(0)
            
            if klient.left != None:
                line.append( klient.left )
            if klient.right != None:
                line.append( klient.right )
    
    if len(line) == 0:
        print( f'\Числа {N} в дереве не нашлось, потребовалось шагов: {steps}' )
        
    
broad( N=42 )




#
# 1. Поиск в дереве вглубь (с помощью "стопки")
# Задание: написать функцию, которая найдёт заданное число в дереве,
# и искать будет начиная с самых молодых узлов (детей).
#
# Алгоритм:
#
# (перед запуском функции)
# 1. Создать пустой список stack (стопка)
# 2. Добавить в стопку tree
# 3. Создать пустой список looked (узлы, которые мы уже проверили)
#
# (функция)
# 4. Создать переменную steps котоая считает количство проверок
# 5. Бесконечный цикл
# 6. Создать переменную look и поместить в неё самый правый элемент стопки
# 7. Если у узла look есть левый ребёнок, и если этого ребёнка нет в списке looked,
#    то добавить его в стопку справа, и вернуться к началу цикла (команда continue)
# 8. Такая же проверка для правого ребёнка
# 9. Добавить 1 к переменной steps
# 10. Если число в узле look это то что мы ищем, выписать на экран и сломать цикл
# 11. Если нет, удалить из стопки самый правый узел, и добавить его в список looked
# 12. В конце: если длина стопки 0, то числа в дереве нет, и мы ломаем цикл


stack = []
stack.append(tree)
looked = []

def deep(N):
    steps = 0
    while True:
        look = stack[-1]
        
        if look.left != None:
            if not (look.left in looked):
                stack.append(look.left)
                continue
            
        if look.right != None:
            if not (look.right in looked):
                stack.append(look.right)
                continue
            
        steps +=1

        print (f'checked node with number {look.number}')
        if look.number == N:
            print ( f'Ура! Нашлось число {N}, потребовалось шагов: {steps}' )
            break
        if look.number != N:
            stack.pop()
            looked.append(look)
        if len(stack) == 0:
            print( f'\Числа {N} в дереве не нашлось, потребовалось шагов: {steps}' )
            break
        
            
        
    
    print(f'\nПоиск числа {N} вглубину')


    

        

deep(42)









# 2. Новые деревья
# Задание: написать функцию new_tree, которая будет создавать новое дерево.
# Глубина этого дерева определяется переменной how_deep.
# Функция возвращает (слово return в конце) корень дерева (первый узел),
# А также случайное число из тех которые есть в дереве.
#
# Алгоритм:
# 
# 1. Создать узел root со случайным числом от 1 до 100 (это наш начальный узел, корень)
# 2. Создать список need_children, и добавить в него корень (это те узлы, которым нужны дети)
# 3. Создать пустой список all_numbers (все числа которые есть в дереве)
# 4. Основной цикл, который повторится (how_deep-1) раз
# 5.     Создать пустой список children (новые дети)
# 6.     Вложенный цикл, для каждого узла из тех кому нужны дети (список need_children)
# 7.         Добавить каждому такому узлу левого и правого ребёнка (узлы со случайными числами от 1 до 100)
# 8.         Добавить этих детей в список children
# 9.         Добавить их номера в список all_numbers
# 10.    После вложенного цикла, но в основном, need_children = children (смена поколений)
# 11. В конце выбрать случайное число N из списка all_numbers (random.choice)
# 12. Вернуть два значения: root и N (return root, N)



# def new_tree( how_deep ):
    

    
        















import random

# Использование функции new_tree

# D1, N1 = new_tree( how_deep=5 )

# show(D1)
# print('Ищем:', N1)





## Поиск числа вглубь
# stack = []
# stack.append( D1 )
# looked = []
# deep( N1 )




## Поиск числа вширь
# line = []
# line.append( D1 )
# broad( N1 )





