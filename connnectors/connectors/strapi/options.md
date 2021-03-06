# Job-&gt;Endpoint-&gt;Details Option

#### Sending specific contents of collection/single types. 

To get the content of a collection type \(or a single type\) you will need to provide the API ID of the content type in the details of the endpoint like this:  
  
**`"detail": "contentType:application::<api-id>.<api-id>"`**  
  
Example:    
**`"detail": "contentType:application::my-type.my-type"`** 

#### Syncing media files from the media library

Media files in the media library are treated as files that live under a path. As such the details to get files would be as follows:  
  
**`"detail": "path:<path/to/file(s)>"`**  
  
Example 1: all media files  
**` "detail": "path:/upload/files" `**  
  
Example 2: specific media file with Id 1  
` `**`"detail": "path:/upload/files/1"`**` `  
  
Example 3: media files in a range  
**`"detail": "path:/upload/files?_limit=2&_start=2"`**` `  
This example will get all media files within the query range. I.e. 2 files starting at the second in the list.  

{% hint style="warning" %}
Note: This list may change order. It is based on modification date of the files. You may want to verify the query before using it. 
{% endhint %}

1. syncuploaddir flag  Because strapi doesn’t quite maintain the concept of a file system in the same way that other CMS do, by default the parent path of media files is simply “/” Setting the syncuploaddir flag will make it so that the parent path is set to “`/uploads/<strapi_file_hash>`”. This then matches the path that the file lives at in the Strapi system**.**   Use the flag like this:  **`"detail": "path:syncuploaddir:<path/to/file(s)>"`**` `

{% hint style="warning" %}
Note: this does not conform to our current standards and will be changed. Use with caution.
{% endhint %}

#### **Getting dependencies**

Dependencies in Strapi are: 

* Relation field
* Media field

To sync the data of these fields you will need to set the dependency depth to the appropriate level. The flag can be used as follows:   
**`"detail": "dependenciesdepth:<depth limit>"`**` `  
  
Example: get dependencies 1 level deep  
**`"detail": "dependenciesdepth:1"`**` `  
  This will get any media files and related contents for a content of a collection type that is directly on the content. Any content that has a relationship to the related content will not be picked up. 

{% hint style="info" %}
I.e. Collection type, my-type, has a media field and a one-to-one relationship field with related-type. related-type has its own media field. A depth of 1 will sync my-type, my-type’s media, and related-type. It will not sync related-type’s media field. 
{% endhint %}

**Deliver Content Type** 

 This flag allows the Strapi destination to ignore the content model \(collection types, single types, and components\) and only sync the content data.    
  
This flag will default to true   
**`"detail": "deliver-contentType:<True|False>"`**` `  
When setting this flag to False, it is then expected that the content model is fully managed through other options. I.e. Another job, manually, etc.   
  
If the content models do not match between source and destination the content may not sync as expected.   
Example: don’t deliver content typ e  
`"detail": "deliver-contentType:False`**"** 

