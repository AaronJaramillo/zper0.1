from .models import Product
from .serializers import ProductSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from .permissions import isPaid
from .auth import ZperAPISignatureAuthentication
from .models import Keys

#No Auth Required
class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'name'

#todo
#admin only
class CreateProduct(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ListProduct(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

#def zper_validate_host(func):
#    def validate(request):
#        domain, port = split_domain_port(request.META['HTTP_HOST'])
#        if not validate_host(domain, settings.ZPER_ALLOWED_HOSTS):
#            return HttpResponseForbidden('forbiden')
#        return func(request)
#    return validate

def walletnotify(request):
    query_transaction.delay(request.GET['txid'])
    return HttpResponse('success')

#TODO
#Auth node only
def blocknotify(request):
    query_transactions.delay()
    return HttpResponse('success')

class PremiumEndpoint(APIView):
    authentication_classes = [ZperAPISignatureAuthentication]
    permission_classes = [isPaid]

    def get(self, request, format=None):
        content = {
            'status': 'VIP',
            'content': 'Premium Content here'
        }
        return Response(content)
