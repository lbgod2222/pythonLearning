class Hero:
    def __init__(self,name='untitled',hp=100,ack=10):
        self.name = name
        self.hp = hp
        self.ack = ack
        print('Hero %s borned!' % self.name)

    def hit(self,name):
        name.hp -= self.ack

class Boss:
    def __init__(self,name='boss',hp=500,ack=30):
        self.name = name
        self.hp = hp
        self.ack = ack
        print('Boss %s borned!' % self.name)
