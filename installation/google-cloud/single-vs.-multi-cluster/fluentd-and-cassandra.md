# Fluentd & Cassandra

## Single cluster

When running in a single cluster there is no special setup required for Fluentd and Cassandra to connect. Aside from ensuring that the Fluentd config has the correct host for Cassandra \(our default is “db.default.svc.cluster.local”\)

## Multi cluster

When running Fluentd in a separate cluster from Cassandra, you will need to adjust the Cassandra host to connect to, as well as ensure Cassandra is able to be reached from an external source. We solve this by exposing the IP address of the Cassandra service to be an external IP.   
As with the Taxi/Adapter multi-cluster communication, exposing IPs in this way should be accompanied by a proper firewall and network traffic monitoring infrastructure.   
 

