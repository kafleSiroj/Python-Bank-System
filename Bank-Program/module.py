def balance(bal):
    if bal >= 1_000_000:
        return f"Your Bank balance is: ${bal / 1_000_000:.1f}m"
    elif bal >= 1_000:
        return f"Your Bank balance is: ${bal / 1_000:.1f}k"
    else:
        return f"Your Bank balance is: ${bal}"

def parse_amount(amount):
    """Parse input for shorthand notation (e.g., 'k' for thousands, 'm' for millions)."""
    if amount.endswith('k') or amount.endswith('K'):
        return int(float(amount[:-1]) * 1000)
    elif amount.endswith('m') or amount.endswith('M'):
        return int(float(amount[:-1]) * 1_000_000)
    elif amount.isdigit():
        return int(amount)
    else:
        return None

def deposit(bal):
    while True:
        dep = input('How much to deposit (use k for thousands, m for millions): $')
        amount = parse_amount(dep)
        if amount is not None:
            bal += amount
            print(f"Successfully deposited ${amount}.")
            return bal
        else:
            print("Invalid amount. Please enter a valid number or use 'k' or 'm'.")

def withdraw(bal):
    while True:
        wit = input('How much to withdraw (use k for thousands, m for millions): $')
        amount = parse_amount(wit)
        if amount is not None:
            if amount > bal:
                print("Insufficient funds.")
            else:
                bal -= amount
                print(f"Successfully withdrew ${amount}.")
                return bal
        else:
            print("Invalid amount. Please enter a valid number or use 'k' or 'm'.")

def main():
    bal = 0  # Initialize the balance
    while True:
        print('''
                Bank
          ****************
          1. Show Balance
          2. Deposit
          3. Withdraw
          4. Exit
          ****************
          ''')
        option = input('Enter your choice (1-4): ')

        while not option.isdigit() or not (1 <= int(option) <= 4):
            option = input('Enter valid choice (1-4): ')

        option = int(option)

        match option:
            case 1:
                print(balance(bal))
            case 2:
                bal = deposit(bal)
            case 3:
                bal = withdraw(bal)
            case 4:
                print("Exiting the bank system. Goodbye!")
                break
