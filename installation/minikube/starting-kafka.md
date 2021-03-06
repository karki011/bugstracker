# Starting kafka

To start kafka we will be using Helm. This is the repo for the charts that we are using. [https://github.com/confluentinc/cp-helm-charts](https://github.com/confluentinc/cp-helm-charts)

There are two ways to set up Helm. You can get the latest confluentinc charts or use the version provided with Impulse. 

  
Either way path to the root of impulse-minikube. 

```text
cd <checkout location>/impulse-minikube
```

Provided chart 

```text
helm install my-confluent helm/cp-helm-charts-0.5.0.tgz -f helm/values.yaml
```

Latest chart

```text

helm repo add confluentinc https://confluentinc.github.io/cp-helm-charts/
helm repo update
```

To spin up kafka run: 

```text
helm install my-confluent confluentinc/cp-helm-charts -f kubernetes-tools/helm/values.yaml
```

{% hint style="info" %}
**You can check that the services started with:** 

```text
kubectl get svc
```
{% endhint %}



