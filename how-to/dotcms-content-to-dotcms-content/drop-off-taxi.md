# Drop off taxi

{% tabs %}
{% tab title="cURL" %}
```text

curl -X PUT "http://localhost:8080/private/taxi-dropoff-dotcms/config/8eb1794f-b0e7-45f0-911d-45c2dd2798c6" -H "Content-Type: application/json" -d "{\"dotCMSAdapterURL\":\"http://dotcms-5.2.7-adapter-write-app:8080\"}"

```
{% endtab %}

{% tab title=".http file" %}
```text
PUT http://localhost:8080/private/taxi-dropoff-dotcms/config/8eb1794f-b0e7-45f0-911d-45c2dd2798c6
Content-Type: application/json
{
  "dotCMSAdapterURL": "http://dotcms-5.2.7-adapter-write-app:8080"
}
```
{% endtab %}
{% endtabs %}

