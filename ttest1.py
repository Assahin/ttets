import random
x=0
y=0
hp=100
print('первая комната, кинжал лежит на столе. В комнате 4 двери с каждой стороны')
while hp>0:
    if x==0 and y==0:
        dej1='взять кинжал'
        dej2='пойти в другую комнату'
        dan=0
        tre=1
        che='проверить уровень опасности'
        dej=input('введити что хотите сделать. Возможные действия:'+ dej1+', '+dej2+ ', '+ che)
        if dej==dej1 and dej1!='':
            eqv='кинжал. 2d4 '
            print('вы подобрали кинжал')
            dej1=''
            tohit=2
            todam=4
        elif dej== che:
            print(dan, tre)
        elif dej==dej2 and dej!='':
            di=input('в какую дверь войти. введите число от 1 до 4')
            if di==1:
                x=1
                dan=random.randit(1,3)
                tre=random.randit(1,10)
                hpe=random.randit(10,20)
                the=random.randit(1,2)
                tde=random.randit(3,4)
            elif di==2:
                y=1
            elif di==3:
                x=-1
            elif di==4:
                y=-1
        else:
            print('некоректная команда')