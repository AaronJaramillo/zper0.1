from rest_framework import permissions
from .models import Keys

class isPaid(permissions.BasePermission):

    def has_permission(self, request, view):
        print(request.user)
        #print(request.headers.keyId)
        #key = request.keyid
        #key_obj = Keys.objects.get(keyId=key)
        #uri_endpoint = request.build_absolute_uri()
        #if uri_endpoint == key_obj.product.link:
        #    return True
        #else:
        #    return False
        return True


