from brownie import network, accounts, config, Contract, TokenERC20

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["hardhat", "development", "mainnet-fork"]


def main():
    account = accounts.add(config["wallets"]["from_key"])
    erc20_address = "0xA427C8E4e3dfB0c8980C1a5E2cf66841A0e38d4e"

    erc20 = Contract.from_abi("Arbitrary ERC20", erc20_address, abi=TokenERC20.abi)
    erc20.approve("0x85185F1ee0a358c9E6Bb0bcc117B713f0e515d3a", 999999999999999999999999999999999999,{ "from": account})

