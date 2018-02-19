'''
name: heroes never die
part: heroes init
version: 0.0.2
author: Ben
'''
# default infomations
welcome = 'Welcome to heroes never die!'
standrad = {'hp': 100, 'atk': 10, 'def': 10, 'dex': 8, 'crt': 0.1}
# game map set
gamemap = ['#','#','#','#','#','#','#']
point = 0
print(welcome)

standrad['name'] = input('Type your nick:')
# default name slot
if not standrad['name']:
    standrad['name'] = 'Black'
print('Your infomation is:', standrad)

# control
while 1:
    userinput = input('go or quit :')
    if userinput == 'd' and point < len(gamemap)-1:
        gamemap[point] = '#'
        point += 1
        gamemap[point] = '*'
        print(gamemap)
        print('move right')
    if userinput == 'a' and point > 0:
        gamemap[point] = '#'
        point -= 1
        gamemap[point] = '*'
        print(gamemap)
        print('move left')
    if userinput != 'a' or userinput != 'd':
        print('Input wrong !')
    # if point = len(gamemap)-1 or point 0