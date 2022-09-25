"""
Calculator
"""
#
#
# def calculator():
#     num1, num2, op = input('write first num: '), int(input('write second num: ')), input(
#         'write operation(+, -, /, *): ')
#     if num1 == 'quit':
#         return False
#     else:
#         if op == '+':
#             return num1 + num2
#         elif op == '-':
#             return num1 - num2
#         elif op == '/':
#             return num1 / num2
#         elif op == '*':
#             return num1 * num2
#
#
# while True:
#     result = calculator()
#     if result:
#         print(result)
#     else:
#         break


def intro():
    name = input('What is your name: ')
    print(f'Welcome to our bank mr/ms {name}')


def show_balance(balance):
    print(f'Your balance is {balance}$')


def withdraw(balance):
    money_to_withdraw = int(input('Write the amount of money you want to withdraw: '))
    result_withdraw = balance - money_to_withdraw
    if money_to_withdraw > balance:
        return f'{balance} is your current balance. Couldn\'t make trans-action'
    elif money_to_withdraw <= balance:
        return result_withdraw


def deposit(balance):
    money_to_deposit = int(input('Write amount of money you want to add: '))
    return balance + money_to_deposit


def main():
    balance = 1200
    intro()
    while True:
        action = input('choose action: 1 - show balance 2 - withdraw 3 - deposit 4 - quit: ')

        if action == '1':
            show_balance(balance)
        elif action == '2':
            balance = withdraw(balance)
            print(balance)
        elif action == '3':
            balance = deposit(balance)
            print(balance)
        elif action == '4':
            break


if __name__ == '__main__':
    main()
