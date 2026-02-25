ICONS = {
    "bank": "🏦",
    "login": "🔐",
    "ok": "✅",
    "no": "❌",
    "menu": "📋",
    "money": "💸",
    "deposit": "➕",
    "withdraw": "➖",
    "transfer": "🔁",
    "balance": "💰",
    "user": "👤",
    "history": "🧾",
    "exit": "🚪",
    "warn": "⚠️",
}

# account      0     1        2     3   4    5
balance = [300, 4000, 100_000, 5000, 0, 900]
passwords = ['000', '111', '222', '333', '444', '555']
# active   =  [True, True, True, False, False, True] -- bonus

'''
menu:
1. login
2. exit

login:
  account number? 2
  password? 222

menu:
1. deposit --> can deposit up to 10_000 without certificate, above need certificate
2. withdraw --> can withdraw and cannot get negative balance
3. transfer --> can transfer cannot get negative balance, into a valid account
# 4. make active  --> only if not active  -- bonus
# 5. make not active --> only if active  -- bonus
6. exit to main menu
'''


def display_menu_login_exit():
    print('Menu:')
    print('1. Login')
    print('2. Exit')


def get_main_choice():
    choice = int(input('Choose 1-2:'))
    return choice


def get_account_number_from_user():
    account_number = int(input('whats the account number?'))
    return account_number


def check_if_valid(user_account_number: int, balance: list):
    # account      0     1        2     3   4    5
    # balance = [300, 4000, 100_000, 5000, 0, 900] len(balance) = 6
    if 0 <= user_account_number < len(balance):
        valid = True
    else:
        valid = False
    return valid

    # return 0 <= user_account_number < len(balance):


def get_account_password():
    password = input('whats your password?')
    return password


def check_password_correct(user_account_number, user_password, passwords):
    # user_account_number 0
    # '000'
    # passwords = ['000', '111', '222', '333', '444', '555']
    if user_password == passwords[user_account_number]:
        return True
    else:
        return False

    # return user_password == passwords[user_account_number]


def display_account_menu():
    print('\nAccount Menu:')
    print('1. Deposit')
    print('2. Withdraw')
    print('3. Transfer')
    print('4. Exit to main menu')


def get_account_menu_choice():
    choice = int(input('Choose 1-4: '))
    return choice


def get_deposit_amount():
    return float(input('Enter deposit amount: '))


def deposit(account_num, balance_list, amount):
    if amount > 10000:
        print('Warning: Deposits over 10,000 require certificate!')
    balance_list[account_num] += amount
    print(f'Deposited {amount}. New balance: {balance_list[account_num]}')


def get_withdraw_amount():
    return float(input('Enter withdrawal amount: '))


def withdraw(account_num, balance_list, amount):
    if balance_list[account_num] - amount < 0:
        print('Insufficient funds!')
    else:
        balance_list[account_num] -= amount
        print(f'Withdrew {amount}. New balance: {balance_list[account_num]}')


def get_transfer_amount():
    return float(input('Enter transfer amount: '))


def get_transfer_to_account(balance_list):
    return int(input('Enter account number to transfer to: '))


def transfer(from_account, balance_list, to_account, amount):
    if balance_list[from_account] - amount < 0:
        print('Insufficient funds for transfer!')
    else:
        balance_list[from_account] -= amount
        balance_list[to_account] += amount
        print(f'Transferred {amount} to account {to_account}. New balance: {balance_list[from_account]}')


while True:
    display_menu_login_exit()
    main_choice = get_main_choice()
    if main_choice == 2:
        break
    if main_choice != 1:
        print('invalid choice')
        continue
    user_account_number = get_account_number_from_user()

    # if not check_if_valid(user_account_number, accounts):
    if check_if_valid(user_account_number, balance) == False:
        print('account not valid...')
        continue
    user_password = get_account_password()
    if check_password_correct(user_account_number, user_password, passwords) == False:
        print('wrong password...')
        continue

    while True:
        display_account_menu()
        choice = get_account_menu_choice()
        match choice:
            case 1:
                deposit_amount = get_deposit_amount()
                deposit(user_account_number, balance, deposit_amount)
            case 2:
                withdraw_amount = get_withdraw_amount()
                withdraw(user_account_number, balance, withdraw_amount)
            case 3:
                transfer_amount = get_transfer_amount()
                transfer_to_account = get_transfer_to_account(balance)
                if check_if_valid(transfer_to_account, balance) == False:
                    print('account not valid...')
                    continue
                transfer(user_account_number, balance, transfer_to_account, transfer_amount)
            case 4:
                break
            case _:
                print('invalid choice')

    print('Goodbye ...')