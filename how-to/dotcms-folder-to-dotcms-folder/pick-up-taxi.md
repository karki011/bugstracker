---
description: Source endpoint config
---

# Pick up taxi

### **Source endpoint config**

{% tabs %}
{% tab title="cURL" %}
```text
curl -X PUT "http://localhost:8080/private/taxi-pickup-dotcms/config/2e96da36-60a6-4937-9457-7b682aa546dc" -H "Content-Type: application/json" -d "{\"dotCMSAdapterURL\":\"http://dotcms-5.2.7-adapter-read-dotCMS-source1-app:8080\"}"
```
{% endtab %}

{% tab title=".http file" %}
```text
PUT http://localhost:8080/private/taxi-pickup-dotcms/config/2e96da36-60a6-4937-9457-7b682aa546dc
Content-Type: application/json
{
  "dotCMSAdapterURL": "http://dotcms-5.2.7-adapter-read-dotCMS-source1-app:8080"
}
 
```
{% endtab %}
{% endtabs %}

### **Destination endpoint config**

{% tabs %}
{% tab title="cURL" %}
```text
curl -X PUT "http://localhost:8080/private/taxi-pickup-dotcms/config/8eb1794f-b0e7-45f0-911d-45c2dd2798c6" -H "Content-Type: application/json" -d "{\"dotCMSAdapterURL\":\"http://dotcms-5.2.7-adapter-read-dotCMS-destination1-app:8080\"}"
```
{% endtab %}

{% tab title=".http file" %}
```text
PUT http://localhost:8080/private/taxi-pickup-dotcms/config/8eb1794f-b0e7-45f0-911d-45c2dd2798c6
Content-Type: application/json
{
  "dotCMSAdapterURL": "http://dotcms-5.2.7-adapter-read-dotCMS-destination1-app:8080"
}
```
{% endtab %}
{% endtabs %}

