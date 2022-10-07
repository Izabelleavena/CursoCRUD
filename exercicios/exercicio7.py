salario = float(input('digite seu salário atual:'))

if salario < 500:
    media = (salario * 15) / 100 
    salarionovo = salario + media
    print( 'seu novo salario é de', salarionovo);
elif salario >= 500 and salario <= 1000 :
     media = (salario * 10) / 100 
     salarionovo = salario + media
     print( 'seu novo salario é de', salarionovo);
else:    
     media = (salario * 5) / 100 
     salarionovo = salario + media
     print( 'seu novo salario é de', salarionovo);