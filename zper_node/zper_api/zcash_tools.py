from zcash import SelectParams
import zcash.rpc
SelectParams('regtest')

class zcashd:
    def __init__(self):
        self.proxy = zcash.rpc.Proxy(service_url='http://user:password@0.0.0.0:38232')

    def new_z_address(self):
        return self.proxy.z_getnewaddress()

    def get_tx_since(self, block):
        return self.proxy.call('listsinceblock', block, 1)

    def get_transaction(self, txid):
        return self.proxy.call('z_viewtransaction', txid)

    def get_recieved_by_address(self, address, minconf):
        return self.proxy.call('z_listreceivedbyaddress', address, minconf)
