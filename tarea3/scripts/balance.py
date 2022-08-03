from brownie import TokenERC20

def read():
    token = TokenERC20[-1]
    print(f"Cuenta a consultar: ")
    cuenta = input()
    balance = token.balanceOf(cuenta)
    print(f"La cantidad de CZC de la cuenta es de : {balance}")

def main():
    read()