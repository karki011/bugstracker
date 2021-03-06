---
description: >-
  minikube is local Kubernetes, focusing on making it easy to learn and develop
  for Kubernetes.
---

# minikube

{% hint style="info" %}
## [minikube start](https://minikube.sigs.k8s.io/docs/start/)
{% endhint %}

## Local install

You will need access to the GitHub impulse and impulse-minikube repositories and clone those repos locally.

* [ ] [Impulse repository](https://github.com/motiv-labs/impulse)
* [ ] [impulse-minikube](https://github.com/motiv-labs/impulse-minikube)

In addition to minikube, you will need to have Helm installed.

* [ ] [Install Helm](https://helm.sh/docs/intro/install/)

minikube gives the option to run with a variety of VM drivers. The following steps use the docker driver. minikube was configured to use 4 CPUs and 20000MB of memory. Certain applications, such as Elasticsearch, require a specific amount of memory. This config ensures that Impulse will be able to run with dotCMS.

You can set this config as default by running the following commands. 

```text
minikube config set driver docker
minikube config set memory 20000
minikube config set cpus 4
```

Once minikube’s config is set you can start it with: 

```text
minikube start
```

 You can also simply start minikube with those settings if you don’t want to have them as default. 

```text
minikube start --driver=docker --memory=20000 --cpus=4
```

Once minikube is started you can then mount Impulse’s Janus files into minikube. \(This is a good time to check that Janus’ auth config is setup correctly\)

Open a new terminal and run the mount command.

```text
minikube mount <checkout location>/impulse/janus:/janus
```

After minikube is started you will need to create a secret so that the docker images are able to be pulled from motivlabs’ private repos. Run a command like this:  

```text
kubectl create secret docker-registry regsecret3 --docker-username=<username> --docker-password=<password> --docker-email=<email>
```

minikube can start a dashboard UI that helps to view the status of everything. You can use it to check that Impulse is starting up correctly. Open a new terminal and run**:** 

```text
minikube dashboard
```

 

