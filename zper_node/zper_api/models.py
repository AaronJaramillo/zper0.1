from django.db import models
import datetime
from .zcash_tools import zcashd
import uuid
from Cryptodome.Hash import SHA3_256

# Create your models here.
class Product(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    link = models.URLField()
    price = models.IntegerField(default=1)
    address = models.CharField(max_length=260)
    period = models.DurationField()

    def get_new_zaddress(self):
        return zcashd().new_z_address()

    def create_new_product(self, _name, _link, _price, _period):
        product = Product(name=_name, link=_link, price=_price, address=self.get_new_zaddress(), period=_period)
        product.save()
        return product

class Currency(models.Model):
    ticker = models.CharField(max_length=4, default='ZEC', primary_key=True)
    last_block = models.PositiveIntegerField(blank=True, null=True, default=0)

    def update_last_block(self, blocknum):
        self.last_block = blocknum
        self.save()

        return self.last_block

class Transaction(models.Model):
    txid = models.CharField(max_length=100)
    address = models.CharField(max_length=260)
    amount = models.DecimalField(max_digits=16, decimal_places=2)
    processed = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    memo = models.CharField(max_length=1024, null=True)

    def validate_purchase(self):
        if self.amount >= self.product.price:
            if len(self.memo) == 900:
                if Keys().make_key(self.memo, self.product):
                    self.processed = True
                    self.valid = True
                    self.save()
                    return True
                else:
                    print('Error Creating saving Object')
                    return
            else:
                ## TODO possibly allow for refunds to be claimed with payment proofs. For now no memo is a donation
                self.processed = True
                self.valid = False
                return False
        else:
            ## TODO implement functionality to allow underpaid/expired payments to be topped up via a new transaction with the same memo field.
            ## For now an underpayment is a donation
            self.processed = True
            self.valid = False
            return False


class Keys(models.Model):
    keyId = models.CharField(max_length=64)
    pubkey = models.CharField(max_length=900)
    expirary = models.DateTimeField()
    endpoint = models.URLField()

    def make_key(self, memo, product):
        keyId_obj = SHA3_256.new()
        keyId_obj.update(bytes.fromhex(memo))
        keyId_hex = keyId_obj.hexdigest()
        exp_date = datetime.datetime.now() + product.period
        new_key=Keys(keyId=keyId_hex, pubkey=memo, expirary=exp_date, endpoint=product.link)

        try:
            new_key.save()
            return True
        except IntegrityError:
            return False
    def is_expired(self):
        if datetime.datetime.now >= self.exp_date:
            return True
        else:
            return False

