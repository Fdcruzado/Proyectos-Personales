

U=eval(input('ingrese la cantidad de unidades que desea: '))

if U<26 and U>=1:
    P=U*27.7
    d=0.05
    print("el importe de la compra es "+str(round(P, 2))+ ",el importe del descuento es "+str(round(P*d, 2))+" el importe final de la compra es "+str(round(P*(1-d), 2))) 
  
   
elif U>=26 and U<51:
    P=U*25.5
    d=0.15
    print("el importe de la compra es "+str(round(P, 2))+ ",el importe del descuento es "+str(round(P*d, 2))+" el importe final de la compra es "+str(round(P*(1-d), 2)))  

   
elif U<76 and U>=51:
    P=U*23.5
    d=0.15
    print("el importe de la compra es "+str(round(P, 2))+ ",el importe del descuento es "+str(round(P*d, 2))+" el importe final de la compra es "+str(round(P*(1-d), 2)))   

    
elif  U>=76:
    P=U*21.5
    d=0.15
    print("el importe de la compra es "+str(round(P, 2))+ ",el importe del descuento es "+str(round(P*d, 2))+" el importe final de la compra es "+str(round(P*(1-d), 2)))  

    

