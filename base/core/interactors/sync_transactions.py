from dataclasses import dataclass
from core.models import Address, Transaction
from blockcypher import get_address_details
from django.core.exceptions import ValidationError
import requests
from copy import copy
import asyncio


TX_LIMIT = 100  # Max tx limit for blockchain.com multi address fetch


@dataclass
class SyncTransactionsInput:
    wallet_id: int


def SyncTransactions(input: SyncTransactionsInput):
    addresses = Address.objects.filter(wallet_id=input.wallet_id)
    address_str = "|".join([address.address_string for address in addresses])
    base_url = f"https://blockchain.info/multiaddr?active={address_str}&n={TX_LIMIT}"

    def write_transactions(transactions, address):
        Transaction.objects.bulk_create(
            [
                Transaction(
                    wallet_id=input.wallet_id,
                    address_id=address.id,
                    transaction_hash=transaction["hash"],
                )
                for transaction in transactions
            ],
            ignore_conflicts=True,
            # We don't have to worry about double inserts due to model level unique constraint
        )

    def fetch_transactions(offset=None):
        url = copy(base_url)
        if offset is not None:
            url += f"&offset={offset}"

        res = requests.request(method="GET", url=url, timeout=4)
        res = res.json()
        return res["txs"]

    # Fetch transaction data and create transacton records
    for address in addresses:
        transactions = fetch_transactions()

        # Write initial batch
        if transactions:
            write_transactions(transactions=transactions, address=address)

            # Write overflow batches
            tx_overflow_count = TX_LIMIT
            iterations = 0  # Manage iterations for demo purposes
            while (
                len(transactions) == TX_LIMIT and iterations < 1
            ):  # Fetch/write in batches if pagination exists
                iterations += 1
                transactions = fetch_transactions(offset=tx_overflow_count)
                if transactions:
                    tx_overflow_count += len(transactions)
                    write_transactions(transactions=transactions, address=address)
