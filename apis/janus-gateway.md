# Janus Gateway

{% hint style="info" %}
**Impulse is reached at**  [**http://localhost:8080**](http://localhost:8080/)
{% endhint %}

With Janus’ authentication in place, there are 2 paths that the APIs are behind. 

* Public
  * /public
  * Does NOT require “Authorization” header in request
* Private
  * /private
  * Requires “Authorization” header in request

 Most API endpoints are only accessible through the private path, but a few can use the public path.  

Here is the list of **APIs** that are accessible through Impulse and the path to access them. 

* Sync manager
  * /sync-manager
* Job Depot
  * /job-depot
* Endpoint Depot
  * /endpoint-depot
* GitHub Webhook Listener
  * /github-webhook-listener
* Taxi Pickup GitHub
  * /taxi-pickup-github
* Taxi Pickup dotCMS
  * /taxi-pickup-dotcms
* Taxi Dropoff dotCMS
  * /taxi-dropoff-dotcms
* Diesel
  * /diesel
* Logger
  * /logger
* Note Man
  * /note-man

 Putting it all together, an request to impulse would be akin to:

```text
curl -H “Authorization: Bearer ${jwt}” “http://localhost:8080/private/${api/${endpoint}” 
```

