from brownie import vault, config , accounts

account = accounts.add(config["wallets"]["from_key"])

def deposit():
    tx1 = account.transfer('0x0E99a7C143c799B74ff5F68eCbBA7EF9846a68b3', ".0001 ether",gas_limit = 100000 ,gas_price = 1)


def main():
    deposit()
