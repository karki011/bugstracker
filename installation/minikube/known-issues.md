# Known Issues

All microservices stop communication with Kafka

While working locally, we noticed an error where after running for too long, all the microservices would stop communicating with Kafka. 

{% tabs %}
{% tab title="Example Error" %}
dotcms-5-2-7-pickup-taxi-app           \| time="2020-07-09T02:18:01Z" level=error msg="Error receiving message from Kafka : error while reading a message: dial tcp 192.168.112.8:9092: i/o timeout" source="entry.go:125"

dotcms-5-2-7-pickup-taxi-app           \| time="2020-07-09T02:18:01Z" level=error msg="Error receiving message from Kafka : error while reading a message: dial tcp 192.168.112.8:9092: i/o timeout" source="entry.go:97"  
 
{% endtab %}
{% endtabs %}

The fix appears to be adding “`dns_search`: .” to each microservice in the **docker-compose.yml file**.

{% tabs %}
{% tab title="Example container" %}
dotcms-5.2.7-transformer-out-app:  
      image:motivlabs/dotcms-5.2.7-transformer-out:latest  
      container\_name: dotcms-5.2.7-transformer-out-app  
      dns\_search: .  
      depends\_on:  
           - diesel  
      environment:  
           - KAFKA\_BROKERS=kafka:9092  
           - KAFKA\_CONSUMER\_TOPIC=dotcms-5.2.7-transformer-out  
           - KAFKA\_PRODUCER\_TOPIC=sync-manager-dropoff-taxi-raw-data  
           - KAFKA\_TOPIC\_REPLICATION\_FACTOR=1  
           - KAFKA\_TOPIC\_NUM\_PARTITIONS=1  
           - DIESEL\_URL=http://diesel:8080  
           - DIESEL\_MOTATION\_BUCKET=motation  
      networks:  
          - motiv-impulse-net
{% endtab %}
{% endtabs %}



