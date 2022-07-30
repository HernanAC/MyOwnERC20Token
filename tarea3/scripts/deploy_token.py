from brownie import accounts, config, TokenERC20


initial_supply = 1000000000000000000000  # 1000
token_name = "Cruzcoin"
token_symbol = "CZC"


def main():
    account = accounts.add(config["wallets"]["from_key"])
    erc20 = TokenERC20.deploy(
        initial_supply, token_name, token_symbol, {"from": account}, publish_source=True 
    )