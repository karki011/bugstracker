# Strapi

{% hint style="warning" %}
**At the moment, only a Strapi to Strapi sync is supported. The Strapi Transformers are not fully functional.**  
{% endhint %}

**I**mpulse expects users to use the UID field provided in strapi as a UUID for contents. Rather than rely on the auto incrementing ID of contents use the UID field and provide every content a UUID so that it can be queried and searched for. This is not only the best way to work with Impulse, but also the best way to build your Strapi deployment.   
  
Strapi follows the standard Connector setup of: 

* Pickup taxi
* Dropoff taxi
* Adapter read
* Adapter write
* Transformer in
* Transformer out 

{% hint style="info" %}
**Supported Strapi Versions: 3.4x**  
 
{% endhint %}

