# zper
Zper is a paywall merchant app, built on django, designed for use with zcash private transactions.

Zper exposes some basic admin APIs for the merchant to create various products with prices, endpoints and expiration times.

Each product, is associated with an endpoint and a z addr. The client simply has to send a payment of a sufficient amount to the z-address for the desired endpoint including, in the memo field, a RSA public key.

Zper will check that the payment has been made and store the public key so that the client make requests to a premium endpoint signed with his private RSA key 
and zper with Authenticate the request and pass along the response. 

On the backend Zper is using celery to call the zcashd node and to get notified of new transactions.

An extension of zper could use django 3.0s new ASGI features to authenticate and manage the payments via the django framework but pass off the authenticated requests to a more sophisticated async service for things like live streaming video, or high-frequency/enriched-data API access. Basically, ideally the content and service behind the pay wall could be built on any framework with the zper django app acting as a proxy with some invoicing features.
also would be good to extend to the client side. A sortof specialized thin wallet which knows how to derive these keys and make requests with them.

![alt text](https://raw.githubusercontent.com/AaronJaramillo/zper0.1/master/flowchart/Slide1.jpg)

![alt text](https://raw.githubusercontent.com/AaronJaramillo/zper0.1/master/flowchart/Slide2.jpg)

![alt text](https://raw.githubusercontent.com/AaronJaramillo/zper0.1/master/flowchart/Slide3.jpg)

![alt text](https://raw.githubusercontent.com/AaronJaramillo/zper0.1/master/flowchart/Slide4.jpg)


# TODO
- Set Permisssions for which specific endpoints can be accessed by which key
- Update process_tx to allow for purchasing multiple endpoints from the same pubkey
- update process_tx to allow for a key at or near expirary to be extended simply buy making another payment
- All the Admin views need authentication decorators
- Make PremiumViews and AdminViews classes so they can be easily duplicated
- The block notify endpoint needs to be secured so that only the node can call it
- Dockerize all the services more cleanly so that zper can drop into a microservice application easily
- Change CreateProductAPI view to use create_new_product model function to automatically generate an new z_addr
