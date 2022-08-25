
# Алгоритмы
#
# 1.  Линейный поиск (Linear Search) ПРОЙДЕНО
#
# 2.  Двоичный поиск (Binary Search)
#
# 3.  Двоичные деревья (Binary Trees)
# 4.  Алгоритм поиска вглубь (DFS)
# 5.  Алгоритм поиска вширь (BFS)
# 6.  Алгоритм Хаффмана (Huffman Compression)
# 7.  Поиск подстроки (Substring Search)
# 8.  Сортировка пузырьковая (Bubble Sort)
# 9.  Сортировка выбором (Selection Sort)
# 10. Сортировка вставками (Insert Sort)
# 11. Coртировка слиянием (Merge Sort)






# 1. Класс Ученик (Student)
# Задача: создать класс Student
#
# Каждый ученик имеет свойства: name ("имя"), age ("возраст") и mark ("оценка")
# Нужно написать в классе комманду __init__ ("рождение")
# а также команду show ("покажись"), которая выпишет данные об ученике на экран
#
# После создания класса нужно создать нового ученика и вывести его данные на экран
#


class Student:

    def __init__(self, new_name, new_age, new_mark):

        self.name = new_name
        self.age = new_age
        self.mark = new_mark

    def show( self ):
        print( f'Привет! Я {self.name}, мне {self.age} лет. Моя оценка: {self.mark}' )


new_student = Student( new_name='Вася', new_age=42, new_mark=2 )
new_student.show()




# 2. Группа случайных учеников
#
# Задача: создать список из 10 случайных студентов
#
# Сначала создаём список возможных имён, 
# затем в цикле 10 раз создаём нового ученика со случайными данными
# (пригодится библиотека import random)
# 
# Пускай каждый новый студент выведет свои данные на экран и добавит себя
# в список group, который перед циклом мы сделаем пустым (group = [])
#

names = ['Aня', 'Борис', 'Вася', 'Галя', 'Дима', 'Егор', 'Женя', 'Иван', 'Коля']
group = []

import random

for i in range( 10 ):

    random_name = random.choice(names)
    random_age = random.randint(10, 16)
    mark = random.randint(1, 10)
    new_student = Student( new_name=random_name, new_age=random_age, new_mark=mark )
    new_student.show()
    group.append( new_student )





# 3. Линейный поиск
#
# Задача: найти ученика у которого оценка 8 используя линейный поиск
#
# Можно использовать функцию с прошлого занятия, но её нужно будет немного поменять
# 
# Алгоритм:
# 1. найди длину списка
# 2. начни цикл для каждого элемента списка
# 3. найди очередного студента
# 4. сравни его оценку с искомой
# 5. если она равна, выпиши на экран следующее:
#
# print( f'Нашёлся {student.name} с оценкой {iskomaja} на позиции {i} (потребовалось шагов: {i+1})' )
#
# 6. закончи функцию командой return
# 7. если студента с такой оценкой не оказалось, выведи на экран следующее:
#
# print( f'Такую оценку никто не получил' )


def linejny( spisok, iskomaja ):
    print('\nЛинейный поиск')
    dlina = len(spisok)
    for i in range(dlina):
        student = spisok[i]
        if student.mark == iskomaja:
            print( f'Нашёлся {student.name} с оценкой {iskomaja} на позиции {i} (потребовалось шагов: {i+1})' )
            return
    print( f'Такую оценку никто не получил' )


linejny( spisok=group, iskomaja=8 )




# 4. Сортировка
# Задача: посортировать учеников по оценкам и вывести их данные на экран
#
# Использует встроенную в Python сортировку с помощю команды sort
# Как посортировать студентов по оценкам? Нужна функция how_to_sort
#
#


def how_to_sort(student):
    return student.mark


group.sort(key = how_to_sort)

print('\n')
for student in group:
    student.show()







# 1. Задача: найти ученика у которого оценка 8
#    Исползуя двоичный поиск (новое)
#
#
# Алгоритм:
# 1. Найди длину всего списка
# 2. Создай указатели на первый и на последний элемент
# 3. Найди индекс элемента ровно между ними
# 4. Найди значение этого элемента
# 5. Сравни искомое число с этим средним элементом, округли до целого
# 6. Если искомое число больше, передвинь левый указатель
# 7. Если меньше, то передвинь правый
# 8. Если равно, значит искомое число найдено (выпиши на экран индекс)
# 9. Если вдруг два указателя равны, а число всё ещё не найдено,
#    значит его нет в списке
#

def dvoichny( spisok, iskomaja ):

    print('\nДвоичный поиск')

    dlina = len(spisok)
    i = 0
    j = dlina
    steps = 0

    while i != j:
        print(i, j)
        steps += 1
        m = (i+j) / 2
        m = int(m)

        student = spisok[m]
        ocenka = student.mark

        if ocenka < iskomaja:
            i = m+1
        if ocenka > iskomaja:
            j = m
        if ocenka == iskomaja:
            print( f'Нашёлся {student.name} с оценкой {iskomaja} на позиции {m} (потребовалось шагов: {steps})' )
            return
    
    if i == j:
        print( f'Такую оценку никто не получил' )


dvoichny( spisok=group, iskomaja=8 )

