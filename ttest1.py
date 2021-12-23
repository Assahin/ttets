import random
x=0
y=0
hp=0
print('первая комната. В комнате 4 двери с каждой стороны')
dej1='взять компас'
keyy=random.randint(1,5)
keyx=random.randint(1,5)
exy=random.randint(4,5)
exx=random.randint(4,5)
use=''
while hp==0:
    while x==0 and y==0:
        dej2='пойти в другую комнату'
        dej=input('введити что хотите сделать. Возможные действия:'+dej1+', ' +dej2+', '+use)
        if dej=='чит':
            print(keyx,';',keyy,' ', exx,';', exy)
        elif dej==dej1:
            use='использовать компас'
            dej1=''
        elif dej==use:
            print('координаты:',x,';',y)
        elif dej==dej2 and dej!='':
            di=int(input('в какую дверь войти. Север, Юг, Восток, Запад'))
            if di=='Север':
                y=1
            elif di=='Восток':
                x=1
            elif di=='Юг':
                y=-1
            elif di=='Запад':
                x=-1
    while x==1 and y==0:
        a=random.randint(1,4)
        print('в этой комнате ', a,' дверей, учитывая ту, из которой вы вышли.')
        dej=input('введити что хотите сделать. Возможные действия:'+dej1+', ' +dej2+', '+use)
   