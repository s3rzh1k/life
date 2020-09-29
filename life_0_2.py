import pygame
import numpy as np

pygame.init()
sc = pygame.display.set_mode((620, 620))
surf = pygame.Surface((600, 600))
surf.fill((255, 255, 255))

n=60
ar = np.random.rand(n,n)
for i in range(n):
    for j in range(n):
        ar[i][j] = 0
b = 10

ob = pygame.Surface((10,10))    #чёрный пиксель
ob.fill((0,0,0))

ow = pygame.Surface((10,10))    #белый пиксель
ow.fill((255,255,255))

def romb(x,y):
    """
    Рисует закрашенный ромб
    :param x: координата x верхней вершины ромба
    :param y: координата y верхней вершины ромба
    """
    if x == 0 or y == 0:
        if x == 0 and y != 0:
            yy = 0
            xx = y // 10 - 1
        elif y == 1 and x != 1:
            xx = 0
            yy = x // 10 - 1
        else:
            yy = 0
            xx = 0
    else:
        yy = x // 10 - 1
        xx = y // 10 - 1
    surf.blit(ob, (x,y))
    ar[xx][yy]=1
    surf.blit(ob, (x-b,y+b))
    ar[xx+1][yy-1]=1
    surf.blit(ob, (x+b,y+b))
    ar[xx+1][yy+1]=1
    surf.blit(ob, (x,y+2*b))
    ar[xx+2][yy]=1
    surf.blit(ob, (x, y+b))
    ar[xx+1][yy] = 1

def tub(x,y):
    """
    Рисует объект tub (ванна)
    :param x: координата x верхней вершины tub
    :param y: координата y верхней вершины tub
    """
    if x == 0 or y == 0:
        if x == 0 and y != 0:
            yy = 0
            xx = y // 10 - 1
        elif y == 1 and x != 1:
            xx = 0
            yy = x // 10 - 1
        else:
            yy = 0
            xx = 0
    else:
        yy = x // 10 - 1
        xx = y // 10 - 1
    surf.blit(ob, (x,y))
    ar[xx][yy]=1
    surf.blit(ob, (x-b,y+b))
    ar[xx+1][yy-1]=1
    surf.blit(ob, (x+b,y+b))
    ar[xx+1][yy+1]=1
    surf.blit(ob, (x,y+2*b))
    ar[xx+2][yy]=1

def white(x,y):
    """
    Рисует белый <<пиксель>> разм 10х10
    :param x: координата x верхнего левого угла
    :param y: координата y верхнего левого угла
    """
    surf.blit(ow, (x, y))
    if x == 0 or y == 0:
        if x == 0 and y != 0:
            yy = 0
            xx = y // 10 - 1
        elif y == 1 and x != 1:
            xx = 0
            yy = x // 10 - 1
        else:
            yy = 0
            xx = 0
    else:
        yy = x // 10 - 1
        xx = y // 10 - 1
    ar[xx][yy] = 0

def black(x,y):
    """
    Рисует чёрный <<пиксель>> разм 10х10
    :param x: координата x верхнего левого угла
    :param y: координата y верхнего левого угла
    """
    surf.blit(ob, (x, y))
    if x == 0 or y == 0:
        if x == 0 and y != 0:
            yy = 0
            xx = y // 10 - 1
        elif y == 1 and x != 1:
            xx = 0
            yy = x // 10 - 1
        else:
            yy = 0
            xx = 0
    else:
        yy = x // 10 - 1
        xx = y // 10 - 1
    ar[xx][yy] = 1

def stick(x,y):
    """
    Рисует горизонтальную палку
    :param x: координата x левого конца палки
    :param y: координата y левого конца палки
    """
    if x == 0 or y == 0:
        if x == 0 and y != 0:
            yy = 0
            xx = y // 10 - 1
        elif y == 1 and x != 1:
            xx = 0
            yy = x // 10 - 1
        else:
            yy = 0
            xx = 0
    else:
        yy = x // 10 - 1
        xx = y // 10 - 1
    surf.blit(ob, (x, y))
    ar[xx][yy] = 1
    surf.blit(ob, (x+b, y))
    ar[xx][yy+1] = 1
    surf.blit(ob, (x+2*b, y))
    ar[xx][yy+2] = 1

def vert_stick(x,y):
    """
    Рисует вертикальную палку
    :param x: координата x верхнего конца палки
    :param y: координата y верхнего конца палки
    """
    if x == 0 or y == 0:
        if x == 0 and y != 0:
            yy = 0
            xx = y // 10 - 1
        elif y == 1 and x != 1:
            xx = 0
            yy = x // 10 - 1
        else:
            yy = 0
            xx = 0
    else:
        yy = x // 10 - 1
        xx = y // 10 - 1
    surf.blit(ob, (x, y))
    ar[xx][yy] = 1
    surf.blit(ob, (x, y+b))
    ar[xx+1][yy] = 1
    surf.blit(ob, (x, y+2*b))
    ar[xx+2][yy] = 1

def block(x,y):
    """
    Рисует квадрат
    :param x: координата x верхнего левого угла
    :param y: координата y верхнего левого угла
    """
    if x==0 or y==0:
        if x==0 and y!=0:
            yy = 0
            xx = y // 10 - 1
        elif y==1 and x!=1:
            xx = 0
            yy = x // 10 - 1
        else:
            yy = 0
            xx = 0
    else:
        yy = x // 10 - 1
        xx = y // 10 - 1
    surf.blit(ob, (x, y))
    ar[xx][yy] = 1
    surf.blit(ob, (x + b, y))
    ar[xx][yy + 1] = 1
    surf.blit(ob, (x + b, y + b))
    ar[xx + 1][yy + 1] = 1
    surf.blit(ob, (x, y + b))
    ar[xx + 1][yy] = 1

def beehive(x,y):
    """
    Рисует объект beehive (улей)
    :param x: координата x левой вершины
    :param y: координата y левой вершины
    """
    if x==0 or y==0:
        if x==0 and y!=0:
            yy = 0
            xx = y // 10 - 1
        elif y==1 and x!=1:
            xx = 0
            yy = x // 10 - 1
        else:
            yy = 0
            xx = 0
    else:
        yy = x // 10 - 1
        xx = y // 10 - 1
    surf.blit(ob, (x, y))
    ar[xx][yy] = 1
    surf.blit(ob, (x+b, y-b))
    ar[xx-1][yy+1] = 1
    surf.blit(ob, (x+2*b, y-b))
    ar[xx-1][yy+2] = 1
    surf.blit(ob, (x+3*b, y))
    ar[xx][yy+2] = 1
    surf.blit(ob, (x+2*b, y+b))
    ar[xx+1][yy+2] = 1
    surf.blit(ob, (x+b, y+b))
    ar[xx+1][yy+1] = 1

def glider(x,y):
    """
    Рисует малый боевой корабль
    :param x: координата x левого нижнего угла
    :param y: координата y левого нижнего угла
    """
    if x==0 or y==0:
        if x==0 and y!=0:
            yy = 0
            xx = y // 10 - 1
        elif y==1 and x!=1:
            xx = 0
            yy = x // 10 - 1
        else:
            yy = 0
            xx = 0
    else:
        yy = x // 10 - 1
        xx = y // 10 - 1
    stick(x,y)
    surf.blit(ob, (x+2*b, y-b))
    ar[xx-1][yy+2] = 1
    surf.blit(ob, (x+b, y- 2*b))
    ar[xx-2][yy+1] = 1

def middle(x,y):
    """
    Рисует средний боевой корабль
    :param x: координата x левого нижнего угла
    :param y: координата y левого нижнего угла
    """
    if x==0 or y==0:
        if x==0 and y!=0:
            yy = 0
            xx = y // 10 - 1
        elif y==1 and x!=1:
            xx = 0
            yy = x // 10 - 1
        else:
            yy = 0
            xx = 0
    else:
        yy = x // 10 - 1
        xx = y // 10 - 1
    stick(x,y)
    surf.blit(ob, (x + 3 * b, y))
    ar[xx][yy +3] = 1
    surf.blit(ob, (x + 4 * b, y))
    ar[xx][yy +4] = 1
    surf.blit(ob, (x + 4 * b, y+b))
    ar[xx + 1][yy +4] = 1
    surf.blit(ob, (x + 4 * b, y+2*b))
    ar[xx + 2][yy +4] = 1
    surf.blit(ob, (x + 3 * b, y+3*b))
    ar[xx +3][yy +3] = 1
    surf.blit(ob, (x - b, y+b))
    ar[xx + 1][yy -1] = 1
    surf.blit(ob, (x - b, y + 3*b))
    ar[xx +3][yy -1] = 1
    surf.blit(ob, (x + b, y + 4 * b))
    ar[xx +4][yy +1] = 1

def pulsar(x,y):
    """
    Рисует объект pulsar (пульсар)
    :param x: координата x левого верхнего угла
    :param y: координата y левого верхнего угла
    """
    stick(x+2*b,y)  #lt
    vert_stick(x,y+2*b)
    stick(x+2*b,y+5*b)
    vert_stick(x+5*b,y+2*b)
    x += 7*b
    stick(x+b,y)   #rt
    vert_stick(x,y+2*b)
    stick(x+b,y+5*b)
    vert_stick(x+5*b,y+2*b)
    y += 7*b
    stick(x+b,y)    #rd
    vert_stick(x,y+b)
    stick(x+b,y+5*b)
    vert_stick(x+5*b,y+b)
    x -= 7*b
    stick(x+2*b,y)
    vert_stick(x,y+b)
    stick(x+2*b,y+5*b)
    vert_stick(x+5*b,y+b)

def check(x,y):
    """
    Проверяет соседей в матрице, записывает результат в другую матрицу
    :param x: адрес ячейки в матрице
    :param y: адрес ячейки в матрице
    """
    num = 0
    if x>0 and y>0 and x<59 and y<59:
        if ar[x-1][y] == 1:
            num+=1
        if ar[x-1][y-1] == 1:
            num+=1
        if ar[x][y-1] == 1:
            num+=1
        if ar[x+1][y-1] == 1:
            num+=1
        if ar[x+1][y] == 1:
            num+=1
        if ar[x+1][y+1] == 1:
            num+=1
        if ar[x][y+1] == 1:
            num+=1
        if ar[x-1][y+1] == 1:
            num+=1
    elif x==0 and y==0: #lt
        if ar[y][x+1] == 1:
            num+=1
        if ar[y+1][x+1] == 1:
            num+=1
        if ar[y+1][x] == 1:
            num+=1
    elif x==59 and y==0: #rt
        if ar[y][x-1] == 1:
            num+=1
        if ar[y+1][x-1] == 1:
            num+=1
        if ar[y+1][x] == 1:
            num+=1
    elif x==59 and y==59: #rd
        if ar[y][x-1] == 1:
            num+=1
        if ar[y-1][x-1] == 1:
            num+=1
        if ar[y-1][x] == 1:
            num+=1
    elif x==0 and y==59: #ld
        if ar[y-1][x] == 1:
            num+=1
        if ar[y-1][x+1] == 1:
            num+=1
        if ar[y][x+1] == 1:
            num+=1
    elif x==0: #lb
        if ar[y-1][x] == 1:
            num += 1
        if ar[y-1][x+1] == 1:
            num += 1
        if ar[y][x+1] == 1:
            num += 1
        if ar[y+1][x+1] == 1:
            num += 1
        if ar[y+1][x] == 1:
            num += 1
    elif y==0: #tb
        if ar[y][x-1] == 1:
            num += 1
        if ar[y+1][x - 1] == 1:
            num += 1
        if ar[y+1][x] == 1:
            num += 1
        if ar[y+1][x+1] == 1:
            num += 1
        if ar[y][x+1] == 1:
            num += 1
    elif x==59: #rb
        if ar[y-1][x] == 1:
            num += 1
        if ar[y-1][x - 1] == 1:
            num += 1
        if ar[y][x-1] == 1:
            num += 1
        if ar[y+1][x-1] == 1:
            num += 1
        if ar[y+1][x] == 1:
            num += 1
    elif y == 59:  # db
        if ar[y][x-1] == 1:
            num += 1
        if ar[y - 1][x - 1] == 1:
            num += 1
        if ar[y-1][x] == 1:
            num += 1
        if ar[y - 1][x + 1] == 1:
            num += 1
        if ar[y][x+1] == 1:
            num += 1
    if num < 2 or num > 3:
        br[x][y]=0
    elif num == 3:
        br[x][y]=1

def ris(mat):
    """
    Рисует следующую итерацию по новой матрице
    :param mat: матрица, получившаяся после проверок функцией check()
    """
    for i in range(n):
        for j in range(n):
            if mat[i][j] == 1:
                black((j + 1) * 10, (i + 1) * 10)
                sc.blit(surf, (10, 10))
            else:
                white((j + 1) * 10, (i + 1) * 10)
                sc.blit(surf, (10, 10))


def world():
    """
    Создаёт начальное состояние мира
    """
    stick(500,500) #stick
    romb(100,100) #romb
    block(200,200) #block
    tub(100,250) #tub
    beehive(100,300) #beehive
    stick(100,400) #toad
    stick(110,390)
    block(160,400) #beacon
    block(180,420)
    white(180,420)
    white(170,410)
    glider(200,100) #glider
    middle(300,100) #middle
    vert_stick(550,500) #vertical stick
    pulsar(320,320) #pulsar
    sc.blit(surf, (10, 10))

world()
br = np.copy(ar)
pygame.display.update()

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
    for i in range(n):
        for j in range(n):
            check(i,j)
    ar = np.copy(br)
    ris(ar)
    pygame.display.update()
    pygame.time.delay(10)
