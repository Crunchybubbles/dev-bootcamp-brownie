from brownie import vault, config , accounts

def main():
    account = accounts.add(config["wallets"]["from_key"])
    vault.deploy({'from': account})
