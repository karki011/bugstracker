# SCP

### Taxis

SCP also two taxis: 

1. Pickup taxi
2. Drop off taxi

{% hint style="info" %}
Requirements

Ensure that you have both Docker and Docker Compose installed and set up, you will need a private key encoded base64 from the remote server.
{% endhint %}

### Application Purpose

1. The SCP drop-off Taxi application is responsible for synchronizing content to SCP.
2. Right now it only works as target endpoint, also you need to use GitHub pickup taxi as source endpoint.
3. It is important to note that the taxi will create the folder structure under the remote host. Please make sure the user has permissions to do it under the path you configure

 

