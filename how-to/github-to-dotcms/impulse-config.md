# Impulse Config

You will want to start impulse with a destination dotCMS

### Setting up the endpoints against the motivlabs/endpoint-depot

* **GitHub endpoint**

{% tabs %}
{% tab title="cURL" %}
```text
curl -X PUT "http://localhost:8080/private/endpoint-depot/endpoints/0e5bf526-4177-4b85-9e4f-3f64a083db5a" -H "Content-Type: application/json" -d "{\"name\":\"github-endpoint\",\"contentRepo\":\"github\",\"contentRepoVersion\":\"latest\",\"active\":true}"
```
{% endtab %}

{% tab title=".http file" %}
```text
PUT http://localhost:8080/private/endpoint-depot/endpoints/0e5bf526-4177-4b85-9e4f-3f64a083db5a
Content-Type: application/json
{
 "name" : "github-endpoint",
 "contentRepo" : "github",
 "contentRepoVersion" : "latest",
 "active" : true
}
```
{% endtab %}
{% endtabs %}



* **dotCMS endpoint**

{% tabs %}
{% tab title="cURL" %}
```text
curl -X PUT "http://localhost:8080/private/endpoint-depot/endpoints/06a87708-815f-48a8-80d9-d2aaccd855ac" -H "Content-Type: application/json" -d "{\"name\":\"dotcms-endpoint\",\"contentRepo\":\"dotcms\",\"contentRepoVersion\":\"5.2.7\",\"active\":true}"
```
{% endtab %}

{% tab title=".http file" %}
```text
PUT http://localhost:8080/private/endpoint-depot/endpoints/06a87708-815f-48a8-80d9-d2aaccd855ac
Content-Type: application/json
{
 "name" : "dotcms-endpoint",
 "contentRepo" : "dotcms",
 "contentRepoVersion" : "5.2.7",
 "active" : true
}
```
{% endtab %}
{% endtabs %}

#### Save the config for the motivlabs/github-webhook-listener

* Be sure to point to your chosen GitHub repo and use the correct secret

{% tabs %}
{% tab title="cURL" %}
```text
curl -X PUT "http://localhost:8080/private/github-webhook-listener/config/motiv-solutions/poc" -H "Content-Type: application/json" -d "{\"secretField\":\"abc123\"}"
```
{% endtab %}

{% tab title=".http file" %}
```text
PUT http://localhost:8080/private/github-webhook-listener/config/motiv-solutions/poc
Content-Type: application/json
{
"secretField" : "abc123"
}
```
{% endtab %}
{% endtabs %}

#### Save the config for the motivlabs/github-taxi-driver

* Be sure to point to your chosen GitHub repo and use the correct oAuth key 

{% tabs %}
{% tab title="cURL" %}
```text
curl -X PUT "http://localhost:8080/private/taxi-pickup-github/config/motiv-solutions/poc" -H "Content-Type: application/json" -d "{\"oAuthKey\":\"not-needed\"}"
```
{% endtab %}

{% tab title=".http file" %}
```text
PUT http://localhost:8080/private/taxi-pickup-github/config/motiv-solutions/poc
Content-Type: application/json
{
 "oAuthKey" : "not-needed"
}
```
{% endtab %}
{% endtabs %}

#### Save the config for the motivlabs/dotcms-5-2-7-pickup-taxi

{% tabs %}
{% tab title="cURL" %}
```text
curl -X PUT "http://localhost:8080/private/taxi-pickup-dotcms/config/06a87708-815f-48a8-80d9-d2aaccd855ac" -H "Content-Type: application/json" -d "{\"dotCMSAdapterURL\":\"http://dotcms-5.2.7-adapter-read-dotCMS-destination1-app:8080\"}"
```
{% endtab %}

{% tab title=".http file" %}
```text
PUT http://localhost:8080/private/taxi-pickup-dotcms/config/06a87708-815f-48a8-80d9-d2aaccd855ac
Content-Type: application/json 
{
 "dotCMSAdapterURL": "http://dotcms-5.2.7-adapter-read-dotCMS-destination1-app:8080"
}
```
{% endtab %}
{% endtabs %}

#### Save the config for the motivlabs/dotcms-5.2.7-dropoff-taxi

{% tabs %}
{% tab title="cURL" %}
```text
curl -X PUT "http://localhost:8080/private/taxi-dropoff-dotcms/config/06a87708-815f-48a8-80d9-d2aaccd855ac" -H "Content-Type: application/json" -d "{\"dotCMSAdapterURL\":\"http://dotcms-5.2.7-adapter-write-app:8080\"}"
```
{% endtab %}

{% tab title=".http file" %}
```text
PUT http://localhost:8080/private/taxi-dropoff-dotcms/config/06a87708-815f-48a8-80d9-d2aaccd855ac
Content-Type: application/json
{
 "dotCMSAdapterURL": "http://dotcms-5.2.7-adapter-write-app:8080"
}
```
{% endtab %}
{% endtabs %}

#### Save the config for the motivlabs/adapter-dotcms-5-2-7

`### dotCMS adapter in config  
PUT http://localhost:8096/config/data/shared/assets`

{% tabs %}
{% tab title="cURL" %}
```text
curl -X PUT "http://localhost:8096/config/data/shared/assets" -H "Content-Type: application/json" -d "{\"dbUser\":\"dotcmsdbuser\",\"dbPassword\":\"password\",\"dbConnectionURL\":\"postgres://dotcms-db-destination1:5432/dotcms\",\"dotCMSTaxiDispatcherURL\":\"http://dotcms-5-2-7-pickup-taxi-app:8080\",\"assetsPath\":\"/data/shared/assets\",\"defaultLanguageCode\":\"en\",\"defaultCountryCode\":\"US\"}"
```
{% endtab %}

{% tab title=".http file" %}
```text
Content-Type: application/json
{
 "dbUser": "dotcmsdbuser",
 "dbPassword": "password",
 "dbConnectionURL": "postgres://dotcms-db-destination1:5432/dotcms",
 "dotCMSTaxiDispatcherURL": "http://dotcms-5-2-7-pickup-taxi-app:8080",
 "assetsPath": "/data/shared/assets",
 "defaultLanguageCode": "en",
 "defaultCountryCode": "US"
}
```
{% endtab %}
{% endtabs %}

#### Save the config for the motivlabs/job-depot

* The endpoint detail: `pathpath:demo.dotcms.com://pdfs/` should be updated to where you want to save the GitHub commit.

`I.e. pathpath:demo.dotcms.com://my-github-commits/`

{% tabs %}
{% tab title="cURL" %}
```text
curl -X PUT "http://localhost:8080/private/job-depot/jobs/765143d8-7cb7-44b9-bbb8-b538b2d21056" -H "Content-Type: application/json" -d "{\"name\":\"github-to-dotcms-job\",\"type\":\"manual\",\"description\":\"GitHub to dotCMS job\",\"active\":true,\"endpoints\":[{\"id\":\"0e5bf526-4177-4b85-9e4f-3f64a083db5a\",\"type\":\"source\"}, {\"id\":\"06a87708-815f-48a8-80d9-d2aaccd855ac\",\"type\":\"destination\",\"detail\":\"path:demo.dotcms.com://my-github-commits/\"}]}"
```
{% endtab %}

{% tab title=".http file" %}
```text
### Job GitHub - dotCMS 5.2.7
PUT http://localhost:8080/private/job-depot/jobs/765143d8-7cb7-44b9-bbb8-b538b2d21056
Content-Type: application/json
{
 "name": "github-to-dotcms-job",
 "type": "manual",
 "description": "GitHub to dotCMS job",
 "active": true,
 "endpoints": [
  {
   "id": "0e5bf526-4177-4b85-9e4f-3f64a083db5a",
   "type": "source"
  },
  {
   "id": "06a87708-815f-48a8-80d9-d2aaccd855ac",
   "type": "destination",
   "detail": "path:demo.dotcms.com://pdfs/"
  }
 ]
}
```
{% endtab %}
{% endtabs %}

