# GitHub to dotCMS

## **GitHub to dotCMS**

* **Summary** - At the end of the day GitHub is a Content Repository that only supports a single Content Type.  For the purposes of Impulse, we consider this Content Type to be a simple File Content Type. GitHub would typically be used for some kind of  CI/CD process.  For example, a Git Repository where developers commit some code or scripting file that is version controlled in Git but when committed to the specified branch Impulse will Sync the file to ONE to MANY Content Repositories.  In addition to this Impulse will store a version of this file in Motation to aid in all other Impulse features.  
  * Currently, GitHub is **ONLY** a _Source_ and not a _Destination._
* **Flow** -  Your GitHub Repository will have a Webhook set up with the proper configuration to integrate Impulse. This configuration is explained later in this manual but it is pretty easy to set up. In addition to this, there must be a Job configured within Impulse that supports the GitHub Repo and Webhook 
  * A user will push a file to a branch that is configured in the GitHub Webhook for Impulse. 
  * Impulse will consume the GitHub Content into Motation so it can be delivered to any Destination.  All necessary information is captured 
  * **NOT IMPLEMENTED YET** - It is possible that the File coming in from GitHub is LESS rich than the existing Motation Impulse has.  This could be because the **SAME** File lives in another location. In this case, we need to merge the proper data together so Information is not lost. 
  * Assuming the files are not already on the Destinations Impulse will Deliver the Files from the GitHub Commit to all the Destination servers configured for the Job. 
  * For this use case, we are assuming the Job had a dotCMS Server setup as the Destination Endpoint
  * On Delivery to dotCMS, Impulse’s dotCMS Adapter will 
    * Create the File.  
    * If the File already exists meaning the by File Name and Path it will Update the File 
      * The Path starts from the ROOT\_PATH configured in the Job.Endpoint.Detail
    * All necessary Folders will be created
    * **NOT IMPLEMENTED YET** - Hosts and Users that do NOT exist will NOT be created and the Content will fail
    * **NOT IMPLEMENTED YET** - The Content Type will be created and/or Used based on the config of the Detail in the Job.Endpoint.Detail  

