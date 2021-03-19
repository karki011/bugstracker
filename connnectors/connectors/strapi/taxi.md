# Taxi

Both taxis relate to a Strapi endpoint by tracking the ID of the endpoint. 

In addition to the endpoint ID, the taxi’s require the appropriate adapter URL to retrieve and deliver data to the system. The pickup taxi requires the read adapter URL while the dropoff taxi requires the write adapter URL. 

Taxis have the following configuration fields: 

* Endpoint ID
  * Passed in via the taxi endpoint URL
  * See Strapi taxi doc.
    * Pickup:
    * dropoff:
* strapiAdapterURL
  * URL for the read/write adapter
  * Pickup taxi requires read adapter URL
  * Dropoff taxi requires write adapter URL

