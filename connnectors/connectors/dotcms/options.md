# Options

### Job-&gt;Endpoint-&gt;Details

1. Sending specific contentlets:  


   Example1: Specifying the host name   
   **`"detail": "path:demo.dotcms.com://content.ef67af58-c36b-4127-afb6-03928ad41673"`**  
    

   Example2: Without a host name 

   **`"detail": "path:/content.ef67af58-c36b-4127-afb6-03928ad41673"`**

  
   Where `content.ef67af58-c36b-4127-afb6-03928ad41673` is the asset name of the contentlet to sync in the identifier table and it lives in the root folder \(parent path == /\)  


   * If no **hostname** is provided the adapter will use the default host.
   * The provided **hostname** needs to exist otherwise the adapter will fail \(we need to fix this\).

    

2. **Using a folder to sync files under it**  


   Example1: Specifying the host name

   **`"detail": "path:demo.dotcms.com://folder1/"`**

  
   Example2: Without a host name  
   **`"detail": "path:/folder1/"`**   


   * If no **hostname** is provided the adapter will use the default host.
   * The provided **hostname** needs to exist otherwise the adapter will fail \(we need to fix this\). 

3. Using a content type to sync contentlets of the given Content Type type

   Example**:**  **`"detail": "contentType:webPageContent"`**

4. Avoid transformer-out **motation-&gt;rawdata**: If the target **JobEndpoint** detail has the property “**`always-deliver:true`**”. It means that the endpoint will use the same **rawData** that it already retrieved from the source endpoint. If the property is not there or false, it means that rawData will be transformed using the motation + transformer-out.  
  
   Example :  
   **`"detail": "path:default://github/,location.site:default,location.path:/github/,always-deliver:true"`** 

### **Combining endpoint**

 It is possible to have under the same detail multiple paths separated by comma and to combine them with the Content Type option.

{% hint style="info" %}
**NOTE: Only one Content Type option is allowed.**
{% endhint %}

 **`"endpoints": [  
    {  
      "id": "2e96da36-60a6-4937-9457-7b682aa546dc",  
      "type": "source",  
      "detail": "path:demo.dotcms.com://folder1/,path:/folder2/,contentType:webPageContent"  
    },  
    ...    ...  
  ]`** 

