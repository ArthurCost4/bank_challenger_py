from datetime import datetime
import random

print("""
    Digite o numero correspondente a ação desejada
      [1] Deposito
      [2] Saque
      [3] Extrato

      Não possui conta?  que tal criarmos uma:
      [4] Cadastrar conta bancaria
      [5] Cadastrar Usuario

      [0] Sair
""")

#Useful functions
def formatar_data_nascimento(data_str):
    try:
        # Tentar analisar a string da data
        data = datetime.strptime(data_str, "%d/%m/%Y")
        # Formatar a data como desejado
        data_formatada = data.strftime("%d de %B de %Y")
        return data_formatada
    except ValueError:
        return "Formato de data inválido. Use o formato DD/MM/AAAA."

def formatar_cpf(cpf_str):
    # Remover caracteres não numéricos
    cpf_limpo = ''.join(filter(str.isdigit, cpf_str))

    if len(cpf_limpo) != 11:
        return "CPF inválido. Deve conter 11 dígitos."

    return cpf_limpo

def create_id():
    contador = 1

    def gerar_id():
        nonlocal contador
        id_unico = str(contador).zfill(4)
        contador += 1
        return id_unico
    return gerar_id

gerar_id = create_id()

session_bank =     True

balance =          1000 # saldo
history_balance =  []
withdraw =         []  # saques
my_limit_withdraw = 0

bd_users =         []
bd_accounts =      []

def deposito_func(saldo, valor , extrato, /):
    global balance
    balance += valor
    extrato.append(f'Deposito de R$:{valor} no saldo R$:{valor} resultando R$:{saldo+valor}')

def extrato_func(saldo, /, **kwargs):
    show_extrato = kwargs.get('extrato')
    print(f'Saldo atual {saldo}'.center(50))
    for i in show_extrato:
        print(i)

def saque_func(**saque):
    saldo, valor, extrato, limite, numero_saques, limite_saques = saque.get('saldo'), saque.get('valor'), saque.get('extrato'), saque.get('limite'), saque.get('numero_saques'), saque.get('limite_saques')

    #variaveis globais usadas
    global my_limit_withdraw
    global balance
    global history_balance
    
    # tratamento de erros
    value_above_exceeds, value_above_limit, value_exceeds_withdrawal_days  = False, False, False
    warning_saldo = ''
    if valor > saldo:
        value_above_exceeds = True
        warning_saldo += 'O valor de saque é maior do que o saldo atual\n' 
    if valor > limite:
        value_above_limit = True
        warning_saldo += 'Valor saque excede o limite\n'
    if numero_saques >= limite_saques:
        value_exceeds_withdrawal_days = True
        warning_saldo += 'Voce atingiu o limite de 3 saques diarios\n'

    if value_above_exceeds or value_above_limit or value_exceeds_withdrawal_days:
        print(warning_saldo)
    else:
        numero_saques += 1
        my_limit_withdraw += numero_saques

        extrato = f'Saque de R$:{valor} no saldo R$:{balance} resultando R$:{balance-valor}'
        history_balance.append(extrato)

        balance = balance - valor
    
def create_user(**info):
    name, date, cpf, address = info.get('name'), info.get('date'), info.get('cpf'), info.get('address')
    if name and date and cpf and address:
        print('tudo certo')
        user = dict(
            cpf  =         f'{cpf}',
            date =         f'{date}',
            name =         f'{name}',
            address =      f'{address}',
            account_bank = dict()
            )
        return bd_users.append(user)               
        
    else:
        print('Cago no pau')
    
def create_account(**info):
    agencia, num_account, users = info.get('agencia'), info.get('num_account'), info.get('users')

    identification_account = random.randint(10000, 99999)
    num_account =            identification_account

    entra_cpf =              str(input('Digite o seu CPF: '))
    cpf =                    formatar_cpf(entra_cpf)  

    for dicionario in users:
        if cpf in dicionario.values():
         print(f"Valor '{cpf}' encontrado")
         print(dicionario)
         dicionario['account_bank'] = {'agencia': f'{agencia}', 'num_account': f'{num_account}'}
         break
    else:
        print(f"CPF '{cpf}' não encontrado na lista de usuarios.")

while session_bank:
    LIMIT_WITHDRAW = 500
    LIMIT_WITHDRAW_DAYS = 4
    choice = int(input('O que deseja fazer hoje: '))

    if choice   == 1:
        valor = float(input('Quanto deseja depositar? '))
        deposito_func(balance, valor, history_balance)
    elif choice == 2:
        valor = float(input('Quanto deseja sacar? '))
        saque_func(saldo=1000,
                   valor=valor,
                   extrato=history_balance, 
                   limite=LIMIT_WITHDRAW,
                   limite_saques=LIMIT_WITHDRAW_DAYS,numero_saques=my_limit_withdraw)
    elif choice == 3:
        extrato_func(balance, extrato=history_balance)
    elif choice == 4:
        num_account = 0
        create_account(
            agencia =     gerar_id(),
            num_account = num_account,
            users =       bd_users
        )
    elif choice == 5:
        name = str(input('DIga o nome ai, cabra: '))

        date_birth = str(input('Digite sua data de nascimento (DD/MM/AAAA): '))
        date_birth_formatted = formatar_data_nascimento(date_birth)

        cpf = str(input('Digite o seu cpf: '))
        cpf_sanatized = formatar_cpf(cpf)

        address = str(input('Digite o endereço nesse formato por favor logradouro, nro - bairro - cidade/sigla estado: '))
        create_user(
            name =    name,
            date =    date_birth_formatted,
            cpf  =    cpf_sanatized,
            address = address
        )
        print(bd_users)
    elif choice == 0:
        session_bank = False

