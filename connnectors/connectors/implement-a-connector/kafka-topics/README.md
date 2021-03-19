# Kafka Topics



| Microservice Producing | Microservice Consuming | Topic | Example |
| :--- | :--- | :--- | :--- |
| Sync-Manager | PickupTaxi | &lt;endpoint&gt;-pickup-taxi-immutables | dotcms-5-2-7-pickup-taxi-immutables |
| PickupTaxi | Sync-Manager | sync-manager-pickup-taxi-immutable-ids | sync-manager-pickup-taxi-immutable-ids |
| Sync-Manager | PickupTaxi | &lt;endpoint&gt;-pickup-taxi-raw-data | dotcms-5-2-7-pickup-taxi-raw-data |
| PickupTaxi | Sync-Manager | sync-manager-pickup-taxi-raw-data | sync-manager-pickup-taxi-raw-data |
| Sync-Manager | Transformer-In | &lt;endpoint&gt;-transformer-in-raw-data | dotcms-5-2-7-transformer-in-raw-data |
| Transformer-In | Sync-Manager | sync-manager-transformer-in-motation | sync-manager-transformer-in-motation |
| Sync-Manager | DropOffTaxi | &lt;endpoint&gt;-dropoff-taxi | dotcms-5.2.7-dropoff-taxi |
| DropOffTaxi | Sync-Manager | sync-manager-dropoff-taxi-transformer-out | sync-manager-dropoff-taxi-transformer-out |
| Sync-Manager | Transformer-Out | &lt;endpoint&gt;-transformer-out | dotcms-5.2.7-transformer-out |
| Transformer-Out | Sync-Manager | sync-manager-dropoff-taxi-raw-data | sync-manager-dropoff-taxi-raw-data |
| Sync-Manager | DropOffTaxi | &lt;endpoint&gt;-dropoff-taxi-raw-data | dotcms-5.2.7-dropoff-taxi-raw-data |

