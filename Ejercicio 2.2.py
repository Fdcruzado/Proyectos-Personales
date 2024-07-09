Dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]
day = ['L', 'M', 'W', 'J', 'V', 'S']

for i, j in zip(day, Dias):
    if day.index(i) == Dias.index(j) :
        print(i + ": ", j)
        
D=input('Elegir dia en el que trabajó: ')
H=eval(input('Ingrese la cantidad de horas que trabajó: '))

for k in day:
    if k==D:
        PD=day.index(k)

        if (PD)==0 or (PD)==2 or (PD)==4 :
            if H<=8 :
                HE=H-8
                SE=0
                S=(H)*10
                print("Por ser "+Dias[PD]+" el pago por horas extras es S/."+str(SE)+" y el pago es S/."+str(round(S, 2)))
            elif H>8:
                HE=H-8
                SE=HE*15
                S=(8)*10+SE
                print("Por ser "+Dias[PD]+" el pago por horas extras es S/."+str(SE)+" y el pago total es S/."+str(round(S, 2)))
        elif (PD)==1 or (PD)==3 or (PD)==5 :
            if H<=8 :
                HE=H-8
                SE=0
                S=(8)*10+SE
                print("Por ser "+Dias[PD]+" el pago por horas extras es S/."+str(SE)+" y el pago es S/."+str(round(S, 2)))
            elif H>8:
                HE=H-8
                SE=HE*20
                S=(8)*10+SE
                print("Por ser "+Dias[PD]+" el pago por horas extras es S/."+str(SE)+" y el pago es S/."+str(round(S, 2)))

    

