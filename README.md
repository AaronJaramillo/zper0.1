# zper
Zper is a paywall merchant app, built on django, designed for use with zcash private transactions.

Zper exposes some basic admin APIs for the merchant to create various products with prices, endpoints and expiration times.

Each product, is associated with an endpoint and a z addr. The client simply has to send a payment of a sufficient amount to the z-address for the desired endpoint, including in the memo field a RSA public key.

Zper will store check that the payment has been made and store the public key so that the client make requests to a premium endpoint signed with his private RSA key 
and zper with Authenticate the request and pass along the response. 
