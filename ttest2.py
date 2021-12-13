import random
x=0
y=0
hp=100
print('первая комната, кинжал лежит на столе. В комнате 4 двери с каждой стороны')
dej1='взять кинжал'
while hp>0:
    while x==0 and y==0:
        
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
            di=int(input('в какую дверь войти. введите число от 1 до 4'))
            if di==1:
                x=1
    if x==1 and y==0:
        dan=random.randint(1,3)
        tre=random.randint(1,10)
        hpe=random.randint(5,15)
        the=random.randint(1,1)
        tde=random.randint(2,3)
        e=1
        while x==1 and y==0:
            if dan>=1:
                dej1="сражаться"
                dej2='уйти'
                chee="проверить врагов"
                dej=input('введити что хотите сделать. Возможные действия:'+ dej1+', '+dej2+ ', '+ che+', '+chee)
                if dej==chee:
                    print(the, hpe, tde)    
                if dej==dej1:
                    while e>0:
                        while hpe>0:
                            hpe1=hpe
                            dej1='удар'
                            dej2='блок'    
                            dejec=random.randint(1,2)
                            if dejec==1:
                                deje='враг собирается атаковать'
                            else:
                                deje='враг собирается защищатся'
                                dej=input('вы в бою.'+deje+ 'Возможные действия'+dej1+', '+dej2)
                                if dej==dej1:
                                    i=1
                                    for i in range(1,tohit):
                                        dam1=random.randit(1,todam)
                                        dam+=dam1
                                        i=i+1
                                    hpe=hpe-dam
                                    print(hpe)
                                if dejec==1:
                                    hp=hp-tde
                                    print(hp)
                                
                                    
                                
                        
                    
            elif di==2:
                
                y=1
            elif di==3:
                x=-1
            elif di==4:
                y=-1
        else:
            print('некоректная команда')