# Not supported / Known errors

### **Fields**

Currently the sync process does not support the following fields:

* Image: Images are just references to File Assets, we are saving and synchronizing the reference but without the original File Asset the image won’t display. 
* File: : Just as images, file fields are just references to File Assets, we are saving and synchronizing the reference but without the original File Asset the file can not be accessed.
* Tag
* Category
* Relationship

###  **Endpoint details paths:**

As we explained above we can have a detail like this:   
**`"detail": "path:demo.dotcms.com://folder1/"`**  
   
When the hostname is provided that host name must exist on the dotCMS instance otherwise the Adapter Read will fail. 

###  **Locations** 

The Adapter Write supports the concept of locations, locations allow you to override the location of the synced content and support two properties: location.site and location.path, both properties are optional.   
  
Examples:  
**`"endpoints": [  
    {  
      "id": "2e96da36-60a6-4937-9457-7b682aa546dc",  
      "type": "destination",  
      "detail": "location.site:demo.dotcms.com,location.path:/new/path/"  
    }  
  ]`**   


{% hint style="info" %}
**The location properties will only work on the destination instance.** 
{% endhint %}

{% hint style="info" %}
 **Locations are on this section because I’m pretty sure no one is reading those properties so I don’t think they will at this moment get down to the Adapter Write.** 
{% endhint %}

