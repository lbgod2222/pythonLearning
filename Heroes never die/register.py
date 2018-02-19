'''
Heroes never die
version: 0.0.2
register system
'''
import os
# default set
welcome = 'Welcome'
locktip = "Your account is locked due to times try"
tryagain = "Please try again, wrong password"

# flag of try wrong
trycount = 0
while 1:
    if os.path.isfile('lock.log'):
        print(locktip)
        break
    username = input('name:')
    password = input('password:')
    trycount += 1
    if username == 'abise' and password == '6671303':
        print (welcome)
        break
    else:
        print (tryagain)
        if trycount == 3:
            open('lock.log','w').write(username)
            print (locktip)
            break
