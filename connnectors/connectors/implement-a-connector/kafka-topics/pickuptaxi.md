# PickupTaxi configuration

### Configuration

Add the proper values to environment under docker-compose.yml:

```text
KAFKA_SYNC_PICKUP_TAXI_IMMUTABLE_IDS_TOPIC=                                       
KAFKA_DIFFUSER_REQUEST_RAW_DATA_TOPIC=
KAFKA_SYNC_PICKUP_TAXI_RAW_DATA_TOPIC=
KAFKA_TAXI_TOPIC=   
```

For example: 

```text
KAFKA_SYNC_PICKUP_TAXI_IMMUTABLE_IDS_TOPIC=sync-manager-pickup-taxi-immutable-ids
KAFKA_DIFFUSER_REQUEST_RAW_DATA_TOPIC=dotcms-5-2-7-pickup-taxi-raw-data
KAFKA_SYNC_PICKUP_TAXI_RAW_DATA_TOPIC=sync-manager-pickup-taxi-raw-data
KAFKA_TAXI_TOPIC=dotcms-5-2-7-pickup-taxi-immutables  
```

