import random, pygame, sys

pygame.init()
y = 10  # int(input('y = '))
x = 10  # int(input('x = '))
n = 10  # int(input('n = '))
Arial = pygame.font.SysFont('Arial', 20)
win = pygame.display.set_mode((x * 20, y * 20))
img = pygame.image.load('img.png')
bombs = []
bmap = []
fieldss = []
bombss = []
fields = []
flag = pygame.image.load('flag.png')
clock = pygame.time.Clock()
showntiles = []


def map_gen(x, y, n):
    global bombs
    global bmap
    global map
    map = []
    bombs = []
    bmap = []
    if n >= x * y:
        print("dane nie maja sensu ")

    for i in range(x):
        row = []
        for j in range(y):
            bombs.append([i, j])
            row.append(0)
        bmap.append(row)

    for i in range(n):
        bomb = random.choice(bombs)

        bombs.remove(bomb)
        bmap[(bomb[0] - 1)][(bomb[1] - 1)] = "b"

    print("done")


print(y)
print(x)
map_gen(x, y, n)

a = -1
for i in bmap:
    b = 0
    a += 1
    for j in i:

        if j == 'b':
            bombss.append([a, b])
        b += 1

print(bombss)

for i in bombss:  # numermaker
    if not i[0] == 0 and not i[1] == 0 and not i[0] == (y - 1) and not i[1] == (x - 1):
        if not bmap[i[0] - 1][i[1] - 1] == 'b':
            bmap[i[0] - 1][i[1] - 1] += 1
        if not bmap[i[0] - 1][i[1]] == 'b':
            bmap[i[0] - 1][i[1]] += 1
        if not bmap[i[0] - 1][i[1] + 1] == 'b':
            bmap[i[0] - 1][i[1] + 1] += 1
        if not bmap[i[0]][i[1] - 1] == 'b':
            bmap[i[0]][i[1] - 1] += 1
        if not bmap[i[0]][i[1] + 1] == 'b':
            bmap[i[0]][i[1] + 1] += 1
        if not bmap[i[0] + 1][i[1] - 1] == 'b':
            bmap[i[0] + 1][i[1] - 1] += 1
        if not bmap[i[0] + 1][i[1]] == 'b':
            bmap[i[0] + 1][i[1]] += 1
        if not bmap[i[0] + 1][i[1] + 1] == 'b':
            bmap[i[0] + 1][i[1] + 1] += 1

    elif i[0] == 0 and not i[1] == 0 and not i[1] == (x - 1):
        if not bmap[i[0]][i[1] - 1] == 'b':
            bmap[i[0]][i[1] - 1] += 1
        if not bmap[i[0]][i[1] + 1] == 'b':
            bmap[i[0]][i[1] + 1] += 1
        if not bmap[i[0] + 1][i[1] - 1] == 'b':
            bmap[i[0] + 1][i[1] - 1] += 1
        if not bmap[i[0] + 1][i[1]] == 'b':
            bmap[i[0] + 1][i[1]] += 1
        if not bmap[i[0] + 1][i[1] + 1] == 'b':
            bmap[i[0] + 1][i[1] + 1] += 1

    elif i[0] == 0 and i[1] == 0:
        if not bmap[i[0]][i[1] + 1] == 'b':
            bmap[i[0]][i[1] + 1] += 1
        if not bmap[i[0] + 1][i[1]] == 'b':
            bmap[i[0] + 1][i[1]] += 1
        if not bmap[i[0] + 1][i[1] + 1] == 'b':
            bmap[i[0] + 1][i[1] + 1] += 1

    elif not i[0] == 0 and i[1] == 0 and not i[0] == y - 1:
        if not bmap[i[0] - 1][i[1]] == 'b':
            bmap[i[0] - 1][i[1]] += 1
        if not bmap[i[0] - 1][i[1] + 1] == 'b':
            bmap[i[0] - 1][i[1] + 1] += 1
        if not bmap[i[0]][i[1] + 1] == 'b':
            bmap[i[0]][i[1] + 1] += 1
        if not bmap[i[0] + 1][i[1]] == 'b':
            bmap[i[0] + 1][i[1]] += 1
        if not bmap[i[0] + 1][i[1] + 1] == 'b':
            bmap[i[0] + 1][i[1] + 1] += 1
    elif i[0] == y and i[1] == 0:
        if not bmap[i[0] - 1][i[1]] == 'b':
            bmap[i[0 - 1]][i[1]] += 1
        if not bmap[i[0] + 1][i[1] + 1] == 'b':
            bmap[i[0] + 1][i[1] + 1] += 1
        if not bmap[i[0]][i[1] + 1] == 'b':
            bmap[i[0]][i[1] + 1] += 1
    elif i[0] == (y - 1) and i[1] == 0:
        if not bmap[i[0] - 1][i[1]] == 'b':
            bmap[i[0] - 1][i[1]] += 1
        if not bmap[i[0] - 1][i[1] + 1] == 'b':
            bmap[i[0] - 1][i[1] + 1] += 1
        if not bmap[i[0]][i[1] + 1] == 'b':
            bmap[i[0]][i[1] + 1] += 1
    elif i[0] == (y - 1) and not i[1] == 0 and not i[1] == (x - 1):
        if not bmap[i[0] - 1][i[1] - 1] == 'b':
            bmap[i[0] - 1][i[1] - 1] += 1
        if not bmap[i[0] - 1][i[1]] == 'b':
            bmap[i[0] - 1][i[1]] += 1
        if not bmap[i[0] - 1][i[1] + 1] == 'b':
            bmap[i[0] - 1][i[1] + 1] += 1
        if not bmap[i[0]][i[1] - 1] == 'b':
            bmap[i[0]][i[1] - 1] += 1
        if not bmap[i[0]][i[1] + 1] == 'b':
            bmap[i[0]][i[1] + 1] += 1
    elif i[0] == (y - 1) and i[1] == (x - 1):
        if not bmap[i[0] - 1][i[1] - 1] == 'b':
            bmap[i[0] - 1][i[1] - 1] += 1
        if not bmap[i[0] - 1][i[1]] == 'b':
            bmap[i[0] - 1][i[1]] += 1
        if not bmap[i[0]][i[1] - 1] == 'b':
            bmap[i[0]][i[1] - 1] += 1
    elif not i[0] == (y - 1) and not i[0] == 0 and i[1] == (x - 1):
        if not bmap[i[0] - 1][i[1] - 1] == 'b':
            bmap[i[0] - 1][i[1] - 1] += 1
        if not bmap[i[0] - 1][i[1]] == 'b':
            bmap[i[0] - 1][i[1]] += 1
        if not bmap[i[0]][i[1] - 1] == 'b':
            bmap[i[0]][i[1] - 1] += 1
        if not bmap[i[0] + 1][i[1] - 1] == 'b':
            bmap[i[0] + 1][i[1] - 1] += 1
        if not bmap[i[0] - 1][i[1]] == 'b':
            bmap[i[0] - 1][i[1]] += 1
    elif i[0] == y and i[1] == (x - 1):
        if not bmap[i[0]][i[1] - 1] == 'b':
            bmap[i[0]][i[1] - 1] += 1
        if not bmap[i[0] + 1][i[1] - 1] == 'b':
            bmap[i[0] + 1][i[1] - 1] += 1
        if not bmap[i[0] + 1][i[1]] == 'b':
            bmap[i[0] + 1][i[1]] += 1


class tile(object):
    def __init__(self, x, y, isb, ishid, isflagged):
        global bmap
        self.x = x
        self.y = y
        self.isb = isb
        self.ishid = ishid
        self.isflagged = isflagged
        self.val = bmap[y][x]

    def draw(self, win):

        if self.ishid == False and self.isflagged == False:
            if self.isb == True:
                win.blit(img, ([self.x * 20, self.y * 20]))
            else:
                num = Arial.render(str(bmap[self.y][self.x]), 1, (0, 0, 255))
                win.blit(num, (self.x * 20 + 3, self.y * 20))
        elif self.isflagged == True:
            win.blit(flag, ([self.x * 20, self.y * 20]))


        else:
            pygame.draw.rect(win, (127 * (self.x - 2 * (self.x // 2) + self.y - 2 * (self.y // 2)),
                                   127 * (self.x - 2 * (self.x // 2) + self.y - 2 * (self.y // 2)),
                                   127 * (self.x - 2 * (self.x // 2) + self.y - 2 * (self.y // 2))),
                             (20 * self.x, 20 * self.y, 20, 20))

    def odkryj(self):
        if self.isflagged == False:
            if self.ishid == True: self.ishid = False

        else:
            self.isflagged = False

    def flagg(self):
        if self.ishid == True: self.isflagged = True

    def value(self):
        return self.val


for i in range(y):

    for j in range(x):
        if bmap[i][j] == 'b':
            fields.append(tile(j, i, True, True, False))
        else:
            fields.append(tile(j, i, False, True, False))


# print(fieldss)
def redrawgamewindow():
    for field in fields:
        field.draw(win)

    pygame.display.update()


run = True
while run:  # mainloop
    redrawgamewindow()
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if click[0] == 1:
        showntiles.append([int(mouse[1] // 20), int(mouse[0] // 20)])

        #fields[int((mouse[1] // 20) * x + (mouse[0] // 20))].odkryj()
    if click[2] == 1:
        fields[int((mouse[1] // 20) * x + (mouse[0] // 20))].flagg()

    for i in showntiles:
        fields[i[0] * x + i[1]].odkryj()
        if bmap[i[0]][i[1]] == 0:
            if not i[0] == 0 and not i[1] == 0 and not i[0] == (y - 1) and not i[1] == (x - 1):
                showntiles.append([i[0] - 1, i[1] - 1])        #ul
                showntiles.append([i[0] - 1, i[1]])             #u
                showntiles.append([i[0] - 1, i[1] + 1])           #ur
                showntiles.append([i[0], i[1] - 1])                #ml
                showntiles.append([i[0], i[1] + 1])                #mr
                showntiles.append([i[0] + 1, i[1] - 1])              #dl
                showntiles.append([i[0] + 1, i[1]])                 #d
                showntiles.append([i[0] + 1, i[1] + 1])               #dr

            elif i[0] == 0 and not i[1] == 0 and not i[1] == (x - 1):
                showntiles.append([i[0], i[1] - 1])                #mu
                showntiles.append([i[0], i[1] + 1])                #mr
                showntiles.append([i[0] + 1, i[1] - 1])              #dl
                showntiles.append([i[0] + 1, i[1]])                 #d
                showntiles.append([i[0] + 1, i[1] + 1])               #dr
            elif i[0] == 0 and i[1] == 0:
                showntiles.append([i[0], i[1] + 1])                #mr
                showntiles.append([i[0] + 1, i[1]])                 #d
                showntiles.append([i[0] + 1, i[1] + 1])               #dr
            elif not i[0] == 0 and i[1] == 0 and not i[0] == y - 1:
                showntiles.append([i[0], i[1] - 1])                #mu
                showntiles.append([i[0], i[1] + 1])                #mr
                showntiles.append([i[0] + 1, i[1] - 1])              #dl
                showntiles.append([i[0] + 1, i[1]])                 #d
                showntiles.append([i[0] + 1, i[1] + 1])               #dr
            elif i[0] == y and i[1] == 0:
                showntiles.append([i[0], i[1] - 1])                #ml
                showntiles.append([i[0] + 1, i[1] - 1])              #dl
                showntiles.append([i[0] + 1, i[1]])                 #d
            elif i[0] == (y - 1) and i[1] == 0:
                showntiles.append([i[0] - 1, i[1]])             #u
                showntiles.append([i[0] - 1, i[1] + 1])           #ur
                showntiles.append([i[0], i[1] + 1])                #mr
            elif i[0] == (y - 1) and not i[1] == 0 and not i[1] == (x - 1):
                showntiles.append([i[0] - 1, i[1] - 1])        #ul
                showntiles.append([i[0] - 1, i[1]])             #u
                showntiles.append([i[0] - 1, i[1] + 1])           #ur
                showntiles.append([i[0], i[1] - 1])                #ml
                showntiles.append([i[0], i[1] + 1])                #mr
            elif i[0] == (y - 1) and i[1] == (x - 1):
                showntiles.append([i[0] - 1, i[1] - 1])        #ul
                showntiles.append([i[0] - 1, i[1]])             #u
                showntiles.append([i[0], i[1] - 1])                #ml
            elif not i[0] == (y - 1) and not i[0] == 0 and i[1] == (x - 1):
                showntiles.append([i[0] - 1, i[1] - 1])        #ul
                showntiles.append([i[0] - 1, i[1]])             #u
                showntiles.append([i[0], i[1] - 1])                #ml
                showntiles.append([i[0] + 1, i[1]])                 #d
                showntiles.append([i[0] + 1, i[1] + 1])               #dr
            elif i[0] == y and i[1] == (x - 1):
                showntiles.append([i[0], i[1] - 1])                #ml
                showntiles.append([i[0] + 1, i[1] - 1])              #dl
                showntiles.append([i[0] + 1, i[1]])                 #d  

    showntiles = []
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    clock.tick(10)
pygame.quit()
