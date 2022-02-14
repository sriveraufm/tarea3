from cmath import pi
import struct
print('1. Circulo')
print('2. Rectangulo')
print('3. Triangulo')
figura = int(input('Ingrese la figura que desea calcular el area: '))


def area(struct):
    if(len(struct) > 1):
        area = 1
    else:
        area = pi
    for i in range(0,len(struct)):
        area = area * struct[i]
    return area

if(figura ==1 ):
    l1 = float(input('Radio = '))
    slados = struct.pack('f', l1)
    lados = struct.unpack('f', slados)
if(figura ==2):
    l1 = float(input('lado 1 = '))
    l2 = float(input('lado 2 = '))
    slados = struct.pack('ff', l1,l2)
    lados = struct.unpack('ff', slados)

if(figura ==3):
    l1 = float(input('lado 1 = '))
    l2 = float(input('lado 2 = '))
    l3 = float(input('lado 3 = '))
    slados = struct.pack('fff', l1,l2,l3)
    lados = struct.unpack('fff', slados)

print('El area es => ', area(lados))
