# dotCMS \(content\) to dotCMS \(content\)

### **Impulse set-up**

 Start Impulse with 2 dotCMS instances

```text
docker-compose -f docker-tools/docker-compose.yml -f docker-tools/docker-compose-dotCMS-5-3-3-source1.yml -f docker-tools/docker-compose-dotCMS-5-3-3-destination1.yml up --build
```

### **End-points set-up** 

#### Source endpoint 

{% tabs %}
{% tab title="cURL" %}
```text

curl -X PUT "http://localhost:8080/private/endpoint-depot/endpoints/2e96da36-60a6-4937-9457-7b682aa546dc" -H "Content-Type: application/json" -d "{\"name\":\"dotCMS-source-endpoint\",\"contentRepo\":\"dotcms\",\"contentRepoVersion\":\"5.2.7\",\"active\":true}"

```
{% endtab %}

{% tab title=".http file" %}
```text
PUT http://localhost:8080/private/endpoint-depot/endpoints/2e96da36-60a6-4937-9457-7b682aa546dc
Content-Type: application/json
{
  "name" : "dotCMS-source-endpoint",
  "contentRepo" : "dotcms",
  "contentRepoVersion" : "5.2.7",
  "active" : true
}
 
```
{% endtab %}
{% endtabs %}

**Destination endpoint** 

{% tabs %}
{% tab title="cURL" %}
```text

curl -X PUT "http://localhost:8080/private/endpoint-depot/endpoints/8eb1794f-b0e7-45f0-911d-45c2dd2798c6" -H "Content-Type: application/json" -d "{\"name\":\"dotCMS-destination-endpoint\",\"contentRepo\":\"dotcms\",\"contentRepoVersion\":\"5.2.7\",\"active\":true}"

```
{% endtab %}

{% tab title=".http file" %}
```text
PUT http://localhost:8080/private/endpoint-depot/endpoints/8eb1794f-b0e7-45f0-911d-45c2dd2798c6
Content-Type: application/json
{
  "name" : "dotCMS-destination-endpoint",
  "contentRepo" : "dotcms",
  "contentRepoVersion" : "5.2.7",
  "active" : true
}
 
```
{% endtab %}
{% endtabs %}

