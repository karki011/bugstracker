# Local Install

#### You will need access to the GitHub impulse repository locally [Impulse repository](https://github.com/motiv-labs/impulse)

**Docker Hub** is used to store our images, you will need to login to docker hub to gain access to the images. Currently you will need to use the motivlabs credentials. Modify the following command to login. 

```text
docker login --username <username> --password <password>
```

If you want to run the included dotCMS instances you will need to provide more memory to the Docker containers. Based on your OS follow the instructions at this link to adjust the memory.

 [https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html\#docker-prod-prerequisites](https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html#docker-prod-prerequisites)  
 

