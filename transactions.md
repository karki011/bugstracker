# Transactions

**Transactions** are used to track a sync while it is in progress. A transaction will track what job is running, what the source and destination are, start and end time, and details as it progresses through the sync process.   
  
The details show where the sync currently is. If it’s looking for the job, or moving data from the source, or close to finishing by moving data to the destination. All that information is found in the transactions.  

#### The structure of a transaction is as follows: 

* id
  * UUID of the transaction
* jobId
  * UUID of the related job
* startDateTime
  * Start time of the transaction
* endDateTime
  * End time of the transaction
* active
  * Shows whether the transaction is still on going or finished
* details
  * An array of details that show the progress of the transaction

#### The structure for the details of a transaction is as follows: 

* transactionId
  * UUID of the transaction
* detailId
  * UUID of the detail for the transaction
* detailDateTime
  * Time that the detail happened
* type
  * Kafka topic for the detail. This tells what microservice is working on the sync
* detailData
  * Information related to what the detail did

