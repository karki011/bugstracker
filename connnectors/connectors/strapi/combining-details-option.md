# Combining details Option

All the above details can be combined together by separating them with a comma. This allows for one job to sync many types of content.   


{% hint style="info" %}
Note: only one contentType can be synced at a time.  
{% endhint %}

Example 1: Multiple Media Files  
**`"detail": "path:/upload/files/1,path:/upload/files/3"`**` `  
  
Example 2: Collection type and media files   
**`"detail": "contentType:application::my-collection.my-collection,path:/upload/files/3`**  
  
Example 3: With extra flags   
**`"detail": "contentType:application::my-collection.my-collection,path:/upload/files/3,dependenciesdepth:1,deliver-contentType:True,always-deliver:False"`**

