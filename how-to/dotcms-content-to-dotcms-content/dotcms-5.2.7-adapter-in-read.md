# dotCMS 5.2.7 adapter IN / Read

We are syncing two dotCMS instances and each of the dotCMS instances needs to have an adapter container, meaning two adapters IN/Read. 

#### **Source dotCMS**

{% tabs %}
{% tab title="cURL" %}
```text

curl -X PUT "http://localhost:8095/config/data/shared/assets" -H "Content-Type: application/json" -d "{\"dbUser\":\"dotcmsdbuser\",\"dbPassword\":\"password\",\"dbConnectionURL\":\"postgres://dotcms-db-source1:5432/dotcms\",\"dotCMSTaxiDispatcherURL\":\"http://dotcms-5-2-7-pickup-taxi-app:8080\",\"assetsPath\":\"/data/shared/assets\"}"

```
{% endtab %}

{% tab title=".http file" %}
```text
PUT http://localhost:8095/config/data/shared/assets
Content-Type: application/json
{
  "dbUser": "dotcmsdbuser",
  "dbPassword": "password",
  "dbConnectionURL": "postgres://dotcms-db-source1:5432/dotcms",
  "dotCMSTaxiDispatcherURL": "http://dotcms-5-2-7-pickup-taxi-app:8080",
  "assetsPath": "/data/shared/assets"
}
```
{% endtab %}
{% endtabs %}

####  **Destination dotCMS** 

{% tabs %}
{% tab title="cURL" %}
```text

curl -X PUT "http://localhost:8096/config/data/shared/assets" -H "Content-Type: application/json" -d "{\"dbUser\":\"dotcmsdbuser\",\"dbPassword\":\"password\",\"dbConnectionURL\":\"postgres://dotcms-db-destination1:5432/dotcms\",\"dotCMSTaxiDispatcherURL\":\"http://dotcms-5-2-7-pickup-taxi-app:8080\",\"assetsPath\":\"/data/shared/assets\",\"defaultLanguageCode\":\"en\",\"defaultCountryCode\":\"US\"}"

```
{% endtab %}

{% tab title=".http file" %}
```text
PUT http://localhost:8096/config/data/shared/assets
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

{% hint style="info" %}
NOTE: Please note the destination has more information than the source and it is because we are configuring in this step data that will be required for the Adapter OUT/Write. 
{% endhint %}

