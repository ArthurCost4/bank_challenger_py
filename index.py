print("""
    Digite o numero correspondente a ação desejada
      [1] Deposito
      [2] Saque
      [3] Extrato

      [0] Sair
""")

session_bank = True
balance = 0    # saldo
history_balance = []

withdraw = []   # saques

while session_bank:
   
    LIMIT_WITHDRAW = 500
    LIMIT_WITHDRAW_DAYS = 3

    choice = int(input('O que deseja fazer hoje: '))

    if choice == 1:
        balance_add = float(input('Digite o valor desejado: '))

        if balance_add > 0:
           balance = balance + balance_add
           print(f'Deposito de R$:{balance_add} feito com sucesso! saldo atual R$: {balance}')
        else:
           print('Digite um valor valido, por favor')
        
    elif choice == 2:
        removal = float(input('Digite o valor desejado para retirada: '))

        if (removal > 0) and (removal <= LIMIT_WITHDRAW) and (removal <= balance):
            if len(withdraw) < LIMIT_WITHDRAW_DAYS:
                withdraw.append(removal)
                balance -= removal
                history_balance.append(balance)
                print(f'Saque de {removal} feito com sucesso!')
            else:
                print(f'Limite de 3 saques diarios excedido')
        else:
            print('Não é possivel fazer o saque com esse valor, por favor verifique se o seu saldo é suficiente e se é menor ou igual a 500 reais')
        
    elif choice == 3:
        print(f'Saldo atual: R$: {balance}')

        if len(withdraw) > 0:
             print(f'Foram feito(s) {len(withdraw)} saques, segue as ações:')
             
             count = 0
             for i in withdraw:
                 print(f'- Retirada de R$:{i}, que resultou em R$:{history_balance[count]} restantes')
                 count += 1
             
    elif choice == 0:
        print('Saindo')
        session_bank = False
    else:
        print('Opção invalida, por favor escolha uma das seguintes')