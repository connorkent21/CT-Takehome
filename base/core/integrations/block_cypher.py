from django.conf import settings
import blockcypher as bc

class BlockCypher:
    def __init__(self, coin_symbol="btc"):
        self.token = settings.BC_TOKEN
        self.coin_symbol = coin_symbol

    def get_address(self, address):
        return bc.get_full_address(address)
