from drf_httpsig.authentication import SignatureAuthentication
from .models import Keys

class ZperAPISignatureAuthentication(SignatureAuthentication):

    def fetch_user_data(self, key_id, algorithm="rsa-sha256"):
        try:
            key = Keys.objects.get(keyId=key_id)
        except Keys.DoesNotExist:
            return (None, None)

        if key.is_expired():
            return (None, None)
        else:
            return (django.contrib.auth.models.AnonymousUser, key.pubkey)

