---
description: Bring Impulse using Google Cloud.
---

# Bring up Impulse

The first step to bring Impulse up is to [create a project](https://cloud.google.com/appengine/docs/standard/nodejs/building-app/creating-project) for Impulse in Google Cloud. 

Once the project is created, you can run the “`automate-gcloud-kube.sh`” script found in the impulse-google ****cloud repo. This script will go through the process of setting up persistent drives, populating them with the appropriate data, creating a cluster, and deploying Impulse and 2 dotCMS instances. 

```text
./automate-gcloud-kube.sh -p <project_name> -z <zone> -u <docker_user> -s <docker_password> -e <docker_email>
```

{% hint style="info" %}
This script will take a few minutes to fully run. Once the script is finished you can track the status of Impulse by using kubectl.  ****
{% endhint %}

```text
kubectl get pods 
```

Use the following command to check if all the proper ports are exposed yet and get their IP addresses. There should be 6 values in the “EXTERNAL-IP” column. These IP addresses will be how you interact with Impulse, dotCMS, and the adapters.  

```text
kubectl get services
```

