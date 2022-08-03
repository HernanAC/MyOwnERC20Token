from brownie import network, accounts, config, Contract, TokenERC20
from scripts.helpful_scripts import get_account
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["hardhat", "development", "mainnet-fork"]


def main():
    account = accounts.add(config["wallets"]["from_key"])
    erc20_address = "0xA427C8E4e3dfB0c8980C1a5E2cf66841A0e38d4e"
    recipient = "0xA11edA9Fa1CbE8948018fF028C2902BEfEb444FA"
    # This will be how many tokens to send in WEI
    amount = 1000000000000000000  # 1 token
    erc20 = Contract.from_abi("Arbitrary ERC20", erc20_address, abi=TokenERC20.abi)
    tx = erc20.transfer(recipient, amount, {"from": account})

