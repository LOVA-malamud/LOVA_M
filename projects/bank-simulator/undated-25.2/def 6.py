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
BALANCE = [300, 4000, 100_000, 5000, 0, 900]
PASSWORDS = ['000', '111', '222', '333', '444', '555']
# active   =  [True, True, True, False, False, True] -- bonus

"""
Menu:
1. Login
2. Exit

Login:
  Account number? 2
  Password? 222

Menu:
1. Deposit --> Can deposit up to 10_000 without certificate, above need certificate
2. Withdraw --> Can withdraw and cannot get negative balance
3. Transfer --> Can transfer cannot get negative balance, into a valid account
# 4. Make active  --> Only if not active  -- bonus
# 5. Make not active --> Only if active  -- bonus
6. Exit to main menu
"""


def display_menu_login_exit():
    """Display the main login menu."""
    print('Menu:')
    print('1. Login')
    print('2. Exit')


def get_main_choice():
    """Get user's main menu choice."""
    choice = int(input('Choose 1-2: '))
    return choice


def get_account_number_from_user():
    """Get account number from user."""
    account_number = int(input('What is the account number? '))
    return account_number


def check_if_valid(user_account_number: int, balance_list: list) -> bool:
    """Check if account number is valid."""
    # account      0     1        2     3   4    5
    # balance = [300, 4000, 100_000, 5000, 0, 900] len(balance) = 6
    return 0 <= user_account_number < len(balance_list)


def get_account_password():
    """Get account password from user."""
    password = input('What is your password? ')
    return password


def check_password_correct(user_account_number: int, user_password: str, 
                          password_list: list) -> bool:
    """Check if the provided password is correct."""
    # user_account_number 0
    # '000'
    # passwords = ['000', '111', '222', '333', '444', '555']
    return user_password == password_list[user_account_number]


def display_account_menu():
    """Display the account menu."""
    print('\nAccount Menu:')
    print('1. Deposit')
    print('2. Withdraw')
    print('3. Transfer')
    print('4. Exit to main menu')


def get_account_menu_choice():
    """Get user's account menu choice."""
    choice = int(input('Choose 1-4: '))
    return choice


def get_deposit_amount():
    """Get deposit amount from user."""
    return float(input('Enter deposit amount: '))


def deposit(account_num: int, balance_list: list, amount: float) -> None:
    """Deposit amount into account."""
    if amount > 10000:
        print('Warning: Deposits over 10,000 require certificate!')
    balance_list[account_num] += amount
    print(f'Deposited {amount}. New balance: {balance_list[account_num]}')


def get_withdraw_amount():
    """Get withdrawal amount from user."""
    return float(input('Enter withdrawal amount: '))


def withdraw(account_num: int, balance_list: list, amount: float) -> None:
    """Withdraw amount from account."""
    if balance_list[account_num] - amount < 0:
        print('Insufficient funds!')
    else:
        balance_list[account_num] -= amount
        print(f'Withdrew {amount}. New balance: {balance_list[account_num]}')


def get_transfer_amount():
    """Get transfer amount from user."""
    return float(input('Enter transfer amount: '))


def get_transfer_to_account(balance_list: list) -> int:
    """Get destination account number for transfer."""
    return int(input('Enter account number to transfer to: '))


def transfer(from_account: int, balance_list: list, to_account: int, 
           amount: float) -> None:
    """Transfer amount from one account to another."""
    if balance_list[from_account] - amount < 0:
        print('Insufficient funds for transfer!')
    else:
        balance_list[from_account] -= amount
        balance_list[to_account] += amount
        print(f'Transferred {amount} to account {to_account}. '
              f'New balance: {balance_list[from_account]}')


while True:
    display_menu_login_exit()
    main_choice = get_main_choice()
    if main_choice == 2:
        break
    if main_choice != 1:
        print('Invalid choice')
        continue
    user_account_number = get_account_number_from_user()

    # if not check_if_valid(user_account_number, accounts):
    if not check_if_valid(user_account_number, BALANCE):
        print('Account not valid...')
        continue
    user_password = get_account_password()
    if not check_password_correct(user_account_number, user_password, PASSWORDS):
        print('Wrong password...')
        continue

    while True:
        display_account_menu()
        choice = get_account_menu_choice()
        match choice:
            case 1:
                deposit_amount = get_deposit_amount()
                deposit(user_account_number, BALANCE, deposit_amount)
            case 2:
                withdraw_amount = get_withdraw_amount()
                withdraw(user_account_number, BALANCE, withdraw_amount)
            case 3:
                transfer_amount = get_transfer_amount()
                transfer_to_account = get_transfer_to_account(BALANCE)
                if not check_if_valid(transfer_to_account, BALANCE):
                    print('Account not valid...')
                    continue
                transfer(user_account_number, BALANCE, transfer_to_account, transfer_amount)
            case 4:
                break
            case _:
                print('Invalid choice')

    print('Goodbye...')