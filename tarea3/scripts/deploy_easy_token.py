from brownie import accounts, config, EasyToken


initial_supply = 1000000000000000000000  # 1000
token_name = "Cruzcoin"
token_symbol = "CZC"


def main():
    account = accounts[0]
    erc20 = EasyToken.deploy({"from": account})