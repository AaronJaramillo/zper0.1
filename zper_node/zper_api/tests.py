from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Product, Currency, Transaction, Keys
from . import views
import datetime
from .zcash_tools import zcashd
from .zcashd_controller import zcashd_control
from .tasks import query_transactions
import codecs
import requests
from httpsig.requests_auth import HTTPSignatureAuth
KEY_ID = '6d9b4ad37e57f4cc7d2419384639d677e2345bda33add7a8f283ed0da2a61f41'
SECRET = open('./zper_api/secret_test_key/private.pem', 'rb').read()
## Create your tests here.
#
#class ProductsApiTestCase(APITestCase):
#    def setUp(self):
#        self.product1 = Product(name='Article1', link='http://article.com', price=1, address='zs1389423', period=datetime.timedelta(days=7))
#        self.product1.save()
#
#        self.product2 = Product().create_new_product("Article2", "http://article2.com", 1, datetime.timedelta(days=7))
#        self.currency = Currency(ticker='ZEC').save()
#
#
#
#class TestZperApi(APITestCase):
#
#    def test_create_product(self):
#        url = '/api/products/'
#        data = {'name': 'Article',
#                'link': 'http://article.com',
#                'price': 1,
#                'address': 'zs1389423',
#                'period': datetime.timedelta(days=7)}
#        response = self.client.post(url, data, format='json')
#        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#        self.assertEqual(Product.objects.count(), 1)
#
#class TestZperProductApi(ProductsApiTestCase):
#
#    def test_list_products(self):
#        url = '/api/products'
#        response = self.client.get(url)
#        print(response.json())
#        self.assertEqual(1, 1)
#
#    def test_detail_product(self):
#        url = '/api/products/' + 'Article1/'
#        response = self.client.get(url)
#        print(response.json())
#        self.assertEqual(1,1)
#
#class TestTransactionModel(ProductsApiTestCase):
#    def setUp(self):
#        super().setUp()
#        self.tx = Transaction(txid='18230FEAB', address=self.product2.address, amount=1, product=self.product2, memo='2d2d2d2d2d424547494e205055424c4943204b45592d2d2d2d2d0a4d494942496a414e42676b71686b6947397730424151454641414f43415138414d49494243674b434151454172584d422b747242434f4f73336f38475678576e0a694e6b76533642703644326962524e4d31376c3573574b4a4d3565743234694967336f4a2b4170615a4f6f444f7156446b4c66732b3253617969432f566957620a676f3862485a576f715a3745574b47624d475072304c6738366d4a6a6f6a507074522f7776463454492f4934494e64486f4863765a516f77346f5568365854660a6c7030413248626a537a64547543696b39526d3442304556766b4f616c4665793631437866334f4f2b593675484777656771615753623643736d456c57324b360a346a667163584d6f46556d6d4f4f3552784532677633735532363936652f772b3068377932647033795633765069637345676766554b526c616a5236435375540a4c592b444f6164436b6c555637485a654d4864316661547a394432394869384b55646477353468563232725656657a68617278512f316c6c707336654e426b570a43514944415141420a2d2d2d2d2d454e44205055424c4943204b45592d2d2d2d2d')
#        self.tx.save()
#
#    def test_validate_purchase(self):
#        self.tx.validate_purchase()
#        key =  Keys.objects.get(pubkey=self.tx.memo)
#        print(key.pubkey)
#        print(key.keyId)
#        print('###### THIS ONE FOR VALIDATING PURCHASES')
#
#class TestZcashd(TestCase):
#
#    def test_new_z_address(self):
#        node = zcashd()
#        print(node.new_z_address())
#
#    def test_get_tx_since(self):
#        node = zcashd()
#        node.get_tx_since('0604a7350f44255f87e7ab045a4eaae2c4a824f8ecb9eec26ad713132a31dea4')
#
#
#class TestZcashdControl(ProductsApiTestCase):
#
#    def setUp(self):
#        self.node = zcashd_control()
#        self.taddr = self.node.new_t_address()
#
#    def test_generate(self):
#        node = zcashd_control()
#        print(node.generate(4))
#
#    def test_send_to_address(self):
#        node = zcashd_control()
#        print(node.send_to_address(str(self.taddr), 1))
#        node.generate(4)
#
#    #def test_generate_to_address(self):
#    #    address = str(self.node.proxy.getnewaddress())
#    #    print(self.node.generatetoaddress(10, address))
#
#class TestCurrencyModel(APITestCase):
#
#    def setUp(self):
#        self.currency = Currency(ticker='ZEC')
#
#    def test_update_last_block(self):
#        self.currency.update_last_block(3)
#        self.assertEqual(3, self.currency.last_block)
#
#class TestTasks(ProductsApiTestCase):
#
#    def setUp(self):
#        super().setUp()
#        self.node_control = zcashd_control()
#        self.node = zcashd()
#        self.zaddr = self.node.new_z_address()
#        self.taddr = self.node_control.new_t_address()
#        self.node_control.send_to_address(str(self.taddr), 1)
#        memo = codecs.encode(bytes('ZCASH', 'ascii'), 'hex').decode()
#        self.node_control.send_to_z_address(self.taddr, [{
#            "address": self.zaddr,
#            "amount": 0.5,
#            "memo": memo
#        }])
#
#    def test_query_transactions(self):
#        query_transactions.delay()
#        txs = Transaction.objects.all()
#        print(txs.values())
#        print(Transaction.objects.count())
#
class TestAuthentication(APITestCase):

    def setUp(self):
        self.product1 = Product().create_new_product('Article1', 'http://localhost:8000/api/premiumguapshit/', 1, datetime.timedelta(days=7))
        self.currency = Currency(ticker='ZEC').save()
    def test_get_z_addr(self):
        url = '/api/products/Article1/'
        response = self.client.get(url)
        z_addr = response.json()['address']
        print(z_addr)
        print(response.json())
        self.assertEqual(z_addr, self.product1.address)

    def test_transaction(self):
        tx = Transaction(txid='18230FEAB', address=self.product1.address, amount=1, product=self.product1,
                         memo='2d2d2d2d2d424547494e205055424c4943204b45592d2d2d2d2d0a4d494942496a414e42676b71686b6947397730424151454641414f43415138414d49494243674b434151454172584d422b747242434f4f73336f38475678576e0a694e6b76533642703644326962524e4d31376c3573574b4a4d3565743234694967336f4a2b4170615a4f6f444f7156446b4c66732b3253617969432f566957620a676f3862485a576f715a3745574b47624d475072304c6738366d4a6a6f6a507074522f7776463454492f4934494e64486f4863765a516f77346f5568365854660a6c7030413248626a537a64547543696b39526d3442304556766b4f616c4665793631437866334f4f2b593675484777656771615753623643736d456c57324b360a346a667163584d6f46556d6d4f4f3552784532677633735532363936652f772b3068377932647033795633765069637345676766554b526c616a5236435375540a4c592b444f6164436b6c555637485a654d4864316661547a394432394869384b55646477353468563232725656657a68617278512f316c6c707336654e426b570a43514944415141420a2d2d2d2d2d454e44205055424c4943204b45592d2d2d2d2d')
        tx.save()
        tx.validate_purchase()
        key = Keys.objects.get(pubkey=tx.memo)
        self.assertEqual(key.keyId, '6d9b4ad37e57f4cc7d2419384639d677e2345bda33add7a8f283ed0da2a61f41')

class TestAccessPremiumEndpoint(TestAuthentication):
    def setUp(self):
        super().setUp()
        tx = Transaction(txid='18230FEAB', address=self.product1.address, amount=1, product=self.product1, memo='2d2d2d2d2d424547494e205055424c4943204b45592d2d2d2d2d0a4d494942496a414e42676b71686b6947397730424151454641414f43415138414d49494243674b434151454172584d422b747242434f4f73336f38475678576e0a694e6b76533642703644326962524e4d31376c3573574b4a4d3565743234694967336f4a2b4170615a4f6f444f7156446b4c66732b3253617969432f566957620a676f3862485a576f715a3745574b47624d475072304c6738366d4a6a6f6a507074522f7776463454492f4934494e64486f4863765a516f77346f5568365854660a6c7030413248626a537a64547543696b39526d3442304556766b4f616c4665793631437866334f4f2b593675484777656771615753623643736d456c57324b360a346a667163584d6f46556d6d4f4f3552784532677633735532363936652f772b3068377932647033795633765069637345676766554b526c616a5236435375540a4c592b444f6164436b6c555637485a654d4864316661547a394432394869384b55646477353468563232725656657a68617278512f316c6c707336654e426b570a43514944415141420a2d2d2d2d2d454e44205055424c4943204b45592d2d2d2d2d')
        tx.save()
        tx.validate_purchase()
    def test_signed_request(self):
        signature_headers = ['(request-target)', 'accept', 'date', 'host']
        headers = {
            'Host': 'localhost:8000',
            'Accept': 'application/json',
            'Date': "Mon, 6 Jul 2020 10:11:00 GMT"
        }
        auth = HTTPSignatureAuth(key_id=KEY_ID, secret=SECRET, algorithm='rsa-sha256', headers=signature_headers)
        data = {
            'auth': auth,
            'headers': headers
        }
        response = self.client.get('http://localhost:8000/api/premiumguapshit/', data, format='json')
        print(response.json())
        self.assertEqual(response.json()['status'], 'VIP')
