from zcash import SelectParams
import zcash.rpc
#SelectParams('regtest')


def main():
    proxy = zcash.rpc.Proxy(service_url='http://user:password@0.0.0.0:38232', zcash_conf_file='./zcash.conf')
    print(proxy.getinfo())



class znode:

    def __init__(self):
        self.proxy = zcash.rpc.Proxy(service_url='http://user:password@0.0.0.0:38232')

    def getaddressgroupings(self):
        return self.proxy.getbalance(account='*', minconf=1)

print(znode().getaddressgroupings())
#bitcoin.SelectParams('regtest')
#def check_node():
#    proxy = bitcoin.rpc.Proxy(service_url='http://user:password@0.0.0.0:38232')
#    print(proxy.getinfo())
#
#check_node()

