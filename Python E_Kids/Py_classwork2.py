n1 = ord('a')
print(n1)
n1 = ord('A')
print(n1)
n1 = ord('z')
print(n1)
n1 = ord('Z')
print(n1)
n1 = ord('?')
print(n1)
n1 = ord('{')
print(n1)
n1 = ord(' ')
print(n1)



n1 = chr(10)
print(n1)


n2 = ord('%')
print (n2)

n3 = chr(38)
print(n3)

word = ''

lista = [1095, 1077, 1088, 1077, 1096, 1085, 1103]

for n in lista:
    d = chr(n)
    word = word + d
    
a = 97
a1 = a

print(word)

#repeat =0 while repeat <=0:print (ord(a1)) and (chr(a))a = a + 1#a1 = a1 + 1repeat = repeat + 1

start = "a"
nomer = ord('a')

for i in range(50):
    print( nomer+i, chr(nomer+i))
    
    
text = 'I love Python'
result = ''
key = 7

for i in text:
    i2 = ord(i)
    i3 = i2 + key
    print((i3), chr(i3))
    result = result + chr(i3)
    
    
print (result)
    

text = 'сзщзпюз"к"сзтукмрдэл"урм'
result = ''
key = 2

for i in text:
    i2 = ord(i)
    i3 = i2 - key
    print((i3), chr(i3))
    result = result + chr(i3)
    
    
print (result)
    
    
    
    
    
