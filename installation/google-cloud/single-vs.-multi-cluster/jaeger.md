# Jaeger

## Single cluster

When running the adapters in the same cluster as Impulse, you can set the jaeger agent to be injected as a sidecar to the adapter. You can do that by adding this line to the metadata.annotations section of the adapter yaml file\(s\).

```text
"sidecar.jaegertracing.io/inject": "true"
```

## Multi cluster

When running the adapters in a separate cluster from Impulse, the adapters will require specific config to be able to use the traces they create. 

The Jaeger collector will need to be able to be reached by an external REST call. This might mean exposing the IP address with a service or editing the existing service to expose an IP address.  
  
The adapter will need to have the environment variable JAEGER\_ENDPOINT set to the address of the Jaeger collector. i.e. `http://<jaeger_collector_IP>:14268/api/traces`

This will allow the adapter to send its traces directly to the Jaeger collector, bypassing the agent.   
 

