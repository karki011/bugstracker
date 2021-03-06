# dotCMS

### Taxis

dotCMS also two taxis: 

1. Pickup taxi
2. Drop off taxi

They should both relate to a dotCMS endpoint by tracking its ID. 

They also get an adapter URL to be able to connect to dotCMS database. The pickup taxi will point to the read adapter and the drop off taxi will point to the write adapter.

Taxis have the following configuration fields: 

* repoId
  * ID of the related endpoint
* dotCMSAdapterURL
  * URL for the read/write adapter
  * Pickup taxi requires read adapter URL
  * Drop off taxi requires write adapter URL

### Adapters

In addition to the connectors dotCMS requires the use of adapters. 

1. Read adapter
2. Write adapter

These adapters take configurations to allow it to access the database, view the assets, and communicate with the taxis. 

Adapters have the following configuration fields: 

* dbUser
  * Username to access the DB
* dbPassword
  * Password to access the DB
* dbConnectionURL
  * Relative connection to the DB
* dotCMSTaxiDispatcherURL
  * Relative connection the to pickup taxi
* assetsPath
  * Relative path to the dotCMS shared assets
* defaultlanguageCode
  * Default code for language
  * Optional for read adapter
  * Required for write adapter
* defaultCountryCode
  * Default code for country
  * Optional for read adapter
  * Required for write adapter
  * 

[ **Write Adapter Doc** ](https://documenter.getpostman.com/view/11567600/T1DmDe9E?version=latest)  
****[**Read Adapter Doc**](https://documenter.getpostman.com/view/11567600/T1DmDe9K?version=latest)  
****

