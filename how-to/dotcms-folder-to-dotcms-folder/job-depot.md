---
description: Post example using a folder
---

# Job Depot

cURL

```text
curl -X PUT "http://localhost:8080/private/job-depot/jobs/33791608-58fc-4aef-a3de-42ba71ce0e55" -H "Content-Type: application/json" -d "{\"name\":\"dotcms-to-dotcms-job-folder\",\"type\":\"manual\",\"description\":\"dotCMS to dotCMS job\",\"active\":true,\"endpoints\":[{\"id\":\"2e96da36-60a6-4937-9457-7b682aa546dc\",\"type\":\"source\",\"detail\":\"path:default://folder1/\"}, {\"id\":\"9538b3c8-d7c8-4602-80a7-20bb00599508\",\"type\":\"destination\",\"detail\":\"path:default://folder1/\"}]}"
```

.http file 

```text
PUT http://localhost:8080/private/job-depot/jobs/33791608-58fc-4aef-a3de-42ba71ce0e55
Content-Type: application/json
{
  "name": "dotcms-to-dotcms-job",
  "type": "manual",
  "description": "dotCMS to dotCMS job",
  "active": true,
  "endpoints": [
    {
      "id": "2e96da36-60a6-4937-9457-7b682aa546dc",
      "type": "source",
      "detail": "path:default://folder1/"
    },
    {
      "id": "8eb1794f-b0e7-45f0-911d-45c2dd2798c6",
      "type": "destination",
      "detail": "path:default://folder1/"
    }
  ]
}
```



