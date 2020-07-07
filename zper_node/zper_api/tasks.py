from __future__ import absolute_import
from socket import error as socket_error
from decimal import Decimal
from collections import defaultdict
from http.client import CannotSendRequest

from celery import shared_task
from celery.utils.log import get_task_logger
from .zcash_tools import zcashd

from django.db import transaction
from .models import Product, Transaction, Currency

from zper_node import settings

@shared_task(throws=(socket_error,))
#@transaction.atomic
def query_transactions():
    node = zcashd()
    currency = Currency.objects.select_for_update().get(ticker=settings.DEFAULT_CURRENCY)

    current_block = node.proxy.getblockcount()
    print(current_block)
    #block_hash = str(node.proxy.getblockhash(currency.last_block))
    #transactions = node.get_tx_since(block_hash)['transactions']
    for product in Product.objects.all():
        print(product.address)
        transactions = node.get_recieved_by_address(product.address, settings.REQUIRED_CONFS)
        print(transactions)
        for tx in transactions:
            print(tx)
            if tx['blockheight']-settings.REQUIRED_CONFS < currency.last_block:
                print(tx['blockheight']-settings.REQUIRED_CONFS)
                print(currency.last_block)
                continue
            process_tx(tx, product)


    currency.update_last_block(current_block)
    currency.save()

    for tx in Transaction.objects.filter(processed=False):
        query_transaction(tx.txid)

#@transaction.atomic
def process_tx(tx, product):
    print('processing')

    #try:
    #    product = Product.objects.select_for_update().get(address=tx['address'])
    #    print('got product')
    #except Product.DoesNotExist:
    #    print('no product')
    #    return

    tx, created = Transaction.objects.select_for_update().get_or_create(txid=tx['txid'], address=tx['address'], memo=tx['memo'], product=product)

    if tx.processed:
        return

    if created:
        tx.save()

        if tx['confirmations'] >= settings.REQUIRED_CONFS:
            #New, Confirmed tx found -> extract memo, whitelist key
            print('confirmed')
            return tx.validate_purchase()
        else:
            print('not confirmed')
            ## Transaction is unconfirmed check back next block
    else:
        if tx['confirmations'] >= settings.REQUIRED_CONFS:
            ## same as above
            print('confirmed')
            return tx.validate_purchase()
        else:
            print('not confirmed')
            ##same as above
    ##new transaction signal

#@shared_task(throws=(socket_error,))
#@transaction.atomic
#def query_transaction(txid):
#    ##coin get transaction
#    node = zcashd()
#    print(node.get_transaction())
#
#    #for tx in transactions:
#    #    process_tx(tx)
