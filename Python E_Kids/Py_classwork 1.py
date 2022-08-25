word1 = str(input('Введите первое слово:'))

length = len(word1)
closed =length

list_w1= []

for i in range(0,length):
    list_w1.append( "_" )
    
    

live = 5

while (live>0) and (closed>0):
    
    print(list_w1)
    
    print('live = 5')
    
    letter = str(input("введи букву"))
    success = False
    for i in range(0, length):
        if letter[i]  == list_w1:
            closed = closed- 1
            list_w1[i] = length
            success = True
    if success== False:
        live = live-1
    

