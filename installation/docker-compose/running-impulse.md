# Running Impulse

There are different docker-compose commands used to start impulse based on what content you want to sync. 

Start by pathing to the root Impulse. 

```text
cd <checkout location>/impulse
```

Then choose what you want to start Impulse with.

### **Impulse Only**

```text

docker-compose -f docker-tools/docker-compose.yml up --build

```

###  **Impulse and Source dotCMS** 

```text
docker-compose -f docker-tools/docker-compose.yml -f docker-tools/docker-compose-dotCMS-source1.yml up --build
```

###  **Impulse and Destination dotCMS**

```text
docker-compose -f docker-tools/docker-compose.yml -f docker-tools/docker-compose-dotCMS-destination1.yml up --build
```

**Impulse, Source dotCMS, and Destination dotCMS**

```text
docker-compose -f docker-tools/docker-compose.yml -f docker-tools/docker-compose-dotCMS-source1.yml -f docker-tools/docker-compose-dotCMS-destination1.yml up --build
```

