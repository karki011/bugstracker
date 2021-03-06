# Taxi/adapter communication

## Single cluster

The first thing to be aware of is the communication required between the taxis and the adapters. The adapters and taxis require the ability to make REST calls to the other each other. 

When running in the same cluster, this doesn’t require special configuration other than the proper internal networking of cluster for the adapter and taxis to communicate with each other. I.e. services

## Multi cluster

When running in separate clusters, this means that the adapters and taxis need to have some sort of exposure.  
  
For the adapters, you can simply open up the ip address for communication.  
For the taxis, you can use Janus to open up the specific REST endpoint that the adapters require. Example files can be found in the Impulse repo.

  
When exposing the adapters and taxis for cross cluster communication, you should have a proper firewall and network traffic monitoring infrastructure in place.  

