# Not supported / Known errors

### **Fields** 

All fields work for Strapi to Strapi syncs.

Currently the sync process does not support the following fields when syncing across systems. 

* Relation
* Media
* Component
* Dynamic zone

Currently these fields may sync data with some issues across systems: 

* JSON
* Rich text
* Boolean
* Password

###  **Non-Strapi source sync**

The Strapi connector does not currently support non-Strapi source.   
The Strapi conector currently lacks a transformer-out to take mutation and convert it into Strapi raw data. Without this piece we cannot convert data from a non-Strapi source into a Strapi destination.  

### **Multiple collection types** 

Only 1 collection type can be set in the details. Multiple collection types set in the details will result in only 1 of them being synced.  

### **syncuploaddir flag**

 This flag is not working as intended. 

1. It does not conform to endpoint details flag standards.
2. It is not always respected. 

### **Non-admin user** 

The adapters require a non-admin user to get all the necessary information about content from the source and post it to the destination. We don’t support other types of users.  

###  **Strapi Private Fields**

Private fields are currently picked up. There is no option to choose whether or not they should be included.

### **Sync Single Content**

The details do not currently support getting a single content. All contents of the collection type are gotten.

