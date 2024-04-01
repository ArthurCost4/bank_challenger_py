print("""
    Digite o numero correspondente a ação desejada
      [1] Deposito
      [2] Saque
      [3] Extrato

      [0] Sair
""")

session_bank = True

while session_bank:
    balance = 0    # saldo
    withdraw = []   # saques

    LIMIT_WITHDRAW = 500
    LIMIT_WITHDRAW_DAYS = 3

    choice = int(input('O que deseja fazer hoje: '))

    if choice == 1:
        print('Deposito')
        
    elif choice == 2:
        print('Saldo')
        
    elif choice == 3:
        print('Extrato')
        
    elif choice == 0:
        print('Saindo')
        session_bank = False
    else:
        print('Opção invalida, por favor escolha uma das seguintes')