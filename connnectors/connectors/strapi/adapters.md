# Adapters

Strapi has both a Read and Write adapter.   
  
These adapters take configurations that allow it to make the appropriate API calls to strapi to interact with the content.   
  
Currently, adapters require admin authentication so that all the information of a content can be synced. I.e. private fields in a collection type.   
Because the adapters communicate with Strapi through Strapi’s REST API, the JWT timeout for that adapter user should be long enough to complete a sync. 

Adapters have the following configuration fields: 

* strapiURL
  * The relative URL of the strapi instance connected to the database
* strapiTaxiDispatcherURL
  * The relative URL of the pickup taxi
* strapiTaxiDropoffURL
  * The relative URL of the dropoff taxi
* user
  * The username for an admin user
* password
  * The password for the admin user  
  
    [**Write Adapter Doc**](https://documenter.getpostman.com/view/11567600/Tz5s3bn9)\*\*\*\*

    \*\*\*\*[**Read Adapter Doc**](https://documenter.getpostman.com/view/11567600/Tz5s3bnA)

