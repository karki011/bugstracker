# Global Connector Options

### **Job-&gt;Endpoint-&gt;Details**

 **always-deliver**  
  
The always-deliver flag is a global flag that can be set on all endpoints.   
  
If set to “`True`” it will skip the transformation out of **motation** and send the raw data directly from the pickup taxi to the dropoff taxi. 

If set to “False” it will always transform out of **motation** and build the raw data from the **motation**.

It is set as follows:  
**`"detail": "always-deliver:<True|False>"`**` `  
 

