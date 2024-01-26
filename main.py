import asyncio
import csv
from starknet_py.cairo.felt import decode_shortstring
from starknet_py.contract import Contract
from starknet_py.hash.address import compute_address
from starknet_py.hash.selector import get_selector_from_name
from starknet_py.net.full_node_client import FullNodeClient
from starknet_py.net.models import StarknetChainId
from starknet_py.net.signer.stark_curve_signer import KeyPair
from starknet_py.net.account.account import Account
from config import ( BRAAVOS_PROXY_CLASS_HASH, BRAAVOS_IMPLEMENTATION_CLASS_HASH, ERC20_ABI,
    ARGENTX_PROXY_CLASS_HASH, ARGENTX_IMPLEMENTATION_CLASS_HASH, ARGENTX_IMPLEMENTATION_CLASS_HASH_NEW, ACCOUNTS)
from settings import TYPE_WALLET, CAIRO_VERSION, STARKNET_TOKENS


async def get_balance(contract_address: int, private_key: str, type_account: str) -> dict:
    key_pair = KeyPair.from_private_key(private_key)
    client = FullNodeClient("https://starknet-mainnet.public.blastapi.io")
    address = _create_account(type_account, key_pair)
    account = Account(
        address=address,
        client=client,
        key_pair=key_pair,
        chain=StarknetChainId.MAINNET,
    )

    contract = get_contract(contract_address, account)
    symbol_data = await contract.functions["symbol"].call()
    symbol = decode_shortstring(symbol_data.symbol)
    decimal = await contract.functions["decimals"].call()
    balance_wei = await contract.functions["balanceOf"].call(address)
    balance = round(balance_wei.balance / 10 ** decimal.decimals, 6)
    print(f"Account: {hex(address)} Balance: {balance}, {symbol}")
    return {"symbol": symbol, "balance": balance, "address": address}


def _create_account(type_account: str, key_pair: KeyPair) -> int:
    if type_account == "argent":
        return _get_argent_address(key_pair)
    elif type_account == "braavos":
        return _get_braavos_account(key_pair)
    else:
        print("Type wallet error! Available values: argent or braavos")
        exit()


def _get_argent_address(key_pair: KeyPair) -> int:
    if CAIRO_VERSION == 0:
        selector = get_selector_from_name("initialize")

        calldata = [key_pair.public_key, 0]

        address = compute_address(
            class_hash=ARGENTX_PROXY_CLASS_HASH,
            constructor_calldata=[ARGENTX_IMPLEMENTATION_CLASS_HASH, selector, len(calldata), *calldata],
            salt=key_pair.public_key,
        )

        return address
    else:
        address = compute_address(
            class_hash=ARGENTX_IMPLEMENTATION_CLASS_HASH_NEW,
            constructor_calldata=[key_pair.public_key, 0],
            salt=key_pair.public_key,
        )

        return address


def _get_braavos_account(key_pair: KeyPair) -> int:
    selector = get_selector_from_name("initializer")

    calldata = [key_pair.public_key]

    address = compute_address(
        class_hash=BRAAVOS_PROXY_CLASS_HASH,
        constructor_calldata=[BRAAVOS_IMPLEMENTATION_CLASS_HASH, selector, len(calldata), *calldata],
        salt=key_pair.public_key,
    )

    return address

def get_contract(contract_address: int, account) -> Contract:
    return Contract(address=contract_address, abi=ERC20_ABI, provider=account)


def get_wallets():
    wallets = [
            {
                "id": _id,
                "private_key": key,
            } for _id, key in enumerate(ACCOUNTS, start=1)
                ]

    return wallets


async def main():
    wallets = get_wallets()
    print(f"Проверяю баланс {len(wallets)} кошельков...\n")
    results = {"Addresses": {}, "Tokens": {token_symbol: [] for token_symbol in STARKNET_TOKENS.keys()}}
    sleep_time = 1

    for account in wallets:
        await get_balance_task(account["id"], account["private_key"], sleep_time, results)

    with open("res.csv", mode="w", newline="") as csv_file:
        fieldnames = ["Address"] + list(STARKNET_TOKENS.keys())
        writer = csv.writer(csv_file, delimiter=';')
        writer.writerow(fieldnames)
        for address, index in results["Addresses"].items():
            row = [address]
            for token_symbol in STARKNET_TOKENS.keys():
                row.append(results["Tokens"][token_symbol][index] if address in results["Addresses"] else "")
            writer.writerow(row)
    print(f"Результат проверки баланс {len(wallets)} кошельков записан в файл res.csv \n")
    print("                 Тебе понравилось? ʕ ᵔᴥᵔ ʔ \n", )
    print("             FeedBacK : https://t.me/MyKlondike  \n", )
    print("             Чат 🐸:  https://t.me/KlondikeCo  \n", )
    print("         🍩: 0xe93081718a75818Be2eB1E1336c8c2AC930e44e0  ", )


async def get_balance_task(_, private_key, sleep_time, results):
    token_data = {token_symbol: [] for token_symbol in STARKNET_TOKENS.keys()}

    for token_symbol, token_address in STARKNET_TOKENS.items():
        result = await get_balance(token_address, private_key, TYPE_WALLET)
        address_hex = hex(result["address"])
        results["Addresses"].setdefault(address_hex, len(results["Addresses"]))
        token_data[token_symbol].append(result["balance"])

    await asyncio.sleep(sleep_time)

    for token_symbol in STARKNET_TOKENS.keys():
        results["Tokens"][token_symbol].extend(token_data[token_symbol])


if __name__ == "__main__":
    asyncio.run(main())
