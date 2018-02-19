from heroes import *
# run it
if __name__=="__main__":
    abise = Hero('abise')
    Turbo = Hero('Turbo')
    print(Turbo.hp)
    abise.hit(Turbo)
    print(Turbo.hp)