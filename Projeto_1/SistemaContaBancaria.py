saque=valor=0
while True:
    operacao=input(("D - Depositar\nS - Sacar\nV - Visualizar o extrato\n"))
    operacao.upper()
    if(operacao=="D"):
        valor=float(input("Deposite algum valor: "))
    elif(operacao=="S"):
        cont=0
        while(cont<=3):
            saque=float(input("Sacar o valor de: "))
            if((saque-valor)>0 and saque<=500):
                cont+=1
            elif(valor<=0):
                print("Não será possivel sacar por falta de saldo")
            elif(saque>500):
                print("Limite de R$ 500")
    elif(operacao=="V"):
        if(saque==0 and valor==0):
            print("Não foram realizadas movimentações")
        else:
            print("Extrato de: {:1.2f}".format(valor-saque))
        break
        
