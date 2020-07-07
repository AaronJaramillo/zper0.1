from zcash import SelectParams
import zcash.rpc
SelectParams('regtest')
class zcashd_control:
    def __init__(self):
        self.proxy = zcash.rpc.Proxy(service_url='http://user:password@0.0.0.0:38232')

    def new_t_address(self):
        return self.proxy.getnewaddress()

    def send_to_address(self, address, amount):
        return self.proxy.call('sendtoaddress', address, amount)

    def generate(self, numblocks):
        return self.proxy.generate(numblocks)

    def send_to_z_address(self, fromaddress, amounts):
        return self.proxy.z_sendmany(fromaddress, amounts, minconf=1, fee=0.0001)

    #def generatetoaddress(self, numblocks, address):
    #    return self.proxy.call('generatetoaddress', numblocks, address)
