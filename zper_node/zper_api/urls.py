from django.urls import path, include
from . import views

from rest_framework.authtoken.views import obtain_auth_token

app_name = 'zper_api'

urlpatterns = [
    path(
        'products',
        views.ListProduct.as_view(),
        name='list-products'
    ),
    path(
        'products/',
        views.CreateProduct.as_view(),
        name='create-products'
    ),
    path(
        'products/<str:name>/',
        views.ProductDetail.as_view(),
        name='get-products'
    ),
    path(
        'blocknotify/',
         views.blocknotify,
         name='zper-blocknotify'
         ),

    path(
        'walletnotify/$',
         views.walletnotify,
         name='zper-walletontify'
    ),
    path(
        'premiumguapshit/',
        views.PremiumEndpoint.as_view(),
        name='premiumguapshit'
    )

]
