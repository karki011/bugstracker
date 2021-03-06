---
description: How to implement a Connector?
---

# Implement a Connector

### **How to implement a Connector?**

Each connector is composed of Taxis, Adapters and Transformers. If the Connector will retrieve and send info to the Endpoint it will need 2 Taxis. A PickupTaxi and a DropOffTaxi. Each Taxi will need its own Adapter, Adapter-Read for the PickupTaxi and Adapter-Write for the DropOffTaxi. Also each Taxi will have a Transformer, Transformer-In for the PickupTaxi and Transformer-Out for the DropOffTaxi. The Transformer-In will transform raw data into Motation and Transformer-Out will transform Motation into raw data. 

**In summary:**

* Connector
  * PickupTaxi
    * Adapter-Read 
    * Transformer-In
  * DropOffTaxi
    * Transformer-Out
    * Adapter-Write

###  **Communication between microservices**

All the communication is done by Apache Kafka, producing and subscribing to specific topics. All the Kafka messages have to go through Sync Manager. The only exception to this rule is the communication between Taxis and Adapters, this is done by REST cause the adapter will live close to the endpoint and it will not be part of the Impulse infrastructure, meaning it will have no access to Kafka.

