---
description: Getting started with impulse docker image.
---

# ⚙️ Start Impulse UI

{% hint style="info" %}
Note: the following steps assume impulse is running in docker compose
{% endhint %}

To setup and start running the UI you can simply pull the docker file from docker hub and run it. You can pull the image from motivlabs/impulse-ui.

```text
docker pull motivlabs/impulse-ui:latest
```

After pulling the image run the container 

```text
docker run -p 80:80 --name impulse-ui motivlabs/impulse-ui:latest
```

Once you have the image you will need to connect it to the same network that the rest of Impulse is on.  

```text
docker network connect docker-tools_motiv-impulse-net impulse-ui
```

