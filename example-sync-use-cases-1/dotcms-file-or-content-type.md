# dotCMS File\|Content Type

### **dotCMS File\|Content Type Content Type to dotCMS File\|Content Type Content Type** 

* **Summary** - Impulse makes decisions on how to handle and map content coming from and into dotCMS using dotCMS’s Content Type’s Type.  In dotCMS a Content Type can be things like Content, File, Widget, Form, etc. 
  * **NOT IMPLEMENTED YET** -  ONLY Content and Files are currently implemented.  No other types are implemented yet
* **Flow** - a dotCMS to dotCMS Sync will happen either manually or automatically via preconfigured Jobs within Impulse.  Each Job within Impulse has its own Config which can be placed in the Job.Endpoint.Detail. 
  * A Job will start because one of the two conditions 
    * A user will fire a preconfigured Job
    * A preconfigured Job will get triggered \(ie… via a predefined time; run every hour or run every night at 1 AM\). 
      * **NOT IMPLEMENTED YET** - Impulse we have other triggers integrating into more of a workflow concept 
  * Impulse will consume the dotCMS Content which will be of Content Type File or Content into Motation so it can be delivered to any Destination.  All necessary information is captured. 
    * The Content in Motation will be recognized as a File or Content respectively 
  * NOT IMPLEMENTED YET - It is possible that the Content coming in is LESS rich than the existing Motation Impulse has.  This could be because the SAME Content lives in another location. In this case, we need to merge the proper data together so Information is not lost. 
  * Assuming the Files or Content are not already on the Destinations Impulse will Deliver the Content and Files to all the Destination servers configured for the Job using the properties in the Job.Endpoint.Detail field
  * For this use case, we are assuming the Job had a dotCMS Server setup as the Destination Endpoint
  * On Delivery to dotCMS, Impulse’s dotCMS Adapter will 
    * Create the File.  
    * If the File already exists meaning the by File Name and Path it will Update the File 
      * The Path starts from the ROOT\_PATH configured in the Job.Endpoint.Detail
    * All necessary Folders will be created
    * **NOT IMPLEMENTED YET** - The Content Type will be created and/or Used based on the config of the Detail in the Job.Endpoint.Detail 
    * **NOT IMPLEMENTED YET** - Hosts and Users that do NOT exist will NOT be created and the Content will fail

