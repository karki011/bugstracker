# DropOffTaxi configuration

**Add the proper values to environment under docker-compose.yml:**

```text

KAFKA_CONSUMER_SYNC_REQUEST_TOPIC=                                       
KAFKA_PRODUCER_TRANSFORM_TOPIC=
KAFKA_CONSUMER_RAW_DATA_TOPIC=
```

  
****For example:  
  
 `KAFKA_CONSUMER_SYNC_REQUEST_TOPIC=dotcms-5.2.7-dropoff-taxi                  
KAFKA_PRODUCER_TRANSFORM_TOPIC=sync-manager-dropoff-taxi-transformer-out  
KAFKA_CONSUMER_RAW_DATA_TOPIC=dotcms-5.2.7-dropoff-taxi-raw-data`

