
# 29.03.2022

# Задание 1. Взламывание шифра Цезаря подбором ключа
# 
# Не зная ключа, которым был зашифрован текст, попробовать
# подобрать ключ и расшифровать оригинальное сообщение. Ключ в пределах от 1 до 26.
# 


text = "їѧњѕшьўшњѤ8џэѓіъэђ8ѕш8љћѕьћђ8єэјњъэўш8ёіѝіѝі8ѐ8щћњѣѓђш8јієћ"

result = ''
key = 0

for key in range(1, 34):
    for i in text:
        i1 = ord(i)
        i3 = i1 - key
        print((i3), chr(i3))
        result = result + chr(i3)
    
    result += ''
    result += str(key)
    result += '\n'
    
print (result)


# Задание 2. Команда index()
# 
# Команда index() позволяет найти первое появление символа в строке (или элеметна в списке).
# В поезде едет 9 мирных жителей и один шпион. Мирные жители подписаны "Мирный",
# а шпион подписан с маленькой буквы: "мирный".
# Найти на каком месте сидит шпион, и подписать его "ШПИОН".
# 

train = ["Мирный", "Мирный", "Мирный", "Мирный", "Мирный", "Мирный", "Мирный", "Мирный", "мирный", "Мирный" ]

Mafia = train.index('мирный')
print(Mafia)
train[Mafia] = 'Шпион'
print [train]











# Задание 3. Подсчёт символов
# 
# Теперь мы хотим посчитать количество букв в тексте.
# Все возможные символы текста составляют алфавит: 33 буквы и символ пробела.
# Счётчик counter показывает, сколько раз этот символ уже появлялся в тексте (в начале все счётчики на нуле)
# 

text3 = "кто проживает на дне океана"

print(text.count('o'))

alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя "
counter = []
for i in alphabet:
    counter.append(0)
    
print (counter)

for x in text:
    number = alphabet.index(x)
    counter[number] += 1
    
print(counter)


# Задание 4. Подсчёт символов в большом тексте
#
# Возьмём текст побольше, и "погрязнее": теперь в тексте есть не только буквы и пробел.
# Задание такое же как предыдущее: посчитать сколько букв и пробелов в тексте.
#

text9 = "o;кто проживает на дне океана tjfkytj;uyrj6"

alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя "
counter = []
for i in alphabet:
    counter.append(0)

for x in text:
    
    if x in alphabet:
    
        number = alphabet.index(x)
        counter[number] += 1

print(counter)

# Задание 5. Использование частоты символов для расшифровки
#
#

text = "¹Сёпшо.Пьп.Шротюоѐыљу.жѐоыљÉ:.ѐошфу.цхруяѐыљч.шош.¹Яэоыѕ.Пьп.Яшрћю.ЭћыѐяÉ.6оысщ<.a~}|usP}p.aos^o|7:.•.оъуюцшоыяшцч.ъёщњѐцэщцшоєцьыыљч.яуюцощ:.шьѐьюљч.ѐюоыящцюёуѐяѝ.ыо.ѐущушоыощу.¹\wqysz}rs}|É<.Эьѝрцщяѝ.р.ћђцюу.?.ъоѝ.?GGG.сьто.ц.яѐощ.ьтыьч.цх.яоъљѓ.эьэёщѝюыљѓ.оыцъоєцьыыљѓ.эюьсюоъъ.ѐущурцтуыцѝ<.лѐь.эуюрљч.эь.эюьтьщфцѐущњыьяѐц.эьшохо.оыцъцюьроыыљч.яуюцощ.ѐущушоыощо.¹\wqysz}rs}|É:.ьпьсыоріцч.¹Ьѓ.ёф.ћѐц.туѐшц/É.•.ыо.тоыыљч.ъьъуыѐ.ьы.ыояѕцѐљроуѐ.?@.эьщыљѓ.яухьыьр<.Р.цќщу.@>?G.сьто.ъёщњѐяуюцощ.пљщ.эюьтщџы.ыо.ѐюцыотєоѐљч.яухьы<.Тучяѐрцѝ.оыцъоєцьыыьсь.яуюцощо.юохрьюоѕцроќѐяѝ.ыо.тыу.ацѓьсь.ьшуоыо:.р.ыупьщњіьъ.рљъљіщуыыьъ.сьюьтшу.эьт.ыохроыцуъ.Пцшцыц.Пьѐѐьъ:.сту.сщорыљъц.тучяѐрёќїцъц.щцєоъц.ѝрщѝќѐяѝ.эюутяѐорцѐущц.ъьюяшьч.ђоёыљ<.Ярѝхоыь.ћѐь.я.ѐуъ:.ѕѐь.яьхтоѐущњ.яуюцощо.Яѐцруы.гцщщуыпуюс.ыоѕощ.яьхтороѐњ.ъёщњѐђцщњъљ.ц.юцяёышц.ыо.ѐуъё.фцхыц.ьпцѐоѐущуч.ъьюяшьсь.тыо:.уїџ.шьсто.эюуэьторощ.ъьюяшёќ.пцьщьсцќ.р.Цыяѐцѐёѐу.ьшуоыьщьсцц.ьшюёсо.Ьюцытф.р.Тоыо;Эьчыѐ:.іѐоѐ.Шощцђьюыцѝ:.я.?GFB.эь.?GFE.сьт<.Р.?GFE.сьтё.гцщщуыпуюс.ьяѐорцщ.цыяѐцѐёѐ:.ѕѐьпљ.юуощцхьроѐњ.ярьќ.ъуѕѐё.•.яѐоѐњ.ъёщњѐцэщцшоѐьюьъ<"

alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя "
counter = []


for i in alphabet:
    counter.append(0)

for x in text:
    
    if x in alphabet:
    
        number = alphabet.index(x)
        counter[number] += 1

print(counter)
