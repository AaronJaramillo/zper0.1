# zper
Zper is a paywall merchant app, built on django, designed for use with zcash private transactions.

Zper exposes some basic admin APIs for the merchant to create various products with prices, endpoints and expiration times.

Each product, is associated with an endpoint and a z addr. The client simply has to send a payment of a sufficient amount to the z-address for the desired endpoint including, in the memo field, a RSA public key.

Zper will check that the payment has been made and store the public key so that the client make requests to a premium endpoint signed with his private RSA key 
and zper with Authenticate the request and pass along the response. 

On the backend Zper is using celery to call the zcashd node and to get notified of new transactions.

An, extension of zper could use django 3.0s new ASGI features to authenticate and manage the payments via the django framework but pass off the authenticated requests to a more sophisticated async service for things like live streaming video, or high-frequency/enriched-data API access. Basically, ideally the content and service behind the pay wall could be built on any framework with the zper django app acting as a proxy with some invoicing features.

