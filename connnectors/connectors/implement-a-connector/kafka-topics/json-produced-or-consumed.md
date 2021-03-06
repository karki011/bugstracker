# JSON produced or consumed

**JSON produced or consumed**

1. **&lt;endpoint&gt;-pickup-taxi-immutables**

   * Go Structure: ContentSyncRequestPickUpImmutableId

   ```text
   {
      "transactionId": "d788915d-6dda-4e0d-af54-496591d3cc7a",
      "jobEndpoint": {
          "id": "2e96da36-60a6-4937-9457-7b682aa546dc",
          "type": "",
          "detail": ""
      }
   }
   ```

2. **sync-manager-pickup-taxi-immutable-ids** 

   1. Go Structure: ContentSyncRequestWithImmutableIds

   ```text
   {
      "transactionId": "d788915d-6dda-4e0d-af54-496591d3cc7a",
      "jobEndpoint": {
          "id": "2e96da36-60a6-4937-9457-7b682aa546dc",
          "type": "",
          "detail": ""
      },
      "objectId": "37996e78-c97e-4b94-aeaa-806d821f6293",
      "pathToSync": "",
      "totalFiles": 4,
      "fileNumber": 1,
      "contentPath": "8a7d5e23-da1e-420a-b4f0-471e7da8ea2d://folder1/bulbasaur.jpeg",
      "defaultVersion": "f6981425-695f-4a77-8770-9ac7d85e64c5",
      "versions": [
          {
              "systemVersionId": "f6981425-695f-4a77-8770-9ac7d85e64c5",
              "versionName": "live",
              "immutableId": "e47c43a1ff079d3545afd927825903da"
          }
      ]
   }

   ```

3. **&lt;endpoint&gt;-pickup-taxi-raw-data**

   1. Go Structure: RawDataRequest 

   ```text
   {
      "repositoryId":"8eb1794f-b0e7-45f0-911d-45c2dd2798c6",
      "transactionId": "d788915d-6dda-4e0d-af54-496591d3cc7a",
      "objectId": "0bd874cd-32e6-4d0a-9b33-fbfa4c170d8b",
      "versions": [
          {
              "systemVersionId": "59b4332b-0c01-4cba-a609-42d425cee842",
              "versionName": "live",
              "immutableId": "5989d9454ea07eb1b3f0c129c2d5a352"
          }
      ]
   }
   ```

4. **sync-manager-pickup-taxi-raw-data**

   1. Go Structure: ReadyForTransformationPayload  

   ```text
   {
      "transactionId": "d788915d-6dda-4e0d-af54-496591d3cc7a",
      "repositoryId": "2e96da36-60a6-4937-9457-7b682aa546dc",
      "rawDataMD5": "358ebd0f067f2b5843938711092003c7",
      "customDataMap": null
   }
   ```

5. **&lt;endpoint&gt;-transformer-in-raw-data** 

   1. Go Structure: MotationReadyPayload 

   ```text
   {
      "transactionID": "d788915d-6dda-4e0d-af54-496591d3cc7a",
      "endpointId": "2e96da36-60a6-4937-9457-7b682aa546dc",
      "objectId": "0bd874cd-32e6-4d0a-9b33-fbfa4c170d8b",
      "motationId": "c42ea71b8afdd6268df08f21ff7fb6dc",
      "motationVersions": {
          "59b4332b-0c01-4cba-a609-42d425cee842": "59b4332b-0c01-4cba-a609-42d425cee842"
      }
   }
   ```

6. **&lt;endpoint&gt;-dropoff-taxi**

   1. Go Structure: SyncRequestPayload

   ```text
   {
      "transactionId": "d788915d-6dda-4e0d-af54-496591d3cc7a",
      "repositoryID": "2e96da36-60a6-4937-9457-7b682aa546dc",
      "motationMD5": "2358ebd0f067f2b5843938711092003c7",
      "endpoint": {
          "id": "2e96da36-60a6-4937-9457-7b682aa546dc",
          "detail": "path:default://folder1/"
      }
   }
   ```

7. **sync-manager-dropoff-taxi-transformer-out**

   1. Go Structure: TransformPayload 

   ```text
   {
      "transactionId": "d788915d-6dda-4e0d-af54-496591d3cc7a",
      "repositoryId": "8eb1794f-b0e7-45f0-911d-45c2dd2798c6",
      "rawDataMD5": "59affd00503de8ba24bf3847d1bccf6e",
      "customDataMap": null
   }
   ```

8. **sync-manager-dropoff-taxi-raw-data** 

   1. Go Structure: ReadyForSyncPayload

   ```text
   {
      "transactionId": "d788915d-6dda-4e0d-af54-496591d3cc7a",
      "repositoryId": "8eb1794f-b0e7-45f0-911d-45c2dd2798c6",
      "rawDataMD5": "59affd00503de8ba24bf3847d1bccf6e",
      "customDataMap": null
   }
   ```

9. **&lt;endpoint&gt;-dropoff-taxi-raw-data**

   1. Go Structure: RawDataPayload 

   ```text
   {
      "transactionId": "d788915d-6dda-4e0d-af54-496591d3cc7a",
      "repositoryId": "8eb1794f-b0e7-45f0-911d-45c2dd2798c6",
      "rawDataMD5": "cc403f922a1c3327a6d6c9001a7a5964",
      "endpoint": {
          "id": "2e96da36-60a6-4937-9457-7b682aa546dc",
          "detail": ""
      }
   } 
   ```

