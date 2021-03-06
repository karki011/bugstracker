# Impulse Pieces

Impulse requires a few pieces of information to start syncing content. 

* Jobs
* Endpoints

  * Endpoints Configs

  Sometimes It requires additional information based on source and destination location. 

* Adapter config
* Webhook listener config

## **How it works**

 A sync requires a job. A job requires endpoints. Endpoints then each need a config.   
  
Endpoints are sources and destinations. Endpoints contain the information required to connect source and destinations, such as Github and dotCMS. Each endpoint tells what the site is and the config tells the location and includes authentication needed.   
  
Jobs use endpoints to access locations and determine which are sources or destinations. A job has a list of endpoints which declare if an endpoint is a source or destination. A job also includes details for each endpoint which determine what data should be synced from source endpoints and where it should be synced in destination endpoints.   
  
Once a job exists and has endpoints with configs, a sync can be started.  
 

